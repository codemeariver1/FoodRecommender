# Method that will parse the specific data that we need from each one of the boxes.

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class RestaurantReport:
    def __init__(self, boxes_section_element: WebElement):
        self.boxes_section_element = boxes_section_element
        self.restaurant_boxes = self.pull_restaurant_boxes()

    def pull_restaurant_boxes(self):
        return self.boxes_section_element.find_elements(by=By.CLASS_NAME, value='VkpGBb')

    def pull_restaurant_box_attributes(self):
        collection = []
        for restaurant_box in self.restaurant_boxes:
            restaurant_name = restaurant_box.find_element(
                by=By.CLASS_NAME, value='dbg0pd.eDIkBe'
            ).find_element(by=By.CLASS_NAME, value='OSrXXb'
            ).get_attribute('innerHTML').strip()
            print(restaurant_name)
            #restaurant_name = restaurant_name[6:-7]
            #restaurant_name = restaurant_name[restaurant_name.find(">") + 1: restaurant_name.find("</")]
            restaurant_name = restaurant_name.replace("&amp;", "&")
            try :
                restaurant_score = restaurant_box.find_element(
                    by=By.CLASS_NAME, value='YDIN4c'
                ).get_attribute('innerHTML').strip()
            except:
                restaurant_score = 'N/A'

            #print(restaurant_name)
            #print(restaurant_score)

            collection.append(
                [restaurant_name, restaurant_score]
            )
        return collection
