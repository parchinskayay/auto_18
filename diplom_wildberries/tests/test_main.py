from diplom_wildberries.pages import MainPage
from diplom_wildberries.pages.favorites_page import FavouritesPage


def test_open_wildberries(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.assert_that_main_is_opened()



def test_open_liked(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.assert_that_main_is_opened()

    main_page.click_on_liked()

    favorites_page = FavouritesPage(driver)
    favorites_page.assert_that_page_is_opened()



