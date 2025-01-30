from playwright.sync_api import expect

from playwrightpython.pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.name_box = "input[name='name']"
        self.email_box = "input[name='email']"
        self.navBar="//a[@class='navbar-brand']"

    def enter_details(self, name, email):
        self.type(self, self.name_box, name)
        self.type(self, self.email_box, email)
        return self

    def gettext(self):
       return self.get_text(self.navBar)


    def check_if_landed_on_homePage(self):
        expect(self.page.get_by_text("Logged In Successfully")).to_be_visible()
