import time

import faker
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.Login_Page import Login_Page_Class
from pageObjects.Registration_Page import Registration_Page_Class
from utilities.ReadConfig import ReadConfigClass
from utilities.Logger import log_generator_class

@pytest.mark.usefixtures("driver_setup")
class Test_User_Profile_Class_001:
    # Reading the data from the config file
    email = ReadConfigClass.geta_data_for_email()
    password = ReadConfigClass.geta_data_for_password()
    key1 = ReadConfigClass.section1_data()

    # Initializing the logger, called loggen_method from loggenerator class in utitlties folder
    log = log_generator_class.loggen_method()
    # Initializing the driver
    driver = None
    """Test cases for the UserProfile class."""
    @pytest.mark.sanity
    @pytest.mark.group1
    @pytest.mark.flaky(reruns=0, reruns_delay=2)
    def test_verify_CredKart_Url_001(self):
        """Test verify_credkart_url method with valid URL."""
        #driver = driver_setup
        # self.log.debug("This is debug")
        # self.log.info("This is info")
        # self.log.warning("This is warning")
        # self.log.error("This is error")
        # self.log.critical("This is critical")
        self.log.info("Testcase test_verify_CredKart_Url_001 is started")
        self.driver.get("https://automation.credence.in/")
        self.log.info("Opening Browser")
        self.log.info("Going to CredKart URL ->https://automation.credence.in")
        self.log.info("Checking Page Title")
        if self.driver.title == "CredKart":
            self.log.info(f"Page Title:'{self.driver.title}' is  matches with expected title")
            #print("Test passed: Title matches with expected title")
            self.log.info("Taking Screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_verify_CredKart_Url_001_pass.png")
            self.log.info("Testcase test_verify_CredKart_Url_001 is passed")
            self.log.info("Testcase test_verify_CredKart_Url_001 is completed\n")
            assert True
        else:
            self.log.info("Taking Screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_verify_CredKart_Url_001_fail.png")
            self.log.info("Testcase test_verify_CredKart_Url_001 is failed")
            self.log.info("Testcase test_verify_CredKart_Url_001 is completed\n")
            assert False

    @pytest.mark.sanity
    @pytest.mark.group1
    @pytest.mark.flaky(reruns=1, reruns_delay=2)
    def test_CredKart_User_Login_002(self):
        """Test verify_user_login method with valid credentials."""
        #self.driver = driver_setup
        self.lp = Login_Page_Class(self.driver)
        self.driver.maximize_window()
        self.driver.get("https://automation.credence.in/login")

        # Enter the username
        # username = driver.find_element(By.ID, "email")
        # username.send_keys("Credencetest@test.com")
        self.lp.Enter_Email(self.email)
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")
        print(f"Dummy data: {self.key1}")

        # Enter the password
        # password = driver.find_element(By.ID, "password")
        # password.send_keys("Credence@1234")
        self.lp.Enter_Password(self.password)

        # Click the login button
        #driver.find_element(By.CLASS_NAME, "btn").click()
        self.lp.Click_submit_Button()

        # Verify that the user is logged in
        # try:
        #     #MenuButton = driver.find_element(By.CLASS_NAME, "dropdown-toggle")
        #     MenuButton = driver.find_element(By.XPATH, "//a[@class='dropdown-toggle']")
        #     time.sleep(5)  # Wait for the page to load completely before checking the visibility of the element.
        #     assert MenuButton.is_displayed(), "User is not logged in"
        #     print("User is logged in")
        # except:
        #     print("User is not logged in")
        if self.lp.verify_user_Login_or_registration() == "pass": # wrong logic
            print("User is logged in")
            self.driver.save_screenshot(".\\Screenshots\\test_CredKart_User_Login_002_pass.png")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_CredKart_User_Login_002_fail.png")
            print("User is not logged in")
            assert False



    @pytest.mark.sanity
    @pytest.mark.group1
    @pytest.mark.flaky(reruns=1, reruns_delay=2)
    def test_CredKart_User_Registration_003(self, faker):
        """Test verify_user_login method with valid credentials."""
        #self.driver = driver_setup
        self.rp = Registration_Page_Class(self.driver)
        self.driver.get("https://automation.credence.in/register")
        # random_name = faker.name()
        # random_email = faker.email()
        # Enter the Name
        self.rp.Enter_Name("nilamgodse")
        # Enter the Email
        self.rp.Enter_Email("akshaykaranjekare@gmail.com")
        # Enter the Password
        self.rp.Enter_Password("Credence@123")
        # Enter the Confirm Password
        self.rp.Enter_Confirm_Password("Credence@123")
        # Click the register button
        self.rp.Click_submit_Button()
        if self.rp.verify_user_Login_or_registration() == "pass":
            print("User is registered")
            self.driver.save_screenshot(".\\Screenshots\\test_CredKart_User_Registration_003_pass.png")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_CredKart_User_Registration_003_fail.png")
            print("User is not registered")
            assert False


"pytest -v -n auto --html=HtmlReports/my_report.html --browser chrome"

# robot
# bdd
# api automation
# database automation
#web automation --> syllabus
# uipath
# tosca
# work fusion

