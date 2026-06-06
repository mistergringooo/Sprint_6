from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        
    def get_question(self, number):
        return self.driver.find_element(By.ID, f'accordion__heading-{number}')
    
    def get_answer(self, number):
        return self.driver.find_element(By.ID, f'accordion__panel-{number}')
    
    def click_question(self, number):
        element = WebDriverWait(self.driver, 3).until(
        EC.presence_of_element_located((By.ID, f'accordion__heading-{number}'))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def check_answer_visible(self, number):
        return WebDriverWait(self.driver, 3).until(
        EC.visibility_of_element_located((By.ID, f'accordion__panel-{number}'))
        )
    
    def click_order_top(self):
        self.driver.find_element(By.XPATH, "//div[@class='Header_Nav__AGCXC']//button").click()

    def click_order_bottom(self):
        self.driver.find_element(By.XPATH, "//div[@class='Home_FinishButton__1_cWm']//button").click()

    def accept_cookies(self):
        try:
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.ID, 'rcc-confirm-button'))
            ).click()
        except:
            pass
    
    def click_logo_scooter(self):
        self.driver.find_element(By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']").click()

    def click_logo_yandex(self):
        self.driver.find_element(By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']").click()