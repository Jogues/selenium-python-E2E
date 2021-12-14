import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

EmailField = (By.XPATH, '//*[@id="__next"]/div[1]/div/div[2]/form/div[1]/div/div/input')
FullNameField = (By.XPATH, '//*[@id="__next"]/div[1]/div/div[2]/form/div[2]/div/div/input')
RegisterButton = (By.XPATH, '//*[@id="__next"]/div[1]/div/div[2]/form/div[3]/button')
ErrorMessageEmail = (By.XPATH, '//*[@id="__next"]/div[1]/div/div[2]/form/div[1]/div/span')
MasukField = (By.LINK_TEXT, 'Masuk')
RegisterUrl = 'https://accounts.kitabisa.com/register?type=email'
LoginUrl = 'https://accounts.kitabisa.com/login?type=email'
RegisterOtpUrl = 'https://accounts.kitabisa.com/register/otp?type=email'


class TestRegisterUser(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(RegisterUrl)

    #test error message when user input incorrect format of email
    def test_error_message_invalid_email(self):
        wait = WebDriverWait(self.driver, 20)
        email = wait.until(EC.visibility_of_element_located(EmailField))
        email.send_keys('isaactest7')
        wait.until(EC.visibility_of_element_located(ErrorMessageEmail), 'Hanya diisi dengan nomor ponsel atau email yang valid.')

    #test error message when user input incorrect format of phone number
    def test_error_message_invalid_phone(self):
        wait = WebDriverWait(self.driver, 20)
        email = wait.until(EC.visibility_of_element_located(EmailField))
        email.send_keys('0837484')
        wait.until(EC.visibility_of_element_located(ErrorMessageEmail), 'Hanya diisi dengan nomor ponsel atau email yang valid.')

    #test validation redirection to login page via Masuk link text
    def test_redirection_to_login_page(self):
        wait = WebDriverWait(self.driver, 20)
        masuk = wait.until(EC.visibility_of_element_located(masukField))
        masuk.click()
        time.sleep(3)
        currentUrl = self.driver.current_url
        assert currentUrl == LoginUrl

    #test validation registration and redirect to email otp page
    def test_register_successfully(self):
        wait = WebDriverWait(self.driver, 20)
        email = wait.until(EC.visibility_of_element_located(EmailField))
        email.send_keys('isaactest7@gmail.com')
        fullName = wait.until(EC.visibility_of_element_located(FullNameField))
        fullName.send_keys('UserFullName')
        daftarBtn = wait.until(EC.visibility_of_element_located(RegisterButton))
        daftarBtn.click()
        time.sleep(3)
        currentUrl = self.driver.current_url
        assert currentUrl == RegisterOtpUrl

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
