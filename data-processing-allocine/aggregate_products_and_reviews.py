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
product_and_reviews = db.product_and_reviews

# Make the join between the product dictionary and the reviews dictionaries and we inject the result into the collection
product_and_reviews.insert_many(products.aggregate([
    {"$lookup": {"from": "reviews", "localField": "url", "foreignField": "serie_url", "as": "reviews"}}]))
