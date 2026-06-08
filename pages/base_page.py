import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Прокрутка до элемента')
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    
    @allure.step('Клик по элементу')
    def js_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Найти элемент')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Ожидание элемента')
    def wait_for_element(self, locator, timeout=3):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step('Ожидание кликабельности элемента')
    def wait_for_clickable(self, locator, timeout=3):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
    
    @allure.step('Переключиться на новое окно')
    def switch_to_new_window(self, expected_url_part):
        WebDriverWait(self.driver, 5).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(lambda d: expected_url_part in d.current_url)

    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return self.driver.current_url