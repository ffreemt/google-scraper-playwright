"""Init."""
from playwright.sync_api import sync_playwright
from logzero import logger

from google_scraper_pw.google_tr import google_tr

# from google_scraper_pw.google_tr_async import google_tr_async
# from google_scraper_pw.get_page_pw import get_page_pw

# PAGE, PLAYWRIGHT = get_page_pw()

__all__ = [
    # "google_tr",
    # "google_tr_async",
    # "PAGE",
    # "PLAYWRIGHT",
]
__version__ = "0.1.0"
