# google-scraper-pw
[![tests](https://github.com/ffreemt/google-scraper-playwright/actions/workflows/routine-tests.yml/badge.svg)][![python](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/google-scraper-pw.svg)](https://badge.fury.io/py/google-scraper-pw)

scrape google using playwright, cross platform (Windows/MacOS/Linux)

## Installation

```bash
pip install google-scraper-pw
# pip install google-scraper-pw  # upgrade to the latest version
python -m playwrigh install chromium
```
or
```bash
poetry add google-scraper-pw
# poetry add googlw-scraper-pw@latest  # upgrade to the latest version
python -m playwrigh install chromium
```
or
```bash
pip install git+https://github.com/ffreemt/google-scraper-pw.git
```

or clone the repo (``git clone https://github.com/ffreemt/google-scraper-plawright.git``) and install from it and
```
python -m playwrigh install chromium
```

## Usage

## In an `ipython` session:

```python

# ipython

from google_scraper_pw.google_tr import google_tr

res = await google_tr("test me")
print(res)
# '考我 试探我 测试我 试探'

print(await google_tr("test me", to_lang="de"))
# mich testen mich prüfen testen Sie mich

text = "Playwright is a Python library to automate Chromium, Firefox and WebKit browsers with a single API. Playwright delivers automation that is ever-green, capable, reliable and fast. "
print(await google_tr(text, to_lang="zh"))
# Pyppeteer的API与puppeteer几乎相同。更多的API在文档中列出。
```

## in `python`

```python
import asyncio
from google_scraper_pw.google_tr import google_tr

async def main():
    text1 = "test me"
    text2 = "Pyppeteer has almost same API as puppeteer. More APIs are listed in the document"

    coros = [google_tr(elm) for elm in [text1, text2]]
    res = await asyncio.gather(*coros, return_exceptions=True)
    print(res)

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()

# output: ['考我 试探我 测试我 试探', 'Pyppeteer的API与puppeteer几乎相同。更多的API在文档中列出']

```

## Disclaimer

The pypi is beta and will likely remain beta -- use it at your own peril.

<!---

In [367]: doc0("div.lmt__textarea.lmt__textarea_dummydiv").text()
Out[367]: 'test you are me new lines 试探你是我 新行'

# doc0("div#target-dummydiv").text()
In [371]: doc0("#target-dummydiv").text()
Out[371]: '试探你是我 新行'

In [394]: doc0("#target-dummydiv").html()
Out[394]: '试探你是我\n新行\n\n'

# doc0("button.lmt__translations_as_text__text_btn").text()
In [369]: doc0(".lmt__translations_as_text__text_btn").text()
Out[369]: '试探你是我 新行'
In [369]: doc0(".lmt__translations_as_text__text_btn").html()


In [388]: re.findall(r"<button class=\"lmt__translations_as_text__text_btn[\s\S]*?>[\s\S]*?<\/button>", text0)
Out[388]: ['<button class="lmt__translations_as_text__text_btn">试探你是我\n新行</button>']

re.findall(r"<div id=\"target-dummydiv[\s\S]*?>[\s\S]*?<\/div>", text0)
['<div id="target-dummydiv" class="lmt__textarea lmt__textarea_dummydiv">试探你是我\n新行\n\n</div>']

--->