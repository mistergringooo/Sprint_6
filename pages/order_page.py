from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Заполнить Имя')
    def set_name(self, name):
        self.find_element(OrderPageLocators.NAME).send_keys(name)

    @allure.step('Заполнить Фамилия')
    def set_surname(self, surname):
        self.find_element(OrderPageLocators.SURNAME).send_keys(surname)

    @allure.step('Заполнить Адрес')
    def set_address(self, address):
        self.find_element(OrderPageLocators.ADDRESS).send_keys(address)

    @allure.step('Заполнить Метро')
    def set_metro(self, metro):
        self.find_element(OrderPageLocators.METRO_INPUT).send_keys(metro)
        self.wait_for_element(OrderPageLocators.METRO_OPTIONS_LIST)
        self.find_element(OrderPageLocators.METRO_OPTION).click()

    @allure.step('Заполнить Телефон')
    def set_phone(self, phone):
        self.find_element(OrderPageLocators.PHONE).send_keys(phone)

    @allure.step('Клик по кнопке Далее')
    def click_next(self):
        self.find_element(OrderPageLocators.NEXT).click()

    @allure.step('Заполнить Дату')
    def set_date(self, date):
        self.find_element(OrderPageLocators.DATE).send_keys(date)
        self.find_element(OrderPageLocators.DATE).send_keys(Keys.ESCAPE)

    @allure.step('Выбрать срок аренды')
    def set_rental_period(self, period):
        self.wait_for_clickable(OrderPageLocators.RENTAL_PERIOD).click()
        by, selector = OrderPageLocators.RENTAL_PERIOD_OPTION
        locator = (by, selector.format(period))
        self.wait_for_element(locator).click()

    @allure.step('Клик по кнопке заказать')
    def click_order(self):
        element = self.find_element(OrderPageLocators.CLICK_ORDER)
        self.js_click(element)

    @allure.step('Клик по кнопке Да')
    def click_yes(self):
        self.wait_for_clickable(OrderPageLocators.CLICK_YES).click()

    @allure.step('Проверка подтверждения заказа')
    def check_order_success(self):
        return self.wait_for_element(OrderPageLocators.ORDER_SUCCESS)