<div align="left">
    <h1>SkyAPI</h1>

## Usage

Now ``skyapi`` if developing

## Installation

```bash
pip install git+https://github.com/AmiCreator/skyapi.git
```

## Requirements

 - ``Python 3.8+``
 - ``aiohttp``

## Features

 - ``Asynchronous``
 - ``Exception handling``


## Basic example for a mandatory subscription with aiogram

```python
from skyapi import SkyNanager

from aiogram import types


skyapi = SkyNanager(KEY)

async def message_handler(message: types.Message):
    # Use it wherever verification is necessary
    if not await flyer.check(message.from_user.id, language_code=message.from_user.language_code):
        return

async def callback_handler(call: types.CallbackQuery):
    # Use it wherever verification is necessary
    if not await flyer.check(call.from_user.id, language_code=call.from_user.language_code):
        return
```

### Using custom message

```python
message = {
    'text': '<b>Custom text</b> for $name',  # HTML

    'button_bot': 'Start',
    'button_channel': 'Subscribe',
    'button_url': 'Follow',
    'button_boost': 'Boost',
    'button_fp': 'Perform',
}
await flyer.check(user_id, language_code=language_code, message=message)
```

## Example for tasks

```python
# Getting tasks for the user
tasks = await flyer.get_tasks(
    user_id=user_id,
    language_code=language_code,  # used only for new pinning
    limit=5,  # used only for new pinning
)

...

# Checking for completed task
status = await flyer.check_task(
    user_id=user_id,
    signature=tasks[0]['signature'],
)


```


Developed by Ami (c) 2025-2026
