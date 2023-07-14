# selenium is syntactically goofy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class AccountMaker():

    LOGIN_BUTTON_XPATH = "/html/body/div[1]/div[1]/div[2]/header/div/div/div/div/a[2]"
    EMAIL_INPUT_ID = "PHONE_NUMBER_or_EMAIL_ADDRESS"
    EMAIL_VERINPUT_ID = "EMAIL_OTP_CODE-0"
    PHONE_INPUT_ID = "PHONE_NUMBER"

    
    def __init__(self, **kwargs):
        headless = kwargs.get("headless")
        self.phone = kwargs.get("phone")
        self.domain = kwargs.get("domain")
        self.timeout = kwargs.get("timeout", 30)

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        if headless:
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')

        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

        if self.timeout != 'inf':
            self.wait = WebDriverWait(self.driver, 30)
    
    def __get_element(self, by, content):
        return self.driver.find_element(by, content)
    
    def __wait_for_element(self, by, content, visible=True):
        if self.timeout == 'inf':
            while True:
                try:
                    element = self.driver.find_element(by, content)
                    if visible and not element.is_displayed():
                        continue
                except NoSuchElementException:
                    continue
                else:
                    return element
        elif visible:
            self.wait.until(EC.visibility_of_element_located((by, content)))
        else:
            self.wait.until(EC.presence_of_element_located((by, content)))
                    
    def __element_exists(self, by, content):
        try:
            element = self.driver.find_element(by, content)
        except NoSuchElementException:
            return False
        return element
    
    def create_account(self):
        self.driver.get("https://ubereats.com")
        
    def verify_email(self):
        pass
    
    def verify_phone(self):
        pass


if __name__ == "__main__":
    print("https://i.imgur.com/KCSQ0jb.jpeg")
