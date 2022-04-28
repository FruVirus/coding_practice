# pylint: disable=C0114, E1121, R0204

# Standard Library
import pprint

# Third Party Library
from mongoengine import Document, ListField, StringField, URLField, connect
from pymongo import MongoClient

# client = MongoClient(host="localhost", port=27017)
client = MongoClient("mongodb://localhost:27017")  # type: ignore
print(client)
print()
# db = client["rptutorials"]
db = client.rptutorials
print(db)
print()
tutorial1 = {
    "title": "Working With JSON Data in Python",
    "author": "Lucas",
    "contributors": ["Aldren", "Dan", "Joanna"],
    "url": "https://realpython.com/python-json/",
}
tutorial = db.tutorial
print(tutorial)
print()
result = tutorial.insert_one(tutorial1)
print(result)
print(f"One tutorial: {result.inserted_id}")
print()
tutorial2 = {
    "title": "Python's Requests Library (Guide)",
    "author": "Alex",
    "contributors": ["Aldren", "Brad", "Joanna"],
    "url": "https://realpython.com/python-requests/",
}
tutorial3 = {
    "title": "Object-Oriented Programming (OOP) in Python 3",
    "author": "David",
    "contributors": ["Aldren", "Joanna", "Jacob"],
    "url": "https://realpython.com/python3-object-oriented-programming/",
}
new_result = tutorial.insert_many([tutorial2, tutorial3])
print(new_result)
print(f"Multiple tutorials: {new_result.inserted_ids}")
print()
for doc in tutorial.find():
    pprint.pprint(doc)
print()
jon_tutorial = tutorial.find_one({"author": "Jon"})
pprint.pprint(jon_tutorial)
print()
client.close()

with MongoClient() as client:
    db = client.rptutorials
    for doc in db.tutorial.find():
        pprint.pprint(doc)
print()

connect(db="rptutorials", host="localhost", port=27017)


class Tutorial(Document):
    title = StringField(required=True, max_length=70)
    author = StringField(required=True, max_length=20)
    contributors = ListField(StringField(max_length=20))
    url = URLField(required=True)


tutorial1 = Tutorial(
    title="Beautiful Soup: Build a Web Scraper With Python",
    author="Martin",
    contributors=["Aldren", "Geir Arne", "Jaya", "Joanna", "Mike"],
    url="https://realpython.com/beautiful-soup-web-scraper-python/",
)
tutorial1.save()
for doc in Tutorial.objects:
    print(doc.title)
print()
for doc in Tutorial.objects(author="Alex"):
    print(doc.title)
