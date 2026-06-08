from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import DZEN_DOMAIN
import allure

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверить переход на Дзен по логотипу Яндекса')
    def check_yandex_logo(self):
        self.switch_to_new_window(DZEN_DOMAIN)
        return self.get_current_url()

    @allure.step('Проверить переход на главную по логотипу Самоката')
    def check_scooter_logo(self):
        return self.get_current_url()

    @allure.step('Клик по логотипу Яндекс')
    def click_logo_yandex(self):
        self.find_element(MainPageLocators.LOGO_YANDEX).click()

    @allure.step('Клик по логотипу самоката')
    def click_logo_scooter(self):
        self.find_element(MainPageLocators.LOGO_SCOOTER).click()

    @allure.step('Получить элемент вопроса')
    def get_question(self, number):
        by, selector = MainPageLocators.QUESTION
        locator = (by, selector.format(number))
        return self.find_element(locator)

    @allure.step('Получить элемент ответа')
    def get_answer(self, number):
        by, selector = MainPageLocators.ANSWER
        locator = (by, selector.format(number))
        return self.find_element(locator)

    @allure.step('Получить текст ответа')
    def get_answer_text(self, number):
        by, selector = MainPageLocators.ANSWER
        locator = (by, selector.format(number))
        return self.wait_for_element(locator).text

    @allure.step('Клик по вопросу')
    def click_question(self, number):
        by, selector = MainPageLocators.QUESTION
        locator = (by, selector.format(number))
        element = self.wait_for_element(locator)
        self.scroll_to_element(element)
        self.js_click(element)

    @allure.step('Проверка видимости ответа')
    def check_answer_visible(self, number):
        by, selector = MainPageLocators.ANSWER
        locator = (by, selector.format(number))
        return self.wait_for_element(locator)

    @allure.step('Клик по кнопке заказа сверху')
    def click_order_top(self):
        self.find_element(MainPageLocators.ORDER_BUTTON_TOP).click()

    @allure.step('Клик по кнопке заказ внизу')
    def click_order_bottom(self):
        self.find_element(MainPageLocators.ORDER_BUTTON_BOTTOM).click()

    @allure.step('Принятие куков')
    def accept_cookies(self):
        try:
            self.wait_for_clickable(MainPageLocators.COOKIES).click()
        except:
            pass