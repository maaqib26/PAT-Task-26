from TestData.IDMBData import InputData
from TestLocators.IDMBLocators import Locators
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class Test_IDMB:


    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 15)
        self.driver.get(InputData.url)
        yield
        self.driver.close()

    def test_fill_data(self,boot):
        try:
            # Creating an instance for action class
            actions = ActionChains(self.driver)
            # Clicking on the expand all button
            expand_all_button = self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators().expand_all_locator)))
            expand_all_button.click()

            # Entering the data in the name field
            name = self.wait.until(EC.presence_of_element_located((By.NAME,Locators().name_locator)))
            # Moving to the element using action chains
            actions.move_to_element(name).perform()
            name.send_keys('Logan Williams')


            from_date = self.wait.until(EC.presence_of_element_located((By.NAME,Locators().from_year_locator)))
            # Moving to the element using action chains
            actions.move_to_element(from_date).perform()
            from_date.send_keys('1999')

            to_date = self.wait.until(EC.presence_of_element_located((By.NAME, Locators.to_year_locator)))
            # Moving to the element using action chains
            actions.move_to_element(to_date).perform()
            to_date.send_keys('2010')

            # Selecting desired options in the "Page Topics" section
            page_topic = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.page_topics_selection_locator)))
            # Moving to the element using action chains
            actions.move_to_element(page_topic).perform()
            page_topic.click()

            topic = self.wait.until(EC.element_to_be_clickable((By.NAME, Locators.search_within_topic_locator)))
            # Moving to the element using action chains
            actions.move_to_element(topic).perform()
            topic.click()

            option = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().drop_down_option_locator)))
            option.click()

            #Selecting the gender
            gender_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().gender_identity_locator)))
            # Moving to the element using action chains
            actions.move_to_element(gender_button).perform()
            gender_button.click()

            #Including adult names
            adult_name_button = self.wait.until(EC.element_to_be_clickable((By.ID, Locators().adult_name_choice_locator)))
            # Moving to the element using action chains
            actions.move_to_element(adult_name_button).perform()
            adult_name_button.click()

            # Searching the results in the IDMB Site
            search_result = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().see_results_locator)))
            search_result.click()
            assert self.driver.current_url == InputData().expected_url
            print("SUCCESS: Searched the Data with Name {a},from date {b} and to_date {c}".format(a=InputData().name,
                                                                                                  b=InputData().from_date,
                                                                                                  c=InputData().to_date))

        except (NoSuchElementException, ElementNotVisibleException) as e:
            print("ERROR : ", e)


