import pytest
import allure
import time




def test_pesok(index_page):
    index_page.test_scroll_to_elem()
    index_page.click_elem_btn()
    index_page.click_check_box_btn()
    index_page.click_home_btn()
    index_page.click_dwnl_btn()
    index_page.select_file()
    index_page.result_text_union()
    index_page.check_text()


