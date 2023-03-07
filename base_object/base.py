from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from typing import List # необходимый импорт
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By





class BaseObject:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def is_visible(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def is_clickable(self, locator):
        return self.wait.until(ec.element_to_be_clickable(locator))



    def to_click(self, locator):
        self.is_clickable(locator).click()

    def get_text(self, locator):
        return self.is_visible(locator).text


    def to_get_attribute(self, locator, attribute):
        return self.is_visible(locator).get_attribute(attribute)

    def are_visible(self, locator) -> List[WebElement]:
        return self.wait.until(ec.visibility_of_all_elements_located(locator))


    def scroll_to_elem(self, locator):
        element = self.is_visible(locator)

        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def scroll_to_mid(self):
        window_height = self.driver.execute_script("return window.innerHeight")
        self.driver.execute_script(f"window.scrollTo(0, {window_height / 2});")



