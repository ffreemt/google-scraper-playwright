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
pip install git+https://github.com/ffreemt/google-scraper-playwright.git
python -m playwrigh install chromium
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
# '考验我'  # took 13.8s
```
13s is a long time. To speed up: prepare a page first.

```
from get_pwbrowser import get_pwbrowser
browser = await get_pwbrowser()
page = await browser.new_page()
from_lang = "auto"
to_lang = "zh"
url = f"https://translate.google.cn/?sl={from_lang}&tl={to_lang}&op=translate"
await page.goto(url)
res = await google_tr("test me", page=page)
print(res)
# '考验我'  # took 2.8s, much better

print(await google_tr("test you", to_lang="de", page=page))
# teste mich

print(await google_tr("test you", to_lang="de", page=page))
# teste dich  # took: 2.8s

# format is preserved
from pprint import pprint

pprint(await google_tr("test you\n\n test me", to_lang="de", page=page))
#'teste dich\n\n  teste mich'

text = "Playwright is a Python library to automate Chromium, Firefox and WebKit browsers with a single API. Playwright delivers automation that is ever-green, capable, reliable and fast. "

print(await google_tr(text, to_lang="de", page=page))

# Playwright ist eine Python-Bibliothek, um Chrom-, Firefox- und Webkit-Browser mit einer einzigen API zu automatisieren. Der Dramatiker liefert Automatisierung, die jemals grün, fähig, zuverlässig und schnell ist.
```

## in `python`

```python
import asyncio
from google_scraper_pw.google_tr import google_tr

from get_pwbrowser import get_pwbrowser
browser = await get_pwbrowser()
page = await browser.new_page()
from_lang = "auto"
to_lang = "zh"
url = f"https://translate.google.cn/?sl={from_lang}&tl={to_lang}&op=translate"
await page.goto(url)

async def main():
    text1 = "test me"
    text2 = "Playwright is a Python library to automate Chromium, Firefox and WebKit browsers with a single API."

    coros = [google_tr(elm, page=page) for elm in [text1, text2]]
    res = await asyncio.gather(*coros, return_exceptions=True)
    print(res)

asyncio.run(main())

# output: ['测试MeplayWright是一个Python库，用于自动化Chromium，Firefox和WebKit浏览器，单个API。', '
测试MeplayWright是一个Python库，用于自动化Chromium，Firefox和WebKit浏览器，单个API。']

```


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