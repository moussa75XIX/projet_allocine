# -*- coding: utf-8 -*- #

import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def init_review_dict():
    """
    Initializes the dictionary with the review data.
    # Returns:
        review_dict: dict, dictionary with the review data.
    """

    review_dict = {
        'id_review_product': None,
        'url': None,
        'serie_url': None,
        'review_text': None,
        'review_date': None,
        'writer_pseudo': None,
        'review_rating': None,
        'collect_date': str(time.strftime("%Y_%m_%d")),
    }

    return review_dict


def collect_reviews_data(driver, url):
    """
    Collects the reviews data for the current page.
    # Args:
       driver: selenium driver
       url: str, url of a product.
       product_dict: dict, product's information

    # Return:
       product_dict: dict, dictionary with product's data.
    """

    reviews_dicts = []

    reviews = driver.find_elements_by_class_name("review-card")

    for id_review, review in enumerate(reviews):
        # Initialize the dictionary to save the data for the current review.
        review_dict = init_review_dict()

        # Review's ID
        try:
            review_dict['id_review_product'] = id_review + 1
        except:
            pass

        # Review's url
        try:
            review_dict['url'] = url
        except:
            pass

        # Serie's url
        try:
            links = driver.find_elements_by_xpath('//*[@id="content-layout"]/div/a')
            review_dict['serie_url'] = links[-1].get_attribute('href')
            if review_dict['serie_url'] == review_dict['url']:
                review_dict['serie_url'] = links[-2].get_attribute('href')
        except:
            pass

        # Review's rating
        try:
            review_dict['review_rating'] = review.find_element_by_class_name("stareval-note").get_attribute("textContent")
        except:
            pass

        # Review's date
        try:
            review_dict['review_date'] = review.find_element_by_class_name("review-card-meta-date").get_attribute("textContent").strip().replace('\n','').replace('Publiée le ','')
        except:
            pass

        # Review's text
        try:
            review_dict['review_text'] = review.find_element_by_class_name("review-card-content").get_attribute("textContent").strip().replace('\n','').replace('\"',"'")
        except:
            pass

        # Writer's pseudo
        try:
            review_dict['writer_pseudo'] = review.find_element_by_class_name("review-card-user-infos").find_element_by_tag_name("div").find_element_by_tag_name("a").get_attribute('textContent')
        except:

            pass

        reviews_dicts.append(review_dict)

    # Show other sections that contain reviews and collect them
    try:
        while driver.find_element_by_class_name("button-right").get_attribute('href') is not None:
            more_reviews_btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'button-right')))
            driver.execute_script("arguments[0].scrollIntoView(true);", more_reviews_btn)
            driver.execute_script("arguments[0].click();", more_reviews_btn)
            reviews_dicts += collect_reviews_data(driver, url)
    except:
        pass

    return reviews_dicts