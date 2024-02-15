class ProgressBarPage:
    def __init__(self, page):
        self.page = page
        self.start_button = page.locator("#startButton")
        self.stop_button = page.locator("#stopButton")
        self.progress_bar = page.locator("#progressBar")

    def click_start_button(self):
        self.start_button.click()

    def click_stop_button(self):
        self.stop_button.click()

    def get_progress_bar_value(self):
        return self.progress_bar.get_attribute("aria-valuenow")
