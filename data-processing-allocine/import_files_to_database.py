import json
import os
from pymongo import MongoClient

# Import PATH
PATH_PRODUCTS = os.path.join(os.curdir, 'products')
PATH_REVIEWS = os.path.join(os.curdir, 'reviews')
PATH_URLS_AGGREGATED = os.path.join(os.curdir, 'urls_aggregated')

# Cluster connection
client = MongoClient(
    "mongodb://projet:allocine123@cluster0-shard-00-00.cxrwt.mongodb.net:27017,cluster0-shard-00-01.cxrwt.mongodb.net:27017,cluster0-shard-00-02.cxrwt.mongodb.net:27017/allocine?ssl=true&replicaSet=atlas-pkujiz-shard-0&authSource=admin&retryWrites=true&w=majority")

# Initialize the database
db = client["allocine"]

# Initialize the collections of the database
products = db.products
reviews = db.reviews
urls_aggregated = db.urls_aggregated

# Open the products file
with open(os.path.join(PATH_PRODUCTS, '2021_04_22_aggregated_products.json'), encoding='utf8') as file_to_open:
    PRODUCTS_FILE = json.load(file_to_open)

# Put it in the database
products.insert_many(PRODUCTS_FILE)

# Open the reviews file
with open(os.path.join(PATH_REVIEWS, '2021_04_22_aggregated_reviews.json'), encoding='utf8') as file_to_open:
    REVIEWS_FILE = json.load(file_to_open)

# Add the label key for each review
for review in REVIEWS_FILE:
    review['review_label'] = None

# Put it in the database
reviews.insert_many(REVIEWS_FILE)

# Open the urls aggregated file
with open(os.path.join(PATH_URLS_AGGREGATED, '2021_04_21_aggregated_series_urls_list.json'),
          encoding='utf8') as file_to_open:
    URLS_AGGREGATED_FILE = json.load(file_to_open)

# Put it in the database
urls_aggregated.insert_many(URLS_AGGREGATED_FILE)
