from playwrightpython.pages.base_page import BasePage
from playwrightpython.pages.home_page import HomePage
from playwrightpython.utils.credential_management import LoginCredentials


class LoginService(BasePage):
    def __init__(self, page, ui_base_url):
        super().__init__(page)
        self.url = ui_base_url
        self.username = "input[name='username']"
        self.password = "input[name='password']"
        self.submit = "//button[@id='submit']"

    def login(self, username, password):
        self.type(self.username, username)
        self.type(self.password, password)
        self.click(self.submit)
        return self

    def login_as(self, role: LoginCredentials):
        self.page.goto(self.url)
        print("username is :", role.username)
        print("password is :", role.password)
        self.login(role.username, role.password)
        return HomePage(self.page)
    # self.login(user.username, user.password)
