from pages.main_page import MainPage
import pytest
from selenium import webdriver
from urls import MAIN_URL

class TestQuestions:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @pytest.mark.parametrize('number', [0, 1, 2, 3, 4, 5, 6, 7])
    def test_question_answer(self, number):
        self.driver.get(MAIN_URL)
        main_page = MainPage(self.driver)
        main_page.click_question(number)
        assert main_page.check_answer_visible(number)