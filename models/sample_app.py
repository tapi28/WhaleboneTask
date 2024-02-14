class SampleAppPage:
    def __init__(self, page):
        self.page = page
        self.username = page.locator('input[name="UserName"]')
        self.password = page.locator('input[name="Password"]')
        self.login_button = page.locator("#login")
        self.logout_button = page.locator('//button[text()="Log Out"]')
        self.login_successful = page.locator("label.text-success")
        self.login_failed = page.locator("label.text-danger")
        self.logout_successful = page.locator('//label[text()="User logged out."]')

    def is_sample_app_loaded(self):
        return self.page.title() == "Sample App"

    def login(self, username: str, password: str):
        self.username.click()
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def logout(self):
        self.logout_button.click()
