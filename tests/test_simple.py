"""Test simple."""
import asyncio
import pytest

from google_scraper_pw.google_tr import google_tr

# from get_ppbrowser.get_ppbrowser import get_ppbrowser
from get_pwbrowser import get_pwbrowser
from logzero import logger


@pytest.mark.asyncio
async def test_simple(pwbrowser):
    """Test simple.

    @pytest.fixture(scope="function")
    async def
        ...
    @pytest.mark.asyncio
        ...

    always runtime errors: loop already closed
    """
    #

    _ = """
    try:
        loop = asyncio.get_event_loop()
    except Exception:
        # logger.error(exc)
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    # """

    # browser = loop.run_until_complete(get_pwbrowser())
    browser = pwbrowser

    # 500 ms
    # page = loop.run_until_complete(browser.newPage())
    page = await browser.new_page()

    from_lang = "auto"
    to_lang = "zh"
    url = f"https://translate.google.cn/?sl={from_lang}&tl={to_lang}&op=translate"

    # _ = loop.run_until_complete(page.goto(url, timeout=45 * 1000))
    try:
        await page.goto(url, timeout=45 * 1000)
    except Exception as exc:
        logger.error(exc)
        raise

    text = "test this and more"
    # res = asyncio.run(google_tr(text, page=page))

    # fist time ~10s, 3.25s
    # res = loop.run_until_complete(google_tr(text, page=page))
    res = await google_tr(text, page=page)

    assert "试" in res

    # loop.run_until_complete(page.close())
    # loop.run_until_complete(browser.close())
