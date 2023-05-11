import json
from utils.logger import Logger

logger = Logger(name="config_parser").logger


class Constants(object):
    """A class to represent config data collection.

    Attributes:
        data_dic (dic) - dictionary containing data from config file
    """

    def __init__(self, data_dic):
        # App constants
        self.debug_mode = data_dic["APP"]["DEBUG_MODE"]
        self.retry_no = data_dic["APP"]["RETRY_NUMBER"]
        self.succ_status_msg = data_dic["APP"]["SUCCESS_STATUS_MSG"]
        self.fail_status_msg = data_dic["APP"]["FAILURE_STATUS_MSG"]
        self.delay_short = data_dic["APP"]["WAIT_TIME_SHORT"]
        self.delay_medium = data_dic["APP"]["WAIT_TIME_MEDIUM"]
        self.delay_long = data_dic["APP"]["WAIT_TIME_LONG"]
        # Location constants
        self.log_path = data_dic["LOCATIONS"]["LOG"]
        self.chromedriver_path = data_dic["LOCATIONS"]["CHROMEDRIVER_PATH"]
        # Accounts constants
        self.linkedin_username = data_dic["ACCOUNTS"]["LINKEDIN_USERNAME"]
        self.linkedin_password = data_dic["ACCOUNTS"]["LINKEDIN_PASSWORD"]
        # Webportals constants
        self.facebook_url = data_dic["WEBPORTALS"]["FACEBOOK_URL"]
        self.instagram_url = data_dic["WEBPORTALS"]["INSTAGRAM_URL"]
        self.twitter_url = data_dic["WEBPORTALS"]["TWITTER_URL"]
        self.linkedin_url = data_dic["WEBPORTALS"]["LINKEDIN_URL"]
        logger.info("json read successfully")


def read_json(file_path):
    """Read data from config file in json format and return dictionary.
    Parameters:
        file_path (str) - config file location
    Returns:
        dictionary
    Throws:
        None
    """
    try:
        logger.info("reading json")
        with open(file_path, "r") as f:
            return json.load(f)
    except Exception as exc:
        logger.error(str(exc))
        raise Exception(str(exc))
