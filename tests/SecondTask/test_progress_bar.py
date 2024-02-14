# Description: This file contains the test cases for the Progress Bar page.
import time

import pytest


class TestProgressBar:
    @pytest.mark.skip(reason="Test is flaky, needs investigation and rework")
    def test_progress_bar_at_75_percent(self, progress_bar_page):
        progress_bar_page.click_start_button()
        try:
            progress_bar_page.get_progress_bar_value()
        finally:
            progress_bar_page.click_stop_button()
        assert progress_bar_page.progress_bar.get_attribute("aria-valuenow") == "75"

    def test_progress_bar_at_75_percent_v2(self, progress_bar_page):
        progress_bar_page.click_start_button()
        progress_bar_interval = [str(num) for num in range(75, 77)]
        while (
            progress_bar_page.progress_bar.get_attribute("aria-valuenow")
            not in progress_bar_interval
        ):
            time.sleep(0.01)
        progress_bar_page.click_stop_button()
        assert (
            progress_bar_page.progress_bar.get_attribute("aria-valuenow")
            in progress_bar_interval
        )
