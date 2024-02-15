# Description: This file contains the test cases for the Load Delay page.
import time


# Test is failing correctly, as the reasonable time for page to load is up to 5 seconds.
def test_load_delay_page_is_loaded_in_5_seconds(homepage):
    # Save current time with the start of the test
    start_time = time.time()
    homepage.click_load_delay()
    # Click the button appearing after a delay and measure end time

    homepage.click_button_appearing_after_delay()
    end_time = time.time()
    # Calculate the time difference
    time_difference = end_time - start_time

    # Assert the time difference is less than 5 seconds
    assert (
        time_difference <= 5
    ), f"Time difference between clicks is {time_difference} seconds."
