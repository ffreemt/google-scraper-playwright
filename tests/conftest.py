"""Config pytest"""
# import pytest
# from get_pwbrowser import get_pwbrowser


# @pytest.fixture
# @pytest.mark.asyncio
# async def pwbrowser(scope="module"):  # session

_ = """
@pytest.fixture
def pwbrowser(scope="module"):  # session

    # browser_ = get_pwbrowser(headless=False)
    browser_ = get_pwbrowser()

    yield browser_

    browser_.close()
# """
