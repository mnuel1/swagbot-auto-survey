from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import WebDriverException

class SwagBot:
    def __init__(self, username, pw):
        # Use the Microsoft Edge WebDriver executable path
        self.driver = webdriver.Edge()  # Replace with the actual path to msedgedriver.exe
        self.username = username
        self.pw = pw
        self.driver.get("https://www.swagbucks.com/p/login")
        sleep(2)
        self.driver.find_element(By.ID, 'sbxJxRegEmail').send_keys(username)  # Using ID, replace with the actual ID attribute valuefind_element()
        self.driver.find_element(By.ID,"sbxJxRegPswd").send_keys(pw)  # Simplified XPath
        sleep(2)
        self.driver.find_element(By.ID,"loginBtn").click()  # Use element ID
        sleep(50)  # Time for manual verification
    
        self.driver.get('https://www.swagbucks.com/surveys')
        sleep(2)

    def survey(self):        
        
        max_retries = 3
        retries = 0

        while retries < max_retries:
            try:
                # Locate the dropdown element and open it
                dropdown = self.driver.find_element(By.CLASS_NAME, "questionDropdownContainer")
                ActionChains(self.driver).move_to_element(dropdown).click().perform()

                # Select an answer by its index (e.g., "Beer" has an index of 1)
                answer_index = 1
                self.driver.find_element(By.XPATH, f"//span[@data-index='{answer_index}']").click()

                # Click the "Answer" button
                answer_button = self.driver.find_element(By.CLASS_NAME, "surveyDashboardCTA")
                answer_button.click()

                # Wait for the response to be processed (you may need to adjust the sleep time)
                sleep(5)
                return  # Successfully answered the survey
            except (ElementNotInteractableException, WebDriverException):
                # Handle exceptions by refreshing the page and retrying
                print("Encountered an error. Refreshing the page and retrying...")
                self.driver.refresh()
                retries += 1

        print(f"Failed to answer the survey after {max_retries} retries.")

            
my_bot = SwagBot("abc888043@gmail.com", "Hellomyworld123")  # Replace with your actual username and password

while (True):
    my_bot.survey()
