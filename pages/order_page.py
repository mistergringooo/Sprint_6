from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def set_name(self, name):
        self.driver.find_element(By.XPATH, "//input[@placeholder='* Имя']").send_keys(name)

    def set_surname(self, surname):
        self.driver.find_element(By.XPATH, "//input[@placeholder='* Фамилия']").send_keys(surname)

    def set_address(self, address):
        self.driver.find_element(By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']").send_keys(address)

    def set_metro(self, metro):
        self.driver.find_element(By.XPATH, "//input[@placeholder='* Станция метро']").send_keys(metro)
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, "//ul[@class='select-search__options']"))
        )
        self.driver.find_element(By.XPATH, "//li[@class='select-search__row']//button").click()

    def set_phone(self, phone):
        self.driver.find_element(By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']").send_keys(phone)

    def click_next(self):
        self.driver.find_element(By.XPATH, "//button[text()='Далее']").click()

    def set_date(self, date):
        self.driver.find_element(By.XPATH, "//input[@placeholder='* Когда привезти самокат']").send_keys(date)
        self.driver.find_element(By.XPATH, "//input[@placeholder='* Когда привезти самокат']").send_keys(Keys.ESCAPE)

    def set_rental_period(self, period):
        WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='Dropdown-control']"))
        ).click()
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, f"//div[@class='Dropdown-option' and text()='{period}']"))
        ).click()

    def click_order(self):
        element = self.driver.find_element(By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[text()='Заказать']")
        self.driver.execute_script("arguments[0].click();", element)

    def click_yes(self):
        WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Да']"))
        ).click()

    def check_order_success(self):
        return WebDriverWait(self.driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']"))
        )