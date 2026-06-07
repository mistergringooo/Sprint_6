from selenium.webdriver.common.by import By

class MainPageLocators:
    QUESTION = (By.ID, 'accordion__heading-{}')
    ANSWER = (By.ID, 'accordion__panel-{}')
    ORDER_BUTTON_TOP = (By.XPATH, "//div[@class='Header_Nav__AGCXC']//button")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']//button")
    COOKIES = (By.ID, 'rcc-confirm-button')
    LOGO_SCOOTER = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    LOGO_YANDEX = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")