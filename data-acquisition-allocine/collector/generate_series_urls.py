# -*- coding: utf-8 -*-

import json
import time
import os
import random

import requests
from bs4 import BeautifulSoup

PATH_SERIES_COLLECTED = os.path.join(os.curdir, 'urls_series_collected')


def init_url_serie_dict():
    """
    Initializes the dictionary with the product data.

    Returns:
        url_serie_dict : dict, dictionary with the information of a serie.
    """

    url_serie_dict = {
        'serie_name': None,
        'serie_url': None,
        'series_reviews_page': None,
    }

    return url_serie_dict


def collect_series_urls(url):
    """
    Collects the name and the url of each serie on the page.

    # Args:
        url: str, url with list of series.

    # Returns:
        urls_series_list : list, list of url_serie_dict dictionaries
    """

    urls_series_list = []

    # Load the page
    response = requests.get(url)
    time.sleep(random.uniform(0, 3))

    print('[LOG] Response =', response)

    if response.ok:

        html_page = BeautifulSoup(response.text, 'html.parser')
        # Get the list of series urls.
        series = html_page.find_all('li', {'mdl'})
        try:
            # For each serie
            for serie in series:
                url_serie_dict = init_url_serie_dict()

                # Serie's name
                try:
                    url_serie_dict['serie_name'] = serie.find('h2',class_='meta-title').text.strip()
                except:
                    pass

                # Serie's url
                try:
                    url_serie_dict['serie_url'] = "https://www.allocine.fr" + serie.find('h2',class_='meta-title').a['href']
                except:
                    pass

                # Serie's reviews page
                try:
                    url_serie_dict['series_reviews_page'] = url_serie_dict['serie_url'].replace("_gen_cserie=","-").replace(".html","") + "/critiques/"
                except:
                    pass

                # Save the url if there are reviews on it
                if serie.find('div',class_='rating-item'):
                    # a modifier
                    urls_series_list.append(url_serie_dict)

        except:
            pass

    return urls_series_list


def main():

    url = "https://www.allocine.fr/series-tv/"

    # Load the page
    response = requests.get(url)
    time.sleep(random.uniform(0, 3))

    # For the first 10 pages we execute the method which collects the information
    for i in range(1, 10+1):
        current_page = url + "?page=" + str(i)

        print('[LOG] Current url =', current_page)

        try:
            dict_urls_product_reviews = collect_series_urls(current_page)
            # Save series list in a json file
            with open(os.path.join(PATH_SERIES_COLLECTED, str(time.strftime("%Y_%m_%d_%H_%*M_%S")) + '_urls_series_list.json'), 'w',encoding='utf-8') as file_to_dump:
                json.dump(dict_urls_product_reviews, file_to_dump, ensure_ascii=False, indent=4)
            print('[LOG] All the information of the current url have been saved.')

        except:
            print('[LOG] Issue with the current url. Information has not been saved')


if __name__ == "__main__":
    main()