from abc import ABC, abstractmethod
from selenium.webdriver import Chrome

class BaseSocialBot(ABC):
    def __init__(self, driver_path, email, password):
        self.driver_path = driver_path
        self.email = email
        self.password = password
        self.driver = None

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def search(self):
        pass
    
    @abstractmethod
    def like(self):
        pass

    @abstractmethod
    def follow(self):
        pass
    
    @abstractmethod
    def unfollow(self):
        pass
    
    @abstractmethod
    def write_message(self, recipient, message):
        pass
    
    @abstractmethod
    def comment(self, post, comment):
        pass
    
    @abstractmethod
    def check_ban(self):
        pass
