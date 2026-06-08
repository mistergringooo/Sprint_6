from pages.main_page import MainPage
from pages.order_page import OrderPage
import pytest
from urls import MAIN_URL
from urls import DZEN_DOMAIN
import allure

class TestOrder:

    @pytest.mark.parametrize('name, surname, address, metro, phone, date, period', [
        ('Антон', 'Антонов', 'Черского, 15', 'Сокольники', '89998887766', '05.06.2026', 'сутки'),
        ('Олег', 'Олегов', 'Черского, 13', 'Бибирево', '89991112233', '06.06.2026', 'двое суток')
    ])
    @allure.title('Проверка оформления заказа')
    def test_order(self,driver, name, surname, address, metro, phone, date, period):
        driver.get(MAIN_URL)
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.accept_cookies()
        main_page.click_order_top()
        order_page.set_name(name)
        order_page.set_surname(surname)
        order_page.set_address(address)
        order_page.set_metro(metro)
        order_page.set_phone(phone)
        order_page.click_next()
        order_page.set_date(date)
        order_page.set_rental_period(period)
        order_page.click_order()
        order_page.click_yes()
        assert order_page.check_order_success()

    @pytest.mark.parametrize('name, surname, address, metro, phone, date, period', [
        ('Антон', 'Антонов', 'Черского, 15', 'Сокольники', '89998887766', '05.06.2026', 'сутки'),
        ('Олег', 'Олегов', 'Черского, 13', 'Бибирево', '89991112233', '06.06.2026', 'двое суток')
    ])
    @allure.title('Проверка оформления заказа через кнопку внизу')
    def test_order_bottom(self,driver, name, surname, address, metro, phone, date, period):
        driver.get(MAIN_URL)
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.accept_cookies()
        main_page.click_order_bottom()
        order_page.set_name(name)
        order_page.set_surname(surname)
        order_page.set_address(address)
        order_page.set_metro(metro)
        order_page.set_phone(phone)
        order_page.click_next()
        order_page.set_date(date)
        order_page.set_rental_period(period)
        order_page.click_order()
        order_page.click_yes()
        assert order_page.check_order_success()

    @allure.title('Проверка открытия главной страницы по клику на логотип самоката')
    def test_logo_scooter(self, driver):
        driver.get(MAIN_URL)
        main_page = MainPage(driver)
        main_page.click_logo_scooter()
        assert main_page.check_scooter_logo() == MAIN_URL

    @allure.title('Проверка редиректа на Дзен.ру по клику на логотип Яндекса')
    def test_logo_yandex(self, driver):
        driver.get(MAIN_URL)
        main_page = MainPage(driver)
        main_page.click_logo_yandex()
        assert DZEN_DOMAIN in main_page.check_yandex_logo()
