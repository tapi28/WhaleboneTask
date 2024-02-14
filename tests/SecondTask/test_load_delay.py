# Description: This file contains the test cases for the Load Delay page.
import time


class TestLoadDelay:
    def test_load_delay_page_is_loaded_in_5_seconds(self, load_delay_page):
        # Save current time with the start of the test
        start_time = time.time()
        # Click the button appearing after a delay and measure end time
        load_delay_page.click_button_appearing_after_delay()
        end_time = time.time()
        # Calculate the time difference
        time_difference = end_time - start_time

        assert load_delay_page.is_load_delay_loaded()
        assert load_delay_page.button_appearing_after_delay.is_visible()
        # Assert the time difference is less than 5 seconds
        assert (
            time_difference <= 5
        ), f"Time difference between clicks: {time_difference} seconds"
