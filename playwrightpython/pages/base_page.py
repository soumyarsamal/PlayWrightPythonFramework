class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def click(self, selector):
        self.page.click(selector)

    def type(self, selector, text):
        self.page.fill(selector, text)

    def get_text(self, selector):
        return self.page.inner_text(selector)
