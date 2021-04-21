# -*- coding: utf-8 -*- #


import os
import json
import time


PATH_SERIES_AGGREGATED = os.path.join(os.curdir, 'urls_series_aggregated')
PATH_URLS_PRODUCTS_TO_COLLECT = os.path.join(os.curdir, 'urls_products_to_collect')
PATH_URLS_REVIEWS_TO_COLLECT = os.path.join(os.curdir, 'urls_reviews_to_collect')

COLLECT_DATE = '2021_04_20'


def filter_products_urls(urls):
    """
    Filters the products urls to collect.

    # Args
        new_urls: list, list of new products urls dictionaries

    # Returns
        products_urls_to_collect: list, products urls to collect
    """

    # Extract the products urls from the dictionaries
    products_urls = [url['serie_url'] for url in urls]

    # Apply the collected key
    products_urls_to_collect = [{'url': product_url, 'collected': 'no'} for product_url in products_urls]

    return products_urls_to_collect


def filter_reviews_urls(urls):
    """
    Filters the reviews urls to collect.

    # Args:
        new_urls_dicts: list, list of new products urls dictionaries

    # Returns:
        reviews_urls_to_collect_json: list, reviews urls to collect
    """

    # Extract the products urls from the dictionaries
    reviews_urls = [url['series_reviews_page'] for url in urls]

    # Apply the collected key
    reviews_urls_to_collect = [{'url': review_url, 'collected': 'no'} for review_url in reviews_urls]

    return reviews_urls_to_collect


def main():

    # Load the new aggregated urls
    with open(os.path.join(PATH_SERIES_AGGREGATED, str(COLLECT_DATE) + '_aggregated_series_urls_list.json')) as file_to_open:
        urls = json.load(file_to_open)

    # Products urls
    # Filter the urls
    products_urls_to_collect = filter_products_urls(urls)

    # Save products urls
    with open(os.path.join(PATH_URLS_PRODUCTS_TO_COLLECT, str(time.strftime("%Y_%m_%d")) + '_products_urls_to_collect.json'), 'w', encoding='utf-8') as file_to_dump:
        json.dump(products_urls_to_collect, file_to_dump, indent=4, ensure_ascii=False)

    # Reviews urls
    # Filter the urls
    reviews_urls_to_collect = filter_reviews_urls(urls)

    # Save reviews urls
    with open(os.path.join(PATH_URLS_REVIEWS_TO_COLLECT, str(time.strftime("%Y_%m_%d")) + '_reviews_urls_to_collect.json'), 'w', encoding='utf-8') as file_to_dump:
        json.dump(reviews_urls_to_collect, file_to_dump, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()
