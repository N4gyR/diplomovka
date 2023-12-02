# Import modules
from utils.logger import Logger
from utils.config_parser import read_json
from utils.config_parser import Constants
from modules.facebook import facebook_functions as fb

# logs
logger = Logger(name="facebook hoax L1 bot").logger

# constants
config_dic = read_json("config.json")
consts = Constants(config_dic)


class HoaxBot:
    def __init__(self):
        self.url = consts.facebook_url
        self.comments = []

    def run(self, driver, count=1, time=5):
        try:
            logger.info("START facebook hoax L1 bot")
            fb.login(driver)
            for i in count:
                # search for random post
                fb.search(driver)
                # add some hoax comments
                fb.add_hoax_comments(driver)
                # wait and save responses (meanwhile check if not banned)
                fb.check_respones(driver, time=5)
            logger.info("END facebook hoax L1 bot")
        except Exception as exc:
            logger.error(str(exc))
            raise Exception("Impostor L failed: " + str(exc))