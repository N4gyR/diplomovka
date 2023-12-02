# Import modules
from time import sleep
from utils.db_manager import get_bot
from utils.logger import Logger
from utils.config_parser import read_json
from utils.config_parser import Constants
from modules.facebook import facebook_functions as fb

# logs
logger = Logger(name="facebook_l1_scrapper").logger

# constants
config_dic = read_json("config.json")
consts = Constants(config_dic)


class ScrappingBot:
    def __init__(self):
        self.url = consts.facebook_url
        # Get the random user mail with password from the database table credentials
        self.email, self.password = get_bot("facebook", "scrapper", "1")

    def run(self, driver):
        try:
            logger.info("START Impostor L1 bot")
            if fb.login(driver, self.email, self.password):
                sleep(5)
                logger.info("Login success with email: " + self.email)
                # logger.info("search random users")
                # logger.info("search random users")
                # profiles = fb.search_random_users(driver, 10)
                # logger.info("scrap profile info")
                # fb.scrapp_profile_info(driver, profiles)
                # logger.info("END Impostor L1 bot")
            else:
                logger.error("Login failed with email: " + self.email)
                raise Exception("Login failed")
        except Exception as exc:
            logger.error(str(exc))
            raise Exception("Impostor L1 bot failed: " + str(exc))