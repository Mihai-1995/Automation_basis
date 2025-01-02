from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import unittest

class Test_Alerts(unittest.TestCase):
    driver = None
    LINK = "https://the-internet.herokuapp.com/javascript_alerts"
    BUTTON_JS_ALERT = (By.XPATH, '//button[@onclick="jsAlert()"]')
    BUTTON_JS_CONFIRM =(By.XPATH,'//button[@onclick="jsConfirm()"]')
    BUTTON_JS_PROMPT =(By.XPATH,'//button[@onclick="jsPrompt()"]')
    MESSAGE = (By.ID, "result")

    def setUp(self)->None:
     chrome_options = Options()
     chrome_options.add_argument( "--disable-search-engine-choice-screen")
     self.driver = webdriver.Chrome(options=chrome_options)
     self.driver.maximize_window()
     self.driver.implicitly_wait(5)
     self.driver.get(self.LINK)


    def tearDown(self)->None:
     self.driver.close()

    def click(self,locator):
     self.driver.find_element(*locator).click()

    def get_text(self,locator):
     return self.driver.find_element(*locator).text

    def test_click_js_alert(self):
      self.click(self.BUTTON_JS_ALERT)
      alert = self.driver.switch_to.alert
      alert.accept()
      expected_message= 'You successfully clicked an alert'
      actual_message= self.get_text(self.MESSAGE)
      self.assertEqual(expected_message, actual_message),'message is not there'

    def test_accept_js_confirm(self):
        self.click(self.BUTTON_JS_CONFIRM)
        alert = self.driver.switch_to.alert
        alert.dismiss()
        expected_message = 'You clicked: Cancel'
        actual_message = self.get_text(self.MESSAGE)
        self.assertEqual(expected_message, actual_message), 'message is not there'

    def test_accept_js_prompt(self):
        self.click(self.BUTTON_JS_PROMPT)
        alert = self.driver.switch_to.alert
        alert.accept()
        expected_message = 'You entered: null'
        actual_message = self.get_text(self.MESSAGE)
        self.assertEqual(expected_message, actual_message), 'message is not there'

    def test_complete_alert_js_prompt(self):
        self.click(self.BUTTON_JS_PROMPT)
        alert = self.driver.switch_to.alert
        time.sleep(2)
        input_text = "TEST ALERT"
        alert.send_keys(input_text)
        time.sleep(2)
        alert.accept()
        expected_message ="You entered: " + input_text
        time.sleep(2)
        actual_message = self.get_text(self.MESSAGE)
        self.assertEqual(expected_message, actual_message), 'message is not there'

    def test_cancel_aler_js_prompt(self):
        self.click(self.BUTTON_JS_PROMPT)
        alert = self.driver.switch_to.alert
        alert.dismiss()
        expected_message = 'You entered: null'
        actual_message = self.get_text(self.MESSAGE)
        self.assertEqual(expected_message, actual_message), 'something is not good'