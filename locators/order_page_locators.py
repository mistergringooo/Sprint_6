from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_OPTIONS_LIST = (By.XPATH, "//li[@class='select-search__row']")
    METRO_OPTION = (By.XPATH, "//li[@class='select-search__row']//button")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT = (By.XPATH, "//button[text()='Далее']")
    DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.XPATH, "//div[@class='Dropdown-control']")
    CLICK_ORDER = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[text()='Заказать']")
    CLICK_YES = (By.XPATH, "//button[text()='Да']")
    ORDER_SUCCESS = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")
    RENTAL_PERIOD_OPTION = (By.XPATH, "//div[@class='Dropdown-option' and text()='{}']")