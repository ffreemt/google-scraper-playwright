
import asyncio
from google_scraper_pw.google_tr import google_tr

loop = asyncio.get_event_loop()

from get_pwbrowser import get_pwbrowser  # noqa: E402


async def get_page():
    browser = await get_pwbrowser()
    # browser = await get_pwbrowser(headless=True)
    page = await browser.new_page()
    from_lang = "auto"
    to_lang = "zh"
    url = f"https://translate.google.cn/?sl={from_lang}&tl={to_lang}&op=translate"
    await page.goto(url)
    return page


def main():
    text1 = "test me"
    text2 = "Playwright is a Python library to automate Chromium, Firefox and WebKit browsers with a single API."

    page = loop.run_until_complete(get_page())

    _ = """
    # this wont work since page is shared
    coros = [google_tr(elm, page=page) for elm in [text1, text2]]
    res = await asyncio.gather(*coros, return_exceptions=True)
    # """

    for text in [text1, text2]:
        res = loop.run_until_complete(google_tr(text, page=page))
        print(res)


if __name__ == "__main__":
    main()

# Code block 'fetching' took: 7.29434 s
# 考验我
# Code block 'fetching' took: 2.92278 s
# PlayWight是一个Python库，用于自动化Chromium，Firefox和Webkit浏览器，具有单个API。
