"""Scrape google via playwright.

from pathlib import Path
import os
os.environ['PYTHONPATH'] = Path(r"../get-pwbrowser")
"""
# pylint: disable=too-many-arguments, too-many-locals, too-many-branches, too-many-statements, redefined-outer-name, import-outside-toplevel, invalid-name

from typing import Optional, Union

import asyncio
import re

# from urllib.parse import quote
import html

# from pyquery import PyQuery as pq
from playwright.async_api import async_playwright, Page

import logzero
from logzero import logger
from linetimer import CodeTimer

# from get_ppbrowser.get_ppbrowser import get_ppbrowser


# fmt: off
async def google_tr(
        text: str,
        from_lang: Optional[str] = "auto",
        to_lang: str = "zh",
        page: Optional[Page] = None,
        verbose: Union[bool, int] = False,
        timeout: float = 5,
):
    # fmt: on
    """Deepl via pyppeteer.

    text = "Test it and more"
    from_lang="auto"
    to_lang="zh"
    # page=PAGE
    page=None
    verbose=True
    """
    #

    try:
        text = str(text).strip()
    except Exception as exc:
        logger.warning("%s, setting to ''", exc)
        text = ""

    if not text:
        return ""

    if to_lang in ["zh", "chinese", "zhong"]:
        to_lang = "zh-CN"
    if from_lang is None:
        from_lang = "auto"
    if from_lang in ["zh", "chinese", "zhong"]:
        from_lang = "zh-CN"
    if to_lang in ["zh", "chinese", "zhong"]:
        to_lang = "zh-CN"

    if from_lang in [to_lang]:
        logger.info("Nothing to do, man")
        return text

    _ = 5000
    if len(text) > _:  # 5250
        logger.warning("text too long, trimmed to %s", _)
        text = text[:_]
        return text

    # set verbose=40 to turn most things off
    if isinstance(verbose, bool):
        if verbose:
            logzero.setup_default_logger(level=10)
        else:
            logzero.setup_default_logger(level=20)
    else:  # integer: log_level
        logzero.setup_default_logger(level=verbose)

    logger.debug(" Entry ")

    # if page is not supplied, get one, TODO use get_pwbrowser
    if page is None:
        try:
            playwright = await async_playwright().start()
        except Exception as exc:
            logger.error(exc)
            raise

        try:
            # browser = await get_pwbrowser()
            # browser = await playwright.chromium.launch(headless=False)
            # browser = await playwright.chromium.launch(devtools=True)
            browser = await playwright.chromium.launch()
        except Exception as exc:
            logger.error(exc)
            raise

        try:
            page = await browser.new_page()
            # page = await browser.newPage()
        except Exception as exc:
            logger.error(exc)
            raise

    try:
        google_tr.from_lang
    except AttributeError:
        google_tr.from_lang = "auto"
    try:
        google_tr.to_lang
    except AttributeError:
        google_tr.to_lang = "zh-CN"

    url = ""
    if (from_lang, to_lang) != (google_tr.from_lang, google_tr.to_lang):
        url = f"https://translate.google.cn/?sl={from_lang}&tl={to_lang}&op=translate"

        logger.debug(" lang pair changed")

        try:
            await page.goto(url, timeout=45 * 1000)
        except Exception as exc:
            logger.error(exc)
            raise

    try:
        textarea = await page.wait_for_selector('//textarea', timeout=45 * 1000)
    except Exception as exc:
        logger.error(exc)
        raise

    if verbose < 11 or verbose is True:
        _ = False  # silent
    else:
        _ = True
    with CodeTimer(name="fetching", unit="s", silent=_):
        _ = """
        # maybe no need to click, save some time
        sel_btn = "#ow42 > div:nth-child(1) > span > button > i"
        try:  # first nothing to click, timeout in 2 s
            btn = await page.wait_for_selector(sel_btn, timeout=5000)
            await btn.click()
        except Exception as exc:
            logger.error(exc)
        # """

        timeout = 30  # defaults to 30 seconds
        n_lines = len(text.splitlines())
        if n_lines > 100:
            timeout = n_lines * 0.4
        timeout = timeout * 1000  # convert to ms
        try:
            await textarea.fill('', timeout=timeout)
            await asyncio.sleep(0.1)
            await textarea.fill('', timeout=timeout)
            await asyncio.sleep(0.1)
            await textarea.fill(text, timeout=timeout)
        except Exception as exc:
            logger.error(exc)
            raise

        idx = 0
        flag = False
        ulimit = 3 / 0.1
        while not flag and idx < ulimit:
            idx += 1
            content = await page.content()
            # doc = pq(content)

            # flag = re.findall(r'data-text="[^"]+', doc.html())
            flag = re.findall(r'data-text="[^"]+', content)
            logger.debug(flag)
            if flag:
                break
            await asyncio.sleep(0.1)
        logger.debug("loop: %s", idx)

        await asyncio.sleep(0.1)
        content = await page.content()
        # doc = pq(content)

        try:
            # res, = re.search(r'data-text="([^"]+)', doc.html()).groups()
            res, = re.search(r'data-text="([^"]+)', content).groups()
        except Exception as exc:
            logger.error(exc)
            res = str(exc)
        res = html.unescape(res)
        logger.debug(res)

    if (from_lang, to_lang) != (google_tr.from_lang, google_tr.to_lang):
        logger.debug("url=%s", url)
        logger.debug("page.url=%s", page.url)
        logger.debug("%s, %s", url == page.url, re.findall(rf"tl={to_lang}", page.url))
        if not re.findall(rf"tl={to_lang}", page.url):
            logger.warning(" target lang [%s] does not appear to be a valid language, falled back to the previous tl [%s]", to_lang, google_tr.to_lang)
        else:
            google_tr.from_lang, google_tr.to_lang = from_lang, to_lang

    logger.debug(" Fini ")

    return res


async def main(page):
    """Main."""
    import sys

    text = "test this and that and more"
    res = await google_tr(text, page=page)
    logger.info("%s, %s,", text, res)

    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    else:
        text = "test this and that"

    res = await google_tr(text)
    logger.info("%s, %s,", text, res)


if __name__ == "__main__":
    from get_pwbrowser import get_pwbrowser

    try:
        loop = asyncio.get_event_loop()
    except Exception as exc:
        logger.error(exc)
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    browser = loop.run_until_complete(get_pwbrowser())
    # browser = await get_pwbrowser(headless=False)
    page = loop.run_until_complete(browser.new_page())

    from_lang = "auto"
    to_lang = "zh"
    url = f"https://translate.google.cn/?sl={from_lang}&tl={to_lang}&op=translate"

    _ = loop.run_until_complete(page.goto(url, timeout=45 * 1000))

    try:
        loop.run_until_complete(main(page))
    except Exception as exc:
        logger.error(exc)
    finally:
        loop.close()
