from selenium.webdriver.common.by import By



class Locators:

    ELEMENTS_BUTTON = (By.XPATH, '//h5[contains(text(), "Elements")]/..')
    CHECK_BOX_BUTTON = (By.XPATH, '//li[@id="item-1"]')
    HOME_DIR_BUTTON = (By.XPATH, '//button[@class="rct-collapse rct-collapse-btn"]')
    DOWNLOADS_BUTTON = (By.XPATH, '//span[@class="rct-title"][contains(text(), "Downloads")]/../../button')
    WORD_FILE_CHECK_BOX = (By.XPATH, '//span[@class="rct-title"][contains(text(), "Word File.doc")]/../span[@class="rct-checkbox"]')
    RESULT_TEXT_FIRST = (By.XPATH, '//div[@id="result"]/span[1]')
    RESULT_TEXT_SECOND = (By.XPATH, '//div[@id="result"]/span[2]')
    PATH = (By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[1]/div/div[3]/h5')
