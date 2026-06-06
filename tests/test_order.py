from pages.main_page import MainPage
from pages.order_page import OrderPage
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from urls import MAIN_URL
from urls import DZEN_URL

class TestOrder:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @pytest.mark.parametrize('name, surname, address, metro, phone, date, period', [
        ('Антон', 'Антонов', 'Черского, 15', 'Сокольники', '89998887766', '05.06.2026', 'сутки'),
        ('Олег', 'Олегов', 'Черского, 13', 'Бибирево', '89991112233', '06.06.2026', 'двое суток')
    ])
    def test_order(self, name, surname, address, metro, phone, date, period):
        self.driver.get(MAIN_URL)
        main_page = MainPage(self.driver)
        order_page = OrderPage(self.driver)
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
    def test_order_bottom(self, name, surname, address, metro, phone, date, period):
        self.driver.get(MAIN_URL)
        main_page = MainPage(self.driver)
        order_page = OrderPage(self.driver)
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

    def test_logo_scooter(self):
        self.driver.get(MAIN_URL)
        main_page = MainPage(self.driver)
        main_page.click_logo_scooter()
        assert self.driver.current_url == MAIN_URL

    def test_logo_yandex(self):
        self.driver.get(MAIN_URL)
        main_page = MainPage(self.driver)
        main_page.click_logo_yandex()
        WebDriverWait(self.driver, 5).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(lambda d: 'dzen.ru' in d.current_url)
        assert 'dzen.ru' in self.driver.current_url
