# TWITTER CONSTANTS

## LOGIN
TWITTER_LOGIN_PAGE = "https://x.com/i/flow/login?lang=en"
TWITTER_CLOSE_SUGGESTED_GOOGLE_LOGIN = '//*[@id="close"]'
TWITTER_LOGIN_EMAIL_XPATH = '//*[@autocomplete="username"]'
TWITTER_LOGIN_PASSWORD_XPATH = '//*[@autocomplete="current-password"]'
TWITTER_LOGIN_NEXT_BTN_XPATH = "//button[@role='button' and @type='button']//span[text()='Next']"
TWITTER_LOGIN_BTN_XPATH = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div/span/span'
TWITTER_LOGIN_WRONG_PASSWORD_XPATH = '//*[@id="layers"]/div[2]/div/div/div/div'
TWITTER_ACCEPT_COOKIES_XPATH = "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/span/span"

## USER PAGE
TWITTER_STEAM_GAMES_PC_LINK = "https://twitter.com/SteamGamesPC"

## PINNED TWEET
TWITTER_PINNED_TWEET = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[1]/div/div/article/div/div/div[2]'
TWITTER_PINNED_TWEET_TEXT = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[1]/div/div/article/div/div/div[2]/div[2]/div[2]/div"
TWITTER_PINNED_TWEET_IMAGE = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[1]/div/div/article/div/div/div[2]/div[2]/div[3]/div/div/div/div/div/div/a/div/div[2]/div/img"

###################################################################################################

# STEAM CONSTANTS

## LOGIN
STEAM_LOGIN_PAGE = "https://steamcommunity.com/login/home/?goto=login"
STEAM_LOGIN_EMAIL_XPATH = '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[1]/input'
STEAM_LOGIN_PASSWORD_XPATH = '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[2]/input'
STEAM_LOGIN_BTN_XPATH = '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[4]/button'
STEAM_LOGIN_REMEMBER_ME_XPATH = '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[3]/div/div[2]'
STEAM_LOGIN_WRONG_PASSWORD_XPATH = '//*[@id="layers"]/div[2]/div/div/div/div'
STEAM_AWAITING_2F = '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/div[2]'
STEAM_ACCOUNT_DROPDOWN = '//*[@id="account_pulldown"]'
STEAM_GAME_NAME = '//*[@id="appHubAppName"]'
STEAM_GAME_IMAGE = '//*[@id="gameHeaderImageCtn"]/img'
STEAM_GAME_CLAIM_BTN = (
    '//*[@id="game_area_purchase_section_add_to_cart_1020633"]/div[2]/div/div[2]/a/span'
)
