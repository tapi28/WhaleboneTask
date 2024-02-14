class HomePage:
    def __init__(self, page):
        self.page = page

        # Features on the home page
        self.sample_app = page.locator("text=Sample App")
        self.load_delay = page.locator("text=Load Delay")
        self.progress_bar = page.locator("text=Progress Bar")

    def navigate(self):
        self.page.goto("http://uitestingplayground.com/")

    def click_sample_app(self):
        self.sample_app.click()

    def click_load_delay(self):
        self.load_delay.click()

    def click_progress_bar(self):
        self.progress_bar.click()
