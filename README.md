# google-scraper-pw
[![tests](https://github.com/ffreemt/google-scraper-playwright/actions/workflows/routine-tests.yml/badge.svg)][![python](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/google-scraper-pw.svg)](https://badge.fury.io/py/google-scraper-pw)

scrape google using playwright, cross platform (Windows/MacOS/Linux)

## Installation

```bash
pip install google-scraper-pw
# pip install google-scraper-pw -U  # upgrade to the latest version
python -m playwright install chromium
```
<details>
<summary>or via poetry</summary>
<code style="white-space:wrap;">
poetry add google-scraper-pw &&
python -m playwright install chromium
</code>
</details>

or
```bash
pip install git+https://github.com/ffreemt/google-scraper-playwright.git
python -m playwright install chromium
```

or clone the repo (``git clone https://github.com/ffreemt/google-scraper-playwright.git``) and install from it and
```
python -m playwright install chromium
```

## Usage

```python
from pprint import pprint
from google_scraper_pw import google_tr

res = google_tr("test me")
print(res)
# '考验我'  # took 2.8s

# google_tr preserves format
pprint(google_tr("test you\n\n test me", to_lang="de"))
#'teste dich\n\n  teste mich'

text = "Playwright is a Python library to automate Chromium, Firefox and WebKit browsers with a single API. Playwright delivers automation that is ever-green, capable, reliable and fast. "

print(google_tr(text, to_lang="de"))

# Playwright ist eine Python-Bibliothek, um Chrom-, Firefox- und Webkit-Browser mit einer einzigen API zu automatisieren. Der Dramatiker liefert Automatisierung, die jemals grün, fähig, zuverlässig und schnell ist.  # took: 2.5s
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