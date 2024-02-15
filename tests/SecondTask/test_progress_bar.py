# Description: This file contains the test cases for the Progress Bar page.
import time

import pytest


# This test identifies and stop progress bar when it is at 75 or higher(in case of super quick loading)
def test_progress_bar_stopped_closest_to_75_percent(progress_bar_page):
    progress_bar_page.click_start_button()
    progress_bar_interval = [str(num) for num in range(75, 100)]

    while progress_bar_page.get_progress_bar_value() not in progress_bar_interval:
        time.sleep(0.01)
    progress_bar_page.click_stop_button()
    assert progress_bar_page.get_progress_bar_value() in progress_bar_interval
