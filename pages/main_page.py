from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import DZEN_DOMAIN
import allure

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    @allure.step('Получить элемент вопроса')
    def get_question(self, number):
        locator = (MainPageLocators.QUESTION[0], MainPageLocators.QUESTION[1].format(number))
        return self.driver.find_element(*locator)
    
    @allure.step('Получить элемент ответа')
    def get_answer(self, number):
        locator = (MainPageLocators.ANSWER[0], MainPageLocators.ANSWER[1].format(number))
        return self.driver.find_element(*locator)
    
    @allure.step('Получить текст ответа')
    def get_answer_text(self, number):
        locator = (MainPageLocators.ANSWER[0], MainPageLocators.ANSWER[1].format(number))
        return WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(locator)
        ).text
    
    @allure.step('Клик по вопросу')
    def click_question(self, number):
        locator = (MainPageLocators.QUESTION[0], MainPageLocators.QUESTION[1].format(number))
        element = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Проверка видимости ответа')
    def check_answer_visible(self, number):
        locator = (MainPageLocators.ANSWER[0], MainPageLocators.ANSWER[1].format(number))
        return WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(locator)
        )
    
    @allure.step('Клик по кнопке заказа сверху')
    def click_order_top(self):
        self.driver.find_element(*MainPageLocators.ORDER_BUTTON_TOP).click()

    @allure.step('Клик по кнопке заказ внизу')
    def click_order_bottom(self):
        self.driver.find_element(*MainPageLocators.ORDER_BUTTON_BOTTOM).click()

    @allure.step('Принятие куков')
    def accept_cookies(self):
        try:
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(MainPageLocators.COOKIES)
            ).click()
        except:
            pass
    
    @allure.step('Клик по логотипу самоката')
    def click_logo_scooter(self):
        self.driver.find_element(*MainPageLocators.LOGO_SCOOTER).click()

    @allure.step('Клик по логотипу Яндекс')
    def click_logo_yandex(self):
        self.driver.find_element(*MainPageLocators.LOGO_YANDEX).click()

    @allure.step('Проверить переход на Дзен по логотипу Яндекса')
    def check_yandex_logo(self):
        WebDriverWait(self.driver, 5).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(lambda d: DZEN_DOMAIN in d.current_url)
        return self.driver.current_url
    
    @allure.step('Проверить переход на главную по логотипу Самоката')
    def check_scooter_logo(self):
        return self.driver.current_url