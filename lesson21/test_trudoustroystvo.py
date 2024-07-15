from lesson21.trudoustroystvo_page import TrudoustroystvoPage


def test_open_page(driver):
    page = TrudoustroystvoPage(driver)
    page.open()

    page.assert_elements_visible()