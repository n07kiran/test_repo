import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import pyautogui
import time
import re
import locators, details


class Packt:

    def __init__(self, course_link):
        self.chrome = webdriver.Chrome(executable_path="D:/Programming/Python/chrome_driver/chromedriver.exe")
        self.course = course_link

    def login(self):

        try:

            username = details.LOGIN.USERNAME
            password = details.LOGIN.PASSWORD

            self.chrome.get("https://subscription.packtpub.com/login")
            self.chrome.maximize_window()

            username_ele = self.chrome.find_element(By.CSS_SELECTOR, locators.LOGIN.USERNAME_LOCATOR)
            password_ele = self.chrome.find_element(By.CSS_SELECTOR, locators.LOGIN.PASSWORD_LOCATOR)
            submit_ele = self.chrome.find_element(By.CSS_SELECTOR, locators.LOGIN.SIGNIN_LOCATOR)

            # print(username, password)
            username_ele.send_keys(username)
            password_ele.send_keys(password)
            submit_ele.click()
            time.sleep(2)

        except Exception as e:
            print("Error while logging in to Page")
            print(e)
            self.logout()

    def get_pages_link_section_wise(self):

        try:
            time.sleep(10)
            self.chrome.get(self.course)
            WebDriverWait(self.chrome, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, locators.SECTION.LOCATOR)))
            all_sections = self.chrome.find_elements(By.CSS_SELECTOR, locators.SECTION.LOCATOR)
            all_sections_with_pages = [sec.find_elements(By.CSS_SELECTOR, locators.WEBPAGE.LOCATOR) for sec in
                                       all_sections]

            pages_sec_sections = [[page.get_attribute("href") for page in sec] for sec in all_sections_with_pages]

            return pages_sec_sections

        except Exception as e:
            print("Error while getting page links")
            print(e)
            self.logout()

    def name(self, page_link):

        try:
            match = re.search(
                '^https://subscription\.packtpub\.com/video/[a-z]*/[0-9]*/\w*/video([0-9]*)_([0-9]*)/([\w-]*)$',
                page_link,
                re.I)

            if match:
                sec = match.group(1)
                no = match.group(2)
                title = match.group(3).replace('-', ' ')

                name = f"{sec}.{no} {title}"

                print(name)
                return name

        except Exception as e:
            print("Error while getting name from link")
            print(e)
            self.logout()
            return None

    def download(self, page_link):


        self.chrome.maximize_window()

        i = 0
        while i < 5:
            try:
                self.chrome.get(page_link)

                WebDriverWait(self.chrome, 30).until(
                    EC.element_attribute_to_include((By.CSS_SELECTOR, locators.VIDEO.VIDEO), 'src'))
                video = self.chrome.find_element(By.CSS_SELECTOR, locators.VIDEO.VIDEO)
                video_src = video.get_attribute('src')
                self.chrome.get(video_src)
                break

            except Exception as e:
                i += 1
                print("Error while getting video source link from page")
                print(e)
                print("Retrying")

                if i > 4:
                    print("Enough of retries")
                    self.logout()

        try:
            pyautogui.press('enter')
            time.sleep(5)
            pyautogui.moveTo(1000, 600)

            with pyautogui.hold('ctrl'):
                pyautogui.press('s')

            title = self.name(page_link)
            time.sleep(2)

            if title:
                pyautogui.write(title)

            time.sleep(5)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.press('left')
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.press('esc')

        except Exception as e:
            print('Error while saving video file from page')
            print(e)
            self.logout()

    def logout(self):
        print("Logging out")
        time.sleep(10)
        self.chrome.get("https://subscription.packtpub.com/logout")
        time.sleep(2)
        self.chrome.close()
        sys.exit()
