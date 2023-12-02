from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

# Import modules
from utils.logger import Logger
from utils.config_parser import read_json
from utils.config_parser import Constants

# logs
logger = Logger(name="instagram functions").logger

# constants
config_dic = read_json("config.json")
consts = Constants(config_dic)


def login(driver) -> bool:
    return False
