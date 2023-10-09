import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_page import BasePage
from SpaceToStudy.ui.pages.first_login_student_modal.first_login_modal import FirstLoginModal
from SpaceToStudy.ui.pages.first_login_student_modal.language_step import LanguageStepStudent


STARTING_TEXT = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/div[2]/div[1]/p[1]")
IMAGE = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/div[1]/img")
MAIN_TUTORING_CATEGORY_INPUT = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/input")
MAIN_TUTORING_CATEGORY_LABEL = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/div[2]/div[1]/div[1]/div/label")
SUBJECT_INPUT = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div/input")
SUBJECT_LABEL = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div/div[2]/div/div[2]/div[1]/div[2]/div/label")
ADD_SUBJECT_BUTTON = (By.XPATH, "//button[@data-testid='add-subject']/span")


class InterestsStepStudent(FirstLoginModal):

    @allure.step("Get starting text")
    def get_starting_text(self) -> str:
        return self.driver.find_element(*STARTING_TEXT).text

    @allure.step("Get image")
    def get_image(self) -> WebElement:
        return self.driver.find_element(*IMAGE)

    @allure.step("Get main tutoring category input")
    def get_main_tutoring_category_input(self) -> WebElement:
        return self.driver.find_element(*MAIN_TUTORING_CATEGORY_INPUT)

    @allure.step("Set main tutoring category input")
    def set_main_tutoring_category_input(self, text):
        self.get_main_tutoring_category_input().send_keys(text)

    @allure.step("Get main tutoring category label")
    def get_main_tutoring_category_label(self) -> WebElement:
        return self.driver.find_element(*MAIN_TUTORING_CATEGORY_LABEL)

    @allure.step("Get subject input")
    def get_subject_input(self) -> WebElement:
        return self.driver.find_element(*SUBJECT_INPUT)

    @allure.step("Set subject input")
    def set_subject_input(self, text):
        self.get_subject_input().send_keys(text)

    @allure.step("Get subject label")
    def get_subject_label(self) -> WebElement:
        return self.driver.find_element(*SUBJECT_LABEL)

    @allure.step("Get add subject button")
    def get_add_subject_button(self) -> WebElement:
        return self.driver.find_element(*ADD_SUBJECT_BUTTON)

    @allure.step("Click add subject button")
    def click_add_subject_button(self):
        self.get_add_subject_button().click()
        return self
    
    @allure.step("Click next button")
    def click_next_button(self):
        self.get_next_button().click()
        return LanguageStepStudent(self.node)
    
    @allure.step("Click back button")
    def click_back_button(self):
        from SpaceToStudy.ui.pages.first_login_student_modal.general_step import GeneralStepStudent
        self.get_back_button().click()
        return GeneralStepStudent(self.node)

