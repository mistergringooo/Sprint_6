from pages.main_page import MainPage
import pytest
from urls import MAIN_URL
import allure
from test_data import ANSWERS

class TestQuestions:

    @pytest.mark.parametrize('number, answer', [
        (0, ANSWERS[0]),
        (1, ANSWERS[1]),
        (2, ANSWERS[2]),
        (3, ANSWERS[3]),
        (4, ANSWERS[4]),
        (5, ANSWERS[5]),
        (6, ANSWERS[6]),
        (7, ANSWERS[7]),
    ])
    @allure.title('Проверка открытия вопросов')
    def test_question_answer(self, driver, number, answer):
        driver.get(MAIN_URL)
        main_page = MainPage(driver)
        main_page.click_question(number)
        assert main_page.get_answer_text(number) == answer