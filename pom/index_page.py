from base_object.base import BaseObject
from base_object.locators import Locators as l
from base_object.assertion import Assertion
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class IndexPage(BaseObject, Assertion):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def test_scroll_to_elem(self):
        self.scroll_to_mid()

    def click_elem_btn(self):
        self.to_click(l.ELEMENTS_BUTTON)

    def click_check_box_btn(self):
        self.to_click(l.CHECK_BOX_BUTTON)

    def click_home_btn(self):
        self.to_click(l.HOME_DIR_BUTTON)

    def click_dwnl_btn(self):
        self.to_click(l.DOWNLOADS_BUTTON)

    def select_file(self):
        self.to_click(l.WORD_FILE_CHECK_BOX)



    def result_text_union(self):
        first_part = self.is_visible(l.RESULT_TEXT_FIRST).text
        second_part = self.is_visible(l.RESULT_TEXT_SECOND).text
        self.result_text = first_part + second_part

    def check_text(self):
        exp_text = 'You have selected :wordFile'
        self.assertion_equal(self.result_text, exp_text), 'text is not correct'

