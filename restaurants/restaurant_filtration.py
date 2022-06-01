from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


# Class with instance methods responsible for interacting with our google search after we reach the results.
class SearchFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def check_open_places(self):
        # self.driver.implicitly_wait(2)
        # self.driver.refresh()
        availability = self.driver.find_element(
            by=By.XPATH,
            value='//*[@id="Odp5De"]/div/div/div/div[1]/div[2]/div/div/div[4]'
        )
        availability.click()
        open_places_only = self.driver.find_element(
            by=By.XPATH, value='//*[@id="filter_4"]/div[1]/div[2]'
        )
        open_places_only.click()
        # expand_hours = self.driver.find_element(
        #    by=By.XPATH, value='/html/body/div[6]/div/div[6]/div/div/div/div/div/div[4]/div/div[1]')
        # expand_hours.click()
        # open_now_places = self.driver.find_element(by=By.XPATH, value='/html/body/div[6]/div/div[6]/div/div/div/div/div/div[4]/div/div[2]/div[1]/div[2]')
        # open_now_places = expand_hours.find_element(by=By.PARTIAL_LINK_TEXT, value='Open now')
        # open_now_places.click()