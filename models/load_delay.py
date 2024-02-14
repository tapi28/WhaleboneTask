class LoadDelayPage:
    def __init__(self, page):
        self.page = page
        self.button_appearing_after_delay = page.locator(".btn.btn-primary")

    def is_load_delay_loaded(self):
        return self.page.title() == "Load Delays"

    def click_button_appearing_after_delay(self):
        self.button_appearing_after_delay.click()
