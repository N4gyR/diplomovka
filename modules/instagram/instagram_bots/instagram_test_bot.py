from instapy import InstaPy

# Import modules
from utils.logger import Logger
from utils.config_parser import read_json
from utils.config_parser import Constants
from modules.instagram import instagram_functions as If

# logs
logger = Logger(name="instagram test bot").logger

# constants
config_dic = read_json("config.json")
consts = Constants(config_dic)


class InstagramTestBot:
    def __init__(self):
        self.name = consts.instagram_username
        self.password = consts.instagram_password
        self.url = consts.instagram_url

    def run(self, driver):
        try:
            logger.info("START instagram bot")
            If.login(driver)
            logger.info("END instagram bot")
        except Exception as exc:
            logger.error(str(exc))
            raise Exception("Instagram spam bot failed: " + str(exc))



