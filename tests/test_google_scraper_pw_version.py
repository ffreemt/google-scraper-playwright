"""Pytest verson."""
from google_scraper_pw import __version__


def test_version():
    """Pytest version."""
    assert __version__[:3] == "0.1"
