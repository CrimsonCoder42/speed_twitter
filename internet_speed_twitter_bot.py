from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0
        self.actions = {
            "find_click_xpath": lambda x: self.driver.find_element(By.XPATH, x).click(),
            "find_write_xpath": lambda x, text: self.driver.find_element(By.XPATH, x).send_keys(text),
            "find_text_xpath": lambda x: self.driver.find_element(By.XPATH, x).text
        }

    def handle_exceptions(self, action, *args):
        try:
            result = self.actions[action](*args)
            return result if result is not None else True
        except Exception as e:
            print(f"Exception: {e}")
            return False

    def get_internet_speed(self):
        go_button_xpath = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a'
        speed_xpaths = {
            'Download Speed': '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span',
            'Upload Speed': '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'
        }

        if self.handle_exceptions("find_click_xpath", go_button_xpath):
            print("Clicked go button")
            download_speed = self.handle_exceptions("find_text_xpath", speed_xpaths['Download Speed'])
            upload_speed = self.handle_exceptions("find_text_xpath", speed_xpaths['Upload Speed'])

            while True:
                time.settimeout(5)

                # download_speed >= 0.0 and upload_speed >= 0.0:
                # try:
                #     download_speed = float(download_speed)
                #     upload_speed = float(upload_speed)
                #     print(f"Download Speed: {download_speed}")
                #     print(f"Upload Speed: {upload_speed}")
                #     return True
                # except Exception as e:
                #     print(f"Exception: {e}")
                #     return False

        #     for speed_type, xpath in speed_xpaths.items():
        #         speed_text = self.handle_exceptions("find_text_xpath", xpath)
        #         speed = float(speed_text) if speed_text.strip() else None
        #         if speed is not None:
        #             print(f"{speed_type}: {speed}")
        #             return True
        # return False

    def tweet_at_provider(self):
        print("Tweeting at provider...")
