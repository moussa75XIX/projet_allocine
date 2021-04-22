# -*- coding: utf-8 -*- #


import os
import glob
import json
import time


PATH_PRODUCTS = os.path.join(os.curdir, 'products')
PATH_MERGED_PRODUCTS = os.path.join(os.curdir, 'merged_products')
PATH_REVIEWS = os.path.join(os.curdir, 'reviews')
PATH_MERGED_REVIEWS = os.path.join(os.curdir, 'merged_reviews')

def aggregate_products():
    """
    Aggregates the product's files collected.
    """

    products_files = []

    # For each json file, open the content of the file
    for products_file in glob.glob(os.path.join(PATH_PRODUCTS, '*.json')):
        open_product_file = json.load(open(products_file, 'r'))
        products_files.append(open_product_file)

    with open(os.path.join(PATH_MERGED_PRODUCTS, str(time.strftime("%Y_%m_%d")) + '_aggregated_products.json'), 'w', encoding='utf-8') as file_to_dump:
        json.dump(products_files, file_to_dump, indent=4, ensure_ascii=False)


def aggregate_reviews():
    """
    Aggregates the reviews' files collected.
    """

    reviews_files = []

    # For each json file, open the content of the file
    for reviews_file in glob.glob(os.path.join(PATH_REVIEWS, '*.json')):
        open_reviews_file = json.load(open(reviews_file, 'r', encoding="utf8"))
        for review_file in open_reviews_file:
            reviews_files.append(review_file)

    with open(os.path.join(PATH_MERGED_REVIEWS, str(time.strftime("%Y_%m_%d")) + '_aggregated_reviews.json'), 'w', encoding='utf-8') as file_to_dump:
        json.dump(reviews_files, file_to_dump, indent=4, ensure_ascii=False)


def main():
    aggregate_reviews()
    aggregate_products()


if __name__ == "__main__":
    main()