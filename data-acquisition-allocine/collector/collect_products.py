# -*- coding: utf-8 -*- #
import os
import time
import json
import random

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from products_collector import collect_product_data

PATH_PRODUCTS = os.path.join(os.curdir, 'products')
PATH_URLS_PRODUCTS_TO_COLLECT = os.path.join(os.curdir, 'urls_products_to_collect')
PATH_DRIVER = r'C:\Users\mouss\OneDrive\Documents\VOYSEN\chromedriver.exe'

CHROME_OPTIONS = Options()
CHROME_OPTIONS.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36')
CHROME_OPTIONS.add_argument("--no-sandbox")
CHROME_OPTIONS.add_argument("--window-size=1280,720")
CHROME_OPTIONS.add_argument("--headless")

COLLECT_DATE = '2021_04_20'


def main():
    urls_dicts = json.load(open(os.path.join(PATH_URLS_PRODUCTS_TO_COLLECT, COLLECT_DATE + '_products_urls_to_collect.json'), 'r'))

    for url_dict in urls_dicts:

        # Select the url under specific conditions
        if url_dict['collected'] == 'no':

            # Load the driver for every new page
            driver = webdriver.Chrome(PATH_DRIVER, options=CHROME_OPTIONS)

            print('[LOG] Current url:', url_dict['url'])
            print('[LOG] Datetime:', time.strftime("%Y_%m_%d_%H_%M_%S"))

            try:
                # Load the url with the driver
                driver.get(url_dict['url'])

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

                # Collect and save the product data
                product_data = collect_product_data(driver, url_dict['url'])

                with open(os.path.join(PATH_PRODUCTS, COLLECT_DATE + '_data_product_' + str(time.strftime("%Y_%m_%d_%H_%M_%S")) + '.json'), 'w') as file_to_dump:
                    json.dump(product_data, file_to_dump, indent=2, ensure_ascii=False)

                # Change the status of the current url and save it.
                # The current url has a title.
                if product_data["original_title"]:

                    with open(os.path.join(PATH_PRODUCTS, COLLECT_DATE + '_data_product_' + str(time.strftime("%Y_%m_%d_%H_%M_%S")) + '.json'), 'w') as file_to_dump:
                        json.dump(product_data, file_to_dump, indent=2, ensure_ascii=False)

                    # The url is set as 'yes'.
                    url_dict['collected'] = 'yes'
                    print("[LOG] All the product's data have been collected for the current url")

                    with open(os.path.join(PATH_URLS_PRODUCTS_TO_COLLECT, COLLECT_DATE + '_products_urls_to_collect.json'),'w') as file_to_dump:
                        json.dump(urls_dicts, file_to_dump, indent=2, ensure_ascii=False)

                else:
                    # If the page data didn't load
                    # The collect for the current url has raised some errors.
                    # The url is set as 'issue'.
                    url_dict['collected'] = 'issue'
                    print('[LOG] Issue with the current url. Saved as url with issues.')

                    with open(os.path.join(PATH_URLS_PRODUCTS_TO_COLLECT, COLLECT_DATE + '_products_urls_to_collect.json'),'w') as file_to_dump:
                        json.dump(urls_dicts, file_to_dump, indent=2, ensure_ascii=False)

            except:
                # The collect for the current url has raised some errors.
                # The url is set as 'issue'.
                url_dict['collected'] = 'issue'
                print('[LOG] Issue with the current url. Saved as url with issues.')

                with open(os.path.join(PATH_URLS_PRODUCTS_TO_COLLECT, COLLECT_DATE + '_products_urls_to_collect.json'),'w') as file_to_dump:
                    json.dump(urls_dicts, file_to_dump, indent=2, ensure_ascii=False)

            # Delete the cookies and quit the driver
            driver.delete_all_cookies()
            driver.quit()


if __name__ == "__main__":
    main()