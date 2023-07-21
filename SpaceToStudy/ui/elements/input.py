from selenium.webdriver.common.by import By

INPUT = (By.XPATH, "./div/input")
LABEL = (By.XPATH, "./label")
ERROR_MESSAGE = (By.XPATH, "./p/span")


class Input:
    def __init__(self, noda):
        self.noda = noda

    def set_text(self, text):
        self.get_input().send_keys(text)

    def get_input(self):
        return self.noda.find_element(*INPUT)

    def get_label_text(self):
        return self.noda.find_element(*LABEL).text

    def get_error_message(self):
        return self.noda.find_element(*ERROR_MESSAGE).text
