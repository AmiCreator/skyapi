import time, logging, aiohttp
from cachetools import TTLCache
from aiohttp.client_exceptions import ClientConnectorError, ContentTypeError

log = logging.getLogger("SkyAPI")

class SkyAPI:
    """
    Minimal async SDK for Sky-service.
    •   check()       – mandatory-subscription check
    •   get_tasks()   – get promo tasks
    •   check_task()  – confirm task
    """

    BASE_URL = "https://api.skymanager.io"      #  ← поменяйте на свой хост

    def __init__(self, key: str, debug: bool = False, **req_kw):
        if not isinstance(key, str):
            raise TypeError("key must be a string")
        self.key = key
        self.debug = debug
        self.req_kw = req_kw
        self.cache = TTLCache(maxsize=10_000, ttl=60)   # 60 с
        self.service_down_till = 0                     # секунд

    # ---- low-level ---------------------------------------------------------
    async def _post(self, method: str, params: dict | None = None) -> dict:
        url = f"{self.BASE_URL}/{method}"
        body = {"key": self.key}
        if params:
            body.update(params)

        async with aiohttp.ClientSession() as sess:
            async with sess.post(url, json=body, **self.req_kw) as r:
                data = await r.json()
                if self.debug:
                    print("SkyAPI>", data)
                return data

    # ---- high-level --------------------------------------------------------
    async def get_me(self) -> dict:
        return await self._post("get_me")

    async def check(self, user_id: int, language_code: str | None = None,
                    message: dict | None = None) -> bool:
        """
        True  → пользователь уже подписан / прошёл проверку
        False → бот должен показать ему обязательные каналы
        """
        if not isinstance(user_id, int) or user_id < 0:
            log.error("user_id must be positive int")
            return True

        now = time.time()
        if now < self.service_down_till:
            return True                                   # сервис недоступен – пропускаем

        # кеш на 60 с
        if self.cache.get(user_id):
            return True

        params = {"user_id": user_id}
        if language_code:
            params["language_code"] = language_code
        if message:
            params["message"] = message

        try:
            res = await self._post("check", params)
        except (ClientConnectorError, TimeoutError):
            self.service_down_till = now + 60
            return True
        except ContentTypeError as e:
            log.error(f"SkyAPI bad JSON: {e}")
            return True
        except Exception as e:
            log.error(f"SkyAPI error: {e}")
            return True

        # обработка полей
        if res.get("skip"):
            self.cache[user_id] = True
        if "error" in res:
            log.error(res["error"])
        return res.get("skip", True)

    async def get_tasks(self, user_id: int, language_code: str | None = None,
                        limit: int | None = None) -> list[dict]:
        params = {"user_id": user_id}
        if language_code:
            params["language_code"] = language_code
        if limit:
            params["limit"] = limit
        return (await self._post("get_tasks", params)).get("result", [])

    async def check_task(self, user_id: int, signature: str, **kw) -> str | None:
        params = {"user_id": user_id, "signature": signature}
        params.update(kw)
        return (await self._post("check_task", params)).get("result")
