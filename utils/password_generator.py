import random
import string

#from utils.logger import Logger
#logger = Logger(name="password_generator").logger


def generate_password(length=12):
    #logger.info("START generate_password")
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    #logger.info("END generate_password")
    return password


print(generate_password())