import logging
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import random

# Import modules
from utils.logger import Logger
from utils.config_parser import read_json
from utils.config_parser import Constants
from utils import db_manager as dm
from utils import password_generator

# logs
logger = Logger(name="azet functions").logger

# constants
config_dic = read_json("config.json")
consts = Constants(config_dic)


def create_new_acc(driver, conn, c) -> bool:
    logger.info("START create_new_acc")
    action = ActionChains(driver)
    try:
        id, first_name, last_name, date_of_birth, gender, nickname = dm.get_random_phantom_profile(conn, c)
        logger.info(
            f"Creating mail account for profile: id:{id} first_name:{first_name} last_name:{last_name} date_of_birth:{date_of_birth} gender:{gender} nickname:{nickname}")
        driver.get(consts.azet_url)
        sleep(5)
        try:
            logger.info("Looking for cookies")
            cookie_iframe = WebDriverWait(driver, consts.delay_short).until(
                EC.visibility_of_element_located((By.XPATH, r'//iframe[@title="SP Consent Message"]')))
            logger.info("Switch to iframe")
            driver.switch_to.frame(cookie_iframe)
            sleep(3)
            logger.info("Accept cookie")
            action.move_to_element(driver.find_element(By.XPATH, r'//button[@title="Prijať všetko"]')).click().perform()
            logger.info("Switch back to default content")
            driver.switch_to.default_content()
        except:
            pass
        logger.info("Opening mail button")
        email_button = WebDriverWait(driver, consts.delay_medium).until(
            EC.visibility_of_element_located((By.XPATH, r'//span[text()="E-mail"]')))
        action.move_to_element(email_button).click().perform()

        sleep(5)
        logger.info("Opening register button")
        register_button = WebDriverWait(driver, consts.delay_medium).until(
            EC.visibility_of_element_located((By.ID, 'register')))
        action.move_to_element(register_button).click().perform()

        sleep(5)
        logger.info("Send nickname")
        nickname_input = WebDriverWait(driver, consts.delay_medium).until(
            EC.visibility_of_element_located((By.XPATH, r'//input[@placeholder="Názov účtu"]')))
        action.move_to_element(nickname_input).click().perform()
        sleep(2)
        nickname_input.send_keys(nickname)
        sleep(3)
        action.move_to_element(driver.find_element(By.XPATH, r'//input[@value="Ďalej"]')).click().perform()

        sleep(5)
        logger.info("Fill gender, birthdate, city")
        if gender == "M":
            gender_check_button = WebDriverWait(driver, consts.delay_medium).until(
                EC.visibility_of_element_located((By.ID, 'sexMan')))
        else:
            gender_check_button = WebDriverWait(driver, consts.delay_medium).until(
                EC.visibility_of_element_located((By.ID, 'sexWoman')))
        action.move_to_element(gender_check_button).click().perform()
        sleep(2)
        day_input = driver.find_element(By.NAME, 'day')
        action.move_to_element(day_input).click().perform()
        sleep(2)
        day_input.send_keys(date_of_birth.split("-")[2])
        sleep(2)
        month_input = driver.find_element(By.NAME, 'month')
        action.move_to_element(month_input).click().perform()
        sleep(2)
        month_input.send_keys(date_of_birth.split("-")[1])
        sleep(2)
        year_input = driver.find_element(By.NAME, 'year')
        action.move_to_element(year_input).click().perform()
        sleep(2)
        year_input.send_keys(date_of_birth.split("-")[0])
        sleep(2)
        city_input = driver.find_element(By.NAME, 'city')
        action.move_to_element(city_input).click().perform()
        for char in "Nitra":
            sleep(random.uniform(0.1, 0.4))
            city_input.send_keys(char)
        sleep(2)
        action.move_to_element(driver.find_elements(By.XPATH, r'//input[@value="Ďalej"]')[1]).click().perform()

        sleep(5)
        password = password_generator.generate_password()
        logger.info(f"password: {password}")
        logging.info("Fill password, agree with conditions")
        password_input = WebDriverWait(driver, consts.delay_medium).until(
            EC.visibility_of_element_located((By.NAME, 'password')))
        action.move_to_element(password_input).click().perform()
        sleep(2)
        password_input.send_keys(password)
        sleep(2)
        action.move_to_element(driver.find_element(By.NAME, "marketing")).click().perform()
        sleep(2)
        action.move_to_element(driver.find_element(By.NAME, "eula")).click().perform()
        sleep(2)
        action.move_to_element(driver.find_element(By.XPATH, r'//input[@value="Dokončiť"]')).click().perform()
        sleep(5)

        logger.info("Continue to email")
        continue_button = WebDriverWait(driver, consts.delay_medium).until(
            EC.visibility_of_element_located((By.NAME, '//input[@value="Pokračovať na Azet"]')))
        sleep(2)
        action.move_to_element(continue_button).click().perform()
        sleep(1000)
        logger.info("END create_new_acc")
        return True

    except Exception as e:
        raise Exception("Error while creating azet acc: " + str(e))


