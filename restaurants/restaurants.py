import time
import restaurants.constants as const
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from restaurants.restaurant_filtration import SearchFiltration
from restaurants.restaurant_report import RestaurantReport
from prettytable import PrettyTable

# Instantiate library to open the chrome browser.
class Restaurants:
    def __init__(self, driver_path=r"/Users/bigdaddy/Desktop/Code projects/SeleniumDrivers/chromedriver", teardown=False):
        self.driver_path = webdriver.Chrome(service=Service(driver_path))
        self.teardown = teardown
        os.environ['PATH'] += driver_path
        self.driver_path.options = Options()
        self.driver_path.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Restaurants, self).__init__()
        self.driver_path.maximize_window()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.driver_path.quit()

    # Open first page of the program defined in constants, in this case, "Google".
    def land_first_page(self):
        self.driver_path.get(const.BASE_URL)

    # Submit a google search.
    def search_nearby_restaurants(self):
        search_box = self.driver_path.find_element(by=By.NAME, value='q')
        search_box.send_keys('restaurants near me')
        search_box.submit()
        #time.sleep(1)
        #self.driver_path.implicitly_wait(2)

    # Apply page filters and implement any parameters to specify or narrow results.
    def apply_filtrations(self):
        filtration = SearchFiltration(driver=self.driver_path)
        filtration.check_open_places()

     # Gather and process the data found from the results.
    def report_results(self):
        self.driver_path.implicitly_wait(1)
        restaurant_boxes = self.driver_path.find_element(by=By.ID, value='rl_ist0')
        report = RestaurantReport(restaurant_boxes)
        table = PrettyTable(
            field_names=['Restaurant Name', 'Restaurant Rating']
        )
        table.add_rows(report.pull_restaurant_box_attributes())
        print(table)
        #print(report.pull_restaurant_box_attributes())

# # Instantiate library to open the chrome browser
# s = Service('/Users/bigdaddy/Desktop/Code projects/SeleniumDrivers/chromedriver')
# driver = webdriver.Chrome(service=s)
#
# driver.get('http://www.google.com/')
# search_box = driver.find_element(by=By.NAME, value='q')
# search_box.send_keys('restaurants near me')
# search_box.submit()
# #time.sleep(1)
#
# expand_list = driver.find_element(by=By.PARTIAL_LINK_TEXT, value='More places')
# expand_list.click()
