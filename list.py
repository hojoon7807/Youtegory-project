from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.youtegory

db.categoryId.insert_one({"id": 1,"name":"Film & Animation"})
db.categoryId.insert_one({"id": 2,"name":"Cars & Vehicles"})
db.categoryId.insert_one({"id": 10,"name":"Music"})
db.categoryId.insert_one({"id": 15,"name":"Pets & Animals"})
db.categoryId.insert_one({"id": 17,"name":"Sports"})
db.categoryId.insert_one({"id": 19,"name":"Travel & Events"})
db.categoryId.insert_one({"id": 20,"name":"Gaming"})
db.categoryId.insert_one({"id": 22,"name":"People & Blogs"})
db.categoryId.insert_one({"id": 23,"name":"Comedy"})
db.categoryId.insert_one({"id": 24,"name":"Entertainment"})
db.categoryId.insert_one({"id": 25,"name":"News & Politics"})
db.categoryId.insert_one({"id": 26,"name":"Howto & Style"})
db.categoryId.insert_one({"id": 27,"name":"Education"})
db.categoryId.insert_one({"id": 28,"name":"Science & Technology"})
db.categoryId.insert_one({"id": 29,"name":"Nonprofits & Activism"})

name={1:"Film & Animation", 2:"Cars & Vehicles", 10:"Music", 15:"Pets & Animals", 17:"Sports",
19:"Travel & Events", 20:"Gaming", 22:"People & Blogs", 23:"Comedy", 24:"Entertainmetn", 25:"News & Politics",
26:"Howto & Style", 27:"Education", 28:"Science & Technology", 29:"Nonprofits & Activism" }
