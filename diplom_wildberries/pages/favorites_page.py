from diplom_wildberries.elements import HeaderElement
from diplom_wildberries.helpers import BASE_URL
from diplom_wildberries.locators import FavouritesLocators
from diplom_wildberries.pages import BasePage


class FavouritesPage(BasePage, FavouritesLocators, HeaderElement):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.open_page(BASE_URL)

    def assert_that_page_is_opened(self):
        assert self.get_element(self.FAVORITES)
        assert self.get_element(self.GO_SHOPPING_BUTTON)
        assert self.get_element(self.EMPTY_PAGE)

        self.assertions.assert_that_text_is_visible(self.TITLE, 'Здесь будут избранные товары')
