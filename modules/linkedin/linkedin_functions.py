# Import modules
import logging
import traceback
from time import sleep
import datetime
import os
import re
import shutil
from builtins import Exception
from keyring import get_password

import selenium

from selenium.common.exceptions import NoSuchElementException, \
    TimeoutException, \
    ElementClickInterceptedException, \
    JavascriptException, \
    StaleElementReferenceException, NoSuchWindowException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Import modules
from utils.logger import Logger
from utils.config_parser import read_json
from utils.config_parser import Constants

# constants
config_dic = read_json("config.json")
consts = Constants(config_dic)

# logs
logger = Logger(name="linkedin functions").logger


def login(driver) -> bool:
    """Function navigates to login screen in LI portal and logs in by filling form and clicking sign in button.
    Params:\n\tdriver(selenium.webdriver.Chrome) - webdriver under which LI is running\n\turl(str) - None or url to navigate
    Returns:
        True when robot managed to login successfuly\n
        False when some login element was not found
    Throws:\n\tReCaptchaException when recaptcha check appears shortly after login
    """
    logger.info("START linkedin login")
    driver.get(consts.linkedin_url)
    sleep(5)
    try:
##        logger.info("finding username")
##        username_editbox = driver.find_element_by(By.ID, 'username')
##        username_editbox.send_keys(consts.linkedin_username)
##        sleep(0.2)
##        logger.info("finding password")
##        pw_editbox = driver.find_element(By.ID, 'password')
##        pw_editbox.send_keys(consts.linkedin_password)
##        logger.info(f'Credentials successfully filled')
##        sleep(0.2)
##
##        try:
##            driver.execute_script(
##                "document.querySelector('button[type=\"submit\"][aria-label=\"Sign in\"]').id = \"signIn\"")
##            sign_in = driver.find_element(By.ID, "signIn")
##        except:
##            sign_in = driver.find_element_by_xpath("//button[contains(text(), 'Sign in')]")
##
##        sign_in.click()
##        sleep(10)
        logger.info("END linkedin login")
        return True
    except Exception as e:
        logger.error(str(e))
        logger.info("FAILED logging")
        return False
