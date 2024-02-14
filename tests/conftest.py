from typing import List, Dict, Any
import pytest

# from playwright.async_api import async_playwright

from api_clients.test_api import TestApi
from models.home_page import HomePage
from models.load_delay import LoadDelayPage
from models.progress_bar import ProgressBarPage
from models.sample_app import SampleAppPage


@pytest.fixture
def api_instance() -> TestApi:
    return TestApi("https://qa-assignment.dev1.whalebone.io/api/")


@pytest.fixture
def nhl_teams(api_instance) -> List[Dict[str, Any]]:
    list_of_teams = api_instance.get_teams()["teams"]
    return list_of_teams


# @pytest.fixture(scope="module")
# def browser():
#     with async_playwright() as p:
#         browser = p.chromium.launch()
#         yield browser
#         browser.close()


@pytest.fixture
def homepage(browser) -> HomePage:
    page = browser.new_page()
    home_page = HomePage(page)
    home_page.navigate()
    yield home_page
    page.close()


@pytest.fixture
def sample_app_page(homepage: HomePage) -> SampleAppPage:
    homepage.click_sample_app()
    return SampleAppPage(homepage.page)


@pytest.fixture
def load_delay_page(homepage: HomePage) -> LoadDelayPage:
    homepage.click_load_delay()
    return LoadDelayPage(homepage.page)


@pytest.fixture
def progress_bar_page(homepage: HomePage) -> ProgressBarPage:
    homepage.click_progress_bar()
    return ProgressBarPage(homepage.page)
