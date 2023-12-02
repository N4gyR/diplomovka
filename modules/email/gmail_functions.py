import logging
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Import modules
from utils.logger import Logger
from utils.config_parser import read_json
from utils.config_parser import Constants
from utils import db_manager as dm
from utils import password_generator

# logs
logger = Logger(name="gmail functions").logger

# constants
config_dic = read_json("config.json")
consts = Constants(config_dic)


def create_new_acc(driver, conn, c) -> bool:
    try:
        # get profile
        id, first_name, last_name, date_of_birth, gender, nickname = dm.get_random_phantom_profile(conn, c)
        logger.info(
            f"Creating mail account for profile: {id} {first_name} {last_name} {date_of_birth} {gender} {nickname}")
        driver.get(consts.gmail_url)
        sleep(5)
        create_acc = WebDriverWait(driver, consts.delay_medium).until(
            EC.visibility_of_element_located((By.XPATH, r"//span[text()='Create account']")))
        create_acc.click()
        sleep(1.5)
        person_use = WebDriverWait(driver, consts.delay_medium).until(
            EC.visibility_of_element_located((By.XPATH, r"//span[text()='For my personal use']")))
        person_use.click()
        sleep(1.5)

        # fill name
        logger.info("Filling name")
        input_first_name = driver.find_element(By.NAME, "firstName")
        input_first_name.send_keys(first_name)
        sleep(1.5)
        input_last_name = driver.find_element(By.NAME, "lastName")
        input_last_name.send_keys(last_name)
        sleep(1.5)
        driver.find_element(By.XPATH, '//span[text()="Next"]').click()
        sleep(1.5)

        # fill birthdate
        logger.info("Filling birthdate")
        input_day = WebDriverWait(driver, consts.delay_medium).until(
            EC.visibility_of_element_located((By.NAME, "day")))
        input_day.send_keys(date_of_birth.split("-")[2])
        sleep(1.5)
        input_month = Select(driver.find_element(By.ID, "month"))
        input_month.select_by_index(int(date_of_birth.split("-")[1]))
        sleep(1.5)
        input_year = driver.find_element(By.NAME, "year")
        input_year.send_keys(date_of_birth.split("-")[0])
        sleep(1.5)
        input_gender = Select(driver.find_element(By.ID, "gender"))
        input_gender.select_by_index(1 if gender == "M" else 2)
        sleep(1.5)
        driver.find_element(By.XPATH, '//span[text()="Next"]').click()
        sleep(1.5)

        # copy email address
        logger.info("Filling email")
        email = WebDriverWait(driver, consts.delay_medium).until(
            EC.visibility_of_element_located((By.ID, "selectionc0"))).text
        print(email)
        driver.find_element(By.CSS_SELECTOR, 'div[aria-labelledby="selectionc0"]').click()
        sleep(1.5)
        driver.find_element(By.XPATH, '//span[text()="Next"]').click()
        sleep(1.5)

        # generate and fill password
        logger.info("Filling password")
        password = password_generator.generate_password()
        print(password)
        input_password = WebDriverWait(driver, consts.delay_medium).until(
            EC.visibility_of_element_located((By.NAME, "Passwd")))
        input_password.send_keys(password)
        sleep(1.5)
        input_password_again = driver.find_element(By.NAME, 'PasswdAgain')
        input_password_again.send_keys(password)
        sleep(1.5)
        driver.find_element(By.XPATH, '//span[text()="Next"]').click()
        sleep(1.5)

        sleep(10)

    except Exception as e:
        logger.error("Creation of new gmail acc failed: " + str(e))
    return False

