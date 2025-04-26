import os
import codecs

from setuptools import setup, find_packages


VERSION = '1.2.0'
DESCRIPTION = 'Async client for Sky mandatory-subscription service'

here = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()


setup(
    name='skyapi',
    version=VERSION,
    author='Ami',
    author_email='<ami.dev.tg@gmail.com>',
    description=DESCRIPTION,
    long_description_content_type='text/markdown',
    long_description=long_description,
    packages=find_packages(),
    install_requires=['aiohttp', 'cachetools'],
    keywords=['python', 'SkyManager', 'async', 'asyncio', 'cache'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: Unix',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
    ],
    url='https://github.com/AmiCreator/skyapi',
    project_urls={
        'Homepage': 'https://github.com/AmiCreator/skyapi',
        'Bug Tracker': 'https://github.com/AmiCreator/skyapi/issues',
    },
)
