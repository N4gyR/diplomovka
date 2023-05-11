from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
# Import modules
from utils.logger import Logger
from utils.config_parser import read_json
from utils.config_parser import Constants
from modules.linkedin.linkedin_bots.linkedin_spam_bot import LinkedinSpamBot


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

        # Create account manager
        logger.info("Create account manager")
        ##account_manager = AccountManager(config_dic['ACCOUNTS'])

        # Start driver
        options = Options()
        options.add_argument("--disable-notifications")
        options.add_argument("--start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
        options.add_experimental_option('useAutomationExtension', False) 
        webdriver = Chrome(options=options, service=Service(ChromeDriverManager().install()))

        # Run LinkedIn bot
        linkedin_bot = LinkedinSpamBot()
        logger.info("START bot.run()")
        linkedin_bot.run(webdriver)
        logger.info("END bot.run()")
        sleep(10)

        logger.info("---END---")
    except Exception as exc:
        logger.error(str(exc))
        # raise Exception(str(exc))


main()




