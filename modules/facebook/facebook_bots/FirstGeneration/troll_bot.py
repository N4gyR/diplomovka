# Import modules
from utils.logger import Logger
from utils.config_parser import read_json
from utils.config_parser import Constants
from modules.facebook import facebook_functions as fb

# logs
logger = Logger(name="facebook troll bot").logger

# constants
config_dic = read_json("config.json")
consts = Constants(config_dic)