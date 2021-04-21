# -*- coding: utf-8 -*- #

import json
import os
import time
import random

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from products_collector import collect_product_data

PATH_PRODUCT = os.path.join(os.curdir, 'product')
PATH_DRIVER = r'C:\Users\mouss\OneDrive\Documents\VOYSEN\chromedriver.exe'

CHROME_OPTIONS = Options()
CHROME_OPTIONS.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36')
CHROME_OPTIONS.add_argument("--no-sandbox")
CHROME_OPTIONS.add_argument("--window-size=1280,720")
CHROME_OPTIONS.add_argument("--headless")

COLLECT_DATE = '2021_04_20'


def main():

    # Select the url
    url = "https://www.allocine.fr/series/ficheserie_gen_cserie=23120.html"
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

    # Collect data
    product_data = collect_product_data(driver, url)

    print(product_data)

    with open(os.path.join(PATH_PRODUCT,COLLECT_DATE + '_data_product_' + str(time.strftime("%Y_%m_%d_%H_%M_%S")) + '.json'), 'w',encoding='utf-8') as file_to_dump:
        json.dump(product_data, file_to_dump, indent=2, ensure_ascii=False)

    # Delete the cookies and quit the driver
    driver.delete_all_cookies()
    driver.quit()


if __name__ == "__main__":
    main()