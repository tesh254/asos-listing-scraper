from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")


class Scraper:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()
        self.product_details = {}

    def __initiate_request(self):
        self.driver.get(self.url)

    def __set_product_description(self):
        product_description_items_holder = self.driver.find_element(
            By.CSS_SELECTOR, "div.product-description").find_element(By.TAG_NAME, 'ul')

        items = product_description_items_holder.find_elements(
            By.TAG_NAME, 'li')

        product_details_text = ''

        for item in items:
            product_details_text += item.text + '/n'

        self.product_details['description'] = product_details_text

    def __set_product_title(self):
        title = self.driver.find_element(
            By.ID, 'pdp-react-critical-app').find_element(By.TAG_NAME, 'h1').text

        self.product_details['title'] = title

    def __set_product_images(self):
        listing_images = []

        for image in self.driver.find_elements(By.CLASS_NAME, 'gallery-image'):
            if (image.get_attribute('data-bind') == 'attr: imageSources().thumbnail'):
                listing_images.append(image.get_dom_attribute("src"))

        self.product_details['images'] = listing_images

    def __set_product_price(self):
        for div in self.driver.find_elements(By.TAG_NAME, "div"):
            if (div.get_attribute("data-test-id") == 'product-price'):
                for span in div.find_elements(By.TAG_NAME, "span"):
                    if (span.get_attribute('data-test-id') == 'current-price'):
                        self.product_details["price"] = span.text
    
    def __close_driver(self):
        self.driver.close()

    def run(self):
        self.__initiate_request()

        self.__set_product_title()
        self.__set_product_price()
        self.__set_product_images()
        self.__set_product_description()

        self.__close_driver()
