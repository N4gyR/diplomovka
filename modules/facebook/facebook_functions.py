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
logger = Logger(name="facebook functions").logger

# constants
config_dic = read_json("config.json")
consts = Constants(config_dic)


def login(driver, email, password) -> bool:
    logger.info("Facebook login START")
    try:
        driver.get(consts.facebook_url)
        WebDriverWait(driver, consts.delay_medium).until(
            EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        driver.find_elements(By.XPATH, "//button[@type='submit']")[2].click()
        logger.info("Facebook filling email")
        WebDriverWait(driver, consts.delay_medium).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        driver.find_element(By.ID, "email").send_keys(email)
        logger.info("Facebook filling password")
        WebDriverWait(driver, consts.delay_medium).until(
            EC.presence_of_element_located((By.ID, "pass"))
        )
        driver.find_element(By.ID, "pass").send_keys(password)
        logger.info("Facebook pressing login")
        driver.find_element(By.NAME, "login").click()
        WebDriverWait(driver, consts.delay_medium).until(
            EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Facebook']"))
        )
        logger.info("END Facebook login")
        return True
    except Exception as e:
        logger.error("Facebook login failed " + str(e))
        return False

def create_new_acc(driver) -> bool:
    return False


def search_random_users(driver, count=1):
    return None


def scrapp_profile_info(driver, profiles):
    return None