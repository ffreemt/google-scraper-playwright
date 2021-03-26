import pytest
from get_pwbrowser import get_pwbrowser


@pytest.fixture
@pytest.mark.asyncio
async def pwbrowser(scope="module"):  # session
    # browser_ = await get_pwbrowser(headless=False)
    browser_ = await get_pwbrowser()

    yield browser_

    await browser_.close()
