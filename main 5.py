# Import the necessary libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set your internet speeds, the path to your chrome driver, and your Twitter credentials
PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = YOUR CHROME DRIVER PATH
TWITTER_EMAIL = YOUR TWITTER EMAIL
TWITTER_PASSWORD = YOUR TWITTER PASSWORD

# Create a class to represent the internet speed twitter bot
class InternetSpeedTwitterBot:
    # When an object of this class is created, this function is run.
    # The "self" keyword represents the instance of the class (the object).
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)  # Open the browser
        self.up = 0  # Initialize upload speed
        self.down = 0  # Initialize download speed

    # This function opens the speedtest.net website and gets the internet speed
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")  # Open speedtest.net
        go_button = self.driver.find_element_by_css_selector(".start-button a")  # Find the go button
        go_button.click()  # Click the go button to start the speed test
        time.sleep(60)  # Wait for the speed test to complete
        # After waiting, find and store the upload and download speeds
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

    # This function logs into twitter and tweets at the provider
    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")  # Open twitter login page
        time.sleep(2)  # Wait for the page to load
        # Find the email and password input fields and enter the credentials
        email = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)  # Enter your twitter email
        password.send_keys(TWITTER_PASSWORD)  # Enter your twitter password
        time.sleep(2)  # Wait for the login to process
        password.send_keys(Keys.ENTER)  # Press ENTER to login
        time.sleep(5)  # Wait for twitter to load
        # Find the tweet box, compose the tweet, and send it
        tweet_compose = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)  # Enter the tweet
        time.sleep(3)  # Wait for the tweet to process
        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()  # Click the tweet button to post the tweet
        time.sleep(2)  # Wait for the tweet to post
        self.driver.quit()  # Close the browser

# Create an instance of the bot and run the functions
bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
