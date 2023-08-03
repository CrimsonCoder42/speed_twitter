from internet_speed_twitter_bot import InternetSpeedTwitterBot
from dotenv import load_dotenv
import os

load_dotenv()

#Twitter info from .env file
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")

#URLs
SPEED_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/"

# Create the bot
speed_bot = InternetSpeedTwitterBot()

# Open the speed test page and perform the speed test
speed_bot.driver.get(SPEED_URL)

speed_bot.get_internet_speed()

# Keep trying until we get the speed


speed_bot.driver.quit()


