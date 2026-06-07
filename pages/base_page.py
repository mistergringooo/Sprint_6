import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Прокрутка до элемента')
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    
    @allure.step('Клик по элементу')
    def js_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)