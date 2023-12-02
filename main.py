from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import sqlite3

# Import modules
from utils.logger import Logger
from utils.config_parser import read_json
from utils.config_parser import Constants
from modules.email import gmail_functions as gf
from modules.email import azet_functions as af

# Bots
from modules.facebook.facebook_bots.FirstGeneration.scrapping_bot import ScrappingBot


def main():
    try:
        # Logging
        logger = Logger(name=__name__).logger
        logger.info("---START---")

        # Load config file
        logger.info("START loading config file")
        config_dic = read_json("config.json")
        consts = Constants(config_dic)
        logger.info("END loading config file")

        # Start driver
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-notifications")
        options.add_argument("--log-level=3")
        options.add_argument("--start-maximized")
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--single-process')
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("disable-infobars")

        logger.info("Starting webdriver")
        # webdriver = Chrome(options=options, service=Service(ChromeDriverManager().install()))
        webdriver = Chrome(
            service=Service("C:\\Users\\admin\\OneDrive\\Počítač\\skola\\diplmovka\\code\\drivers\\chromedriver.exe"),
            options=options)
        #   hide java script
        webdriver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        webdriver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source":
                "const newProto = navigator.__proto__;"
                "delete newProto.webdriver;"
                "navigator.__proto__ = newProto;"
        })

        # call for specific bot on chosen social network
        ## Run Facebook scrapper bot
        logger.info("START facebook L1 scrapper bot")
        facebook_bot = ScrappingBot()
        logger.info("START bot.run()")
        facebook_bot.run(webdriver)
        logger.info("END bot.run()")
        sleep(10)

        ## Run Instagram spam bot
        # instagram_bot = InstagramSpamBot()
        # logger.info("START bot.run()")
        # instagram_bot.run(webdriver)
        # logger.info("END bot.run()")
        # sleep(10)

        ## Run Twitter spam bot
        # twitter_bot = TwitterSpamBot()
        # logger.info("START bot.run()")
        # twitter_bot.run(webdriver)
        # logger.info("END bot.run()")
        # sleep(10)

        ## Run LinkedIn spam bot
        # linkedin_bot = LinkedinSpamBot()
        # logger.info("START bot.run()")
        # linkedin_bot.run(webdriver)
        # logger.info("END bot.run()")
        # sleep(10)
        sleep(5)

        logger.info("---END---")
    except Exception as exc:
        logger.error(str(exc))
        # raise Exception(str(exc))


main()
