from setuptools import setup, find_packages

setup(
    name="skyapi",
    version="0.1.0",
    description="Async client for Sky mandatory-subscription service",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="SkyManager",
    packages=find_packages(),
    install_requires=["aiohttp", "cachetools"],
    python_requires=">=3.8"
)
