from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json
import time
import random


class Helper:
    def __init__(self, driver: webdriver) -> None:
        self.driver = driver

    def xpath_locator(self, xpath, timeout=10):
        """Wait until the element is loaded before continuing."""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )

    def xpath_fill(self, xpath, keys):
        self.xpath_locator(xpath)

        element = self.driver.find_element(By.XPATH, xpath)
        element.send_keys(keys)
        time.sleep(random.uniform(1.8, 3.2))

    def xpath_btn_click(self, xpath):
        self.xpath_locator(xpath)

        element = self.driver.find_element(By.XPATH, xpath)
        element.click()
        time.sleep(random.uniform(1.8, 3.2))

    def save_twitter_cookies(self, cookies):
        with open("twitter-cookies.json", "w") as file:
            json.dump(cookies, file)

    def load_twitter_cookies(self):
        try:
            with open("twitter-cookies.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print("No cookies found for twitter.")

    def save_steam_cookies(self, cookies):
        with open("steam-cookies.json", "w") as file:
            json.dump(cookies, file)

    def load_steam_cookies(self):
        try:
            with open("steam-cookies.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print("No cookies found for steam.")
