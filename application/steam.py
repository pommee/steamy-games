from yaspin import yaspin
from selenium import webdriver
import os
from constants import (
    STEAM_ACCOUNT_DROPDOWN,
    STEAM_AWAITING_2F,
    STEAM_GAME_CLAIM_BTN,
    STEAM_GAME_IMAGE,
    STEAM_GAME_NAME,
    STEAM_LOGIN_BTN_XPATH,
    STEAM_LOGIN_EMAIL_XPATH,
    STEAM_LOGIN_PAGE,
    STEAM_LOGIN_PASSWORD_XPATH,
    STEAM_LOGIN_REMEMBER_ME_XPATH,
)
from helper import Helper
from tweet import Tweet


class Steam:
    def __init__(
        self, driver: webdriver.Firefox, helper: Helper, tweets: list[Tweet]
    ) -> None:
        self.driver = driver
        self.helper = helper
        self.tweets = tweets

    def login(self):
        cookies = self.helper.load_steam_cookies()

        if cookies is not None:
            self.restore_session(cookies)
        else:
            self.driver.get(STEAM_LOGIN_PAGE)

            STEAM_USERNAME = os.getenv("STEAM_USERNAME")
            STEAM_PASSWORD = os.getenv("STEAM_PASSWORD")

            with yaspin(text="Logging in to Steam", color="yellow"):
                self.helper.xpath_locator(STEAM_LOGIN_EMAIL_XPATH)
                self.helper.xpath_fill(STEAM_LOGIN_EMAIL_XPATH, STEAM_USERNAME)

                self.helper.xpath_locator(STEAM_LOGIN_PASSWORD_XPATH)
                self.helper.xpath_fill(STEAM_LOGIN_PASSWORD_XPATH, STEAM_PASSWORD)

                self.helper.xpath_locator(STEAM_LOGIN_REMEMBER_ME_XPATH)
                self.helper.xpath_btn_click(STEAM_LOGIN_REMEMBER_ME_XPATH)

                self.helper.xpath_locator(STEAM_LOGIN_BTN_XPATH)
                self.helper.xpath_btn_click(STEAM_LOGIN_BTN_XPATH)

            if self.helper.xpath_locator(STEAM_AWAITING_2F).is_displayed:
                with yaspin(
                    text="Accept 2F authentication, waiting...", color="yellow"
                ) as spinner:

                    self.helper.xpath_locator(STEAM_AWAITING_2F, timeout=120)

                    self.helper.xpath_locator(STEAM_ACCOUNT_DROPDOWN)
                    spinner.write("> Logged in to steam")

                    cookies = self.driver.get_cookies()
                    self.helper.save_steam_cookies(cookies)

    def restore_session(self, cookies):
        """Cookies are valid since previous session, reuse"""
        with yaspin(
            text="Restoring cookies to previous session...", color="yellow"
        ) as spinner:
            self.driver.get(STEAM_LOGIN_PAGE)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            spinner.write("> Restored cookies")

    def claim_games(self):
        with yaspin(text="Claiming steam games...", color="yellow") as spinner:
            for tweet in self.tweets:
                self.driver.get(tweet.game_steam_link)

                game_name = self.helper.xpath_locator(STEAM_GAME_NAME).text
                game_image = self.helper.xpath_locator(STEAM_GAME_IMAGE).get_attribute(
                    "src"
                )

                game = Game(self.driver, self.helper, game_name, game_image)
                game.claim()
                spinner.write(f"> claimed {game_name}!")


class Game:
    def __init__(self, driver: webdriver.Firefox, helper: Helper, link, image) -> None:
        self.driver = driver
        self.helper = helper
        self.link = link
        self.image = image

    def claim(self):
        self.helper.xpath_btn_click(STEAM_GAME_CLAIM_BTN)
