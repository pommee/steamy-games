import os
import re
import sys
import time
import random
from selenium import webdriver
from constants import (
    TWITTER_CLOSE_SUGGESTED_GOOGLE_LOGIN,
    TWITTER_ACCEPT_COOKIES_XPATH,
    TWITTER_LOGIN_BTN_XPATH,
    TWITTER_LOGIN_EMAIL_XPATH,
    TWITTER_LOGIN_NEXT_BTN_XPATH,
    TWITTER_LOGIN_PAGE,
    TWITTER_LOGIN_PASSWORD_XPATH,
    TWITTER_PINNED_TWEET,
    TWITTER_PINNED_TWEET_IMAGE,
    TWITTER_PINNED_TWEET_TEXT,
    TWITTER_STEAM_GAMES_PC_LINK,
)
from helper import Helper
from yaspin import yaspin
from dotenv import load_dotenv
from steam import Steam
from tweet import Tweet


class Twitter:
    def __init__(self, driver, helper) -> None:
        self.driver = driver
        self.helper = helper

    def login(self):
        cookies = self.helper.load_twitter_cookies()

        if cookies is not None:
            self.restore_session(cookies)
        else:
            self.driver.get(TWITTER_LOGIN_PAGE)

            TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
            TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")

            with yaspin(text="Logging in to twitter...", color="yellow") as spinner:
                time.sleep(random.uniform(1.8, 3.2))
                self.helper.xpath_fill(TWITTER_LOGIN_EMAIL_XPATH, TWITTER_EMAIL)
                spinner.text = "Email filled..."
                self.helper.xpath_btn_click(TWITTER_LOGIN_NEXT_BTN_XPATH)
                spinner.text = "Clicked next button..."
                self.helper.xpath_fill(TWITTER_LOGIN_PASSWORD_XPATH, TWITTER_PASSWORD)
                spinner.text = "Password filled..."
                self.helper.xpath_btn_click(TWITTER_LOGIN_BTN_XPATH)
                spinner.text = "Clicked login button..."
                self.helper.xpath_btn_click(TWITTER_ACCEPT_COOKIES_XPATH)
                spinner.text = "Accepted cookies..."

                cookies = self.driver.get_cookies()
                self.helper.save_twitter_cookies(cookies)
                spinner.write("> Successfully logged in to Twitter")

    def restore_session(self, cookies):
        """Cookies are valid since previous session, reuse"""
        with yaspin(
            text="Restoring cookies to previous session...", color="yellow"
        ) as spinner:
            self.driver.get(TWITTER_STEAM_GAMES_PC_LINK)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            spinner.write("> Restored cookies")

    def get_tweets(self):
        found_games = list()

        with yaspin(text="Navigating to SteamGamesPC", color="yellow") as spinner:
            self.driver.get(TWITTER_STEAM_GAMES_PC_LINK)
            spinner.write("> Navigated to SteamGamesPc twitter page")

        with yaspin(
            text="Checking if there are any new games", color="yellow"
        ) as spinner:
            self.driver.get(TWITTER_STEAM_GAMES_PC_LINK)

            self.helper.xpath_locator(TWITTER_PINNED_TWEET)
            pinned_tweet_text = self.helper.xpath_locator(TWITTER_PINNED_TWEET_TEXT)

            steam_game_links = find_links(pinned_tweet_text.text)
            for link in steam_game_links:
                if "store.steampowered" not in link:
                    steam_game_links.remove(link)

            spinner.write(f"> Found {len(steam_game_links)} new game(s)")

            steam_game_image: str
            if steam_game_links is not None:
                steam_game_image = self.helper.xpath_locator(
                    TWITTER_PINNED_TWEET_IMAGE
                ).get_attribute("src")

            for game_link in steam_game_links:
                found_games.append(game_link)

            spinner.write(f"> Link: {steam_game_links}")
            spinner.stop()

            tweets = list()
            for found_game in found_games:
                tweets.append(Tweet(found_game))

            return tweets


def find_links(text):
    matches = re.findall(r"https?://\S+", text)
    return matches


def start():
    load_dotenv()

    TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
    TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")

    if TWITTER_EMAIL == "" or TWITTER_PASSWORD == "":
        raise sys.exit("Twitter email address and password needs to be filled in using TWITTER_EMAIL & TWITTER environment variables!")

    try:
        driver = webdriver.Firefox()
        helper = Helper(driver)

        twitter = Twitter(driver, helper)
        twitter.login()
        tweets = twitter.get_tweets()

        steam = Steam(driver, helper, tweets)
        steam.login()
        steam.claim_games()
    finally:
        driver.close()


if __name__ == "__main__":
    start()
