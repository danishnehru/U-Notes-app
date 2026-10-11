from pymongo import MongoClient


mongo_uri ="mongodb+srv://<username>:<password>@<cluster-url>/<database>?retryWrites=true&w=majority"  # Replace with your MongoDB URI

conn = MongoClient(mongo_uri)