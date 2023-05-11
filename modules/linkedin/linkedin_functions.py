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
logger = Logger(name="linkedin functions").logger

# constants
logger.info("Loading config file")
config_dic = read_json("config.json")
consts = Constants(config_dic)
logger.info("Config file loaded successfully")


def login(driver) -> bool:
    """Function navigates to login screen in LI portal and logs in by filling form and clicking sign in button.
    Params:\n\tdriver(selenium.webdriver.Chrome) - webdriver under which LI is running\n\turl(str) - None or url to navigate
    Returns:
        True when robot managed to login successfuly\n
        False when some login element was not found
    """
    logger.info("START linkedin login")
    driver.get(consts.linkedin_url)
    sleep(5)
    try:
        logger.info("finding username")
        username_editbox = driver.find_element(By.ID, 'session_key')
        username_editbox.send_keys(consts.linkedin_username)
        sleep(0.2)
        logger.info("finding password")
        pw_editbox = driver.find_element(By.ID, 'session_password')
        pw_editbox.send_keys(consts.linkedin_password)
        logger.info('credentials successfully filled')
        sleep(0.2)

        try:
            logger.info('signing in')
            driver.execute_script(
                "document.querySelector('button[type=\"submit\"][aria-label=\"Sign in\"]').id = \"signIn\"")
            sign_in = driver.find_element(By.ID, "signIn")
        except:
            sign_in = driver.find_element(By.XPATH, "//button[contains(text(), 'Sign in')]")

        sign_in.click()

        WebDriverWait(driver, consts.delay_medium).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'search-global-typeahead__input')))
        logger.info("END linkedin login")
        return True
    except Exception as e:
        logger.error(str(e))
        logger.info("FAILED logging")
        return False


def search(driver, search_string):
    try:
        logger.info("START search")
        WebDriverWait(driver, consts.delay_short).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'search-global-typeahead__input')))

        search_field = driver.find_element(By.CLASS_NAME, 'search-global-typeahead__input')
        search_field.send_keys(search_string)

        sleep(0.5)
        logger.info('Entering search string')
        search_field.send_keys(Keys.ENTER)
        sleep(2)
        logger.info("END search")
    except Exception as exc:
        logger.error(exc)
        raise Exception("Error durring searching " + str(exc))


def switch_to_people(driver):
    logger.info("START switch to people filter")
    try:
        sleep(2)
        people_button = driver.find_element(By.XPATH, "//a[contains(text(), 'See all people results')]")
        people_button.click()
        sleep(2)
        logger.info("END switch to people filter")
        return None
    except Exception as e:
        logger.info('People button by querySelector was not found: ' + str(e))
    try:
        driver.execute_script(r'document.getElementsByClassName("mr2")[0].id = "ppl"')
        people_button = driver.find_elements(By.ID, 'ppl')
        people_button.click()
        logger.info("END switch to people filter")
    except Exception as exc:
        logger.error(str(exc))
        raise Exception("Error while switch on people filter: " + str(exc))
    return None


def make_connections(driver, param):
    return None