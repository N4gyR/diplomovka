from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
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
        logger.info("Loading config file")
        config_dic = read_json("config.json")
        consts = Constants(config_dic)
        logger.info("Config file loaded successfully")

        # Create account manager
        logger.info("Create account manager")
        ##account_manager = AccountManager(config_dic['ACCOUNTS'])

##        # Start driver
##        options = Options()
##        options.add_argument("--disable-notifications")
##        options.add_argument("--start-maximized")
##        driver = Chrome(executable_path=consts.chromedriver_path, options=options)
##
##        # Run LinkedIn bot
##        logger.info("Run bot")
##        linkedin_bot = LinkedinSpamBot()
##        linkedin_bot.run(driver)


        logger.info("---END---")
    except Exception as exc:
        logger.error(str(exc))
        # raise Exception(str(exc))


main()




