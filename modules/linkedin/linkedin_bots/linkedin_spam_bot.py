# Import modules
from utils.logger import Logger
from utils.config_parser import read_json
from utils.config_parser import Constants
from modules.linkedin import linkedin_functions as lf

# constants
config_dic = read_json("config.json")
consts = Constants(config_dic)

# logs
logger = Logger(name="linkedin functions").logger


class LinkedinSpamBot:
    def __init__(self):
        self.name = consts.linkedin_username
        self.password = consts.linkedin_password
        self.url = consts.linkedin_url

    def run(self, driver):
        try:
            logger.info("START linkedin bot")
            lf.login(driver)
            logger.info("END linkedin bot")
        except Exception as exc:
            logger.error(str(exc))
            raise Exception("Linkedin spam bot failed: " + str(exc))
