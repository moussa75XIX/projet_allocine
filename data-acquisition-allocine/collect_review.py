# -*- coding: utf-8 -*- #

import os
import json
import random
import time

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from reviews_collector import collect_reviews_data

PATH_REVIEW = os.path.join(os.curdir, 'review')
#PATH_DRIVER = r'C:\Users\mouss\OneDrive\Documents\VOYSEN\chromedriver.exe'
PATH_DRIVER = r'D:\Users\Tenma\Documents\chromedriver_win32\chromedriver.exe'
#PATH_DRIVER = r'D:\Ouss\projet_allocine-main\packages.exe'

CHROME_OPTIONS = Options()
CHROME_OPTIONS.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36')
CHROME_OPTIONS.add_argument("--no-sandbox")
CHROME_OPTIONS.add_argument("--window-size=1280,720")
CHROME_OPTIONS.add_argument("--headless")

COLLECT_DATE = '2021_04_20'


def main():
    url = "https://www.allocine.fr/series/ficheserie-23120/critiques/"
    # Load the driver
    driver = webdriver.Chrome(PATH_DRIVER, options=CHROME_OPTIONS)


    # Load the url with the driver
    driver.get(url)

    # Accept the cookies to navigate on the website
    try:
        cookie_btn = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//button[@onclick="Didomi.setUserAgreeToAll();" ]')))
        cookie_btn.click()
        time.sleep(random.uniform(0, 5))
    except:
        pass

    # Wait for the page to load correctly
    time.sleep(10)
    reviews_dicts = collect_reviews_data(driver, url)

    with open(os.path.join(PATH_REVIEW, str(time.strftime("%Y_%m_%d_%H_%M_%S")) + '_review.json'), 'w', encoding='utf-8') as file_to_dump:
        json.dump(reviews_dicts, file_to_dump, indent=4, ensure_ascii=False)

    # Delete the cookies and quit the driver
    driver.delete_all_cookies()
    driver.quit()

if __name__ == "__main__":
    main()
