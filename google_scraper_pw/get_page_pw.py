"""Create Page Playwright instances."""
from playwright.sync_api import sync_playwright
from logzero import logger


def get_page_pw():
    """Create Page Playwright instances."""
    try:
        # playwright = await async_playwright().start()
        playwright = sync_playwright().start()
    except Exception as exc:
        logger.error(exc)
        raise

    try:
        # browser = await get_pwbrowser()
        # browser = await playwright.chromium.launch(headless=False)
        # browser = await playwright.chromium.launch(devtools=True)
        # browser = playwright.chromium.launch(devtools=True)

        browser = playwright.chromium.launch()
    except Exception as exc:
        logger.error(exc)
        logger.info("Apparently, only one playwright instance is allowed.")
        logger.info(
            "Hence, you may wish to use from google_scraper_google import PAGE, PW instead"
        )

        raise

    try:
        page = browser.new_page()
    except Exception as exc:
        logger.error(exc)
        raise

    from_lang = "auto"
    to_lang = "zh"
    url = f"https://translate.google.cn/?sl={from_lang}&tl={to_lang}&op=translate"

    try:
        page.goto(url)
    except Exception as exc:
        logger.error(exc)
        raise

    return page, playwright


PAGE, PLAYWRIGHT = get_page_pw()

if __name__ == "__main__":
    # PA, PW = get_page_pw()

    print(type(PAGE), type(PLAYWRIGHT))
