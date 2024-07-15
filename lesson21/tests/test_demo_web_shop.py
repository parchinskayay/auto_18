from lesson21.pages.demo_web_shop_page import DemoWebShopPage


def test_demo(driver):
    shop_page = DemoWebShopPage(driver)
    shop_page.open().\
        assert_elements_visible()

