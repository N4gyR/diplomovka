# Import modules
from utils.logger import Logger
from utils.config_parser import read_json
from utils.config_parser import Constants
from modules.facebook import facebook_functions as fb

# logs
logger = Logger(name="facebook impostor bot").logger

# constants
config_dic = read_json("config.json")
consts = Constants(config_dic)



class ImpostorBot:
    def __init__(self):
        self.url = consts.facebook_url
        self.comments = []

    def run(self, driver):
        try:
            logger.info("START Impostor L1 bot")
            fb.login(driver)
            # search for random post
            fb.search(driver, "univerzita komenskeho")
            # add random tilting comment
            fb.switch_to_people(driver)
            fb.make_connections(driver, 1)
            logger.info("END Impostor L1 bot")
        except Exception as exc:
            logger.error(str(exc))
            raise Exception("Impostor L1 bot failed: " + str(exc))