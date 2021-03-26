"""Test simple."""
import asyncio

from google_scraper_pw.google_tr import google_tr

# from get_ppbrowser.get_ppbrowser import get_ppbrowser
from get_pwbrowser import get_pwbrowser


def test_simple():
    """Test simple.

    @pytest.fixture(scope="function")
    async def
        ...
    @pytest.mark.asyncio
        ...

    wont work, always runtime errors: loop already closed
    """
    try:
        loop = asyncio.get_event_loop()
    except Exception:
        # logger.error(exc)
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    # browser = asyncio.run(pyppeteer.launch())
    # page = asyncio.run(browser.newPage())

    # 3s
    # browser = loop.run_until_complete(pyppeteer.launch())

    # also OK, 1.8s
    # browser = loop.run_until_complete(get_ppbrowser())

    browser = loop.run_until_complete(get_pwbrowser())

    # 500 ms
    page = loop.run_until_complete(browser.newPage())

    text = "test this and more"
    # res = asyncio.run(google_tr(text, page=page))

    # fist time ~10s, 3.25s
    res = loop.run_until_complete(google_tr(text, page=page))

    assert "试" in res

    loop.run_until_complete(page.close())
    loop.run_until_complete(browser.close())
