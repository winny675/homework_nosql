# import library pymongo
import pymongo

# membuat koneksi ke MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# membuat database dan collection
db = client["bookstore"]
book_collection = db["books"]

# insert one
book = {
  "title": "Sapiens: A Brief History of Humankind",
  "author": "Yuval Noah Harari",
  "tags": ["non-fiction", "history", "anthropology"],
  "price": 150000,
  "stock": 3
}
result = book_collection.insert_one(book)
print(result.inserted_id)

# bulk insert
books = [
  {
    "title": "The Da Vinci Code",
    "author": "Dan Brown",
    "tags": ["fiction", "thriller", "mystery"],
    "price": 125000,
    "stock": 10
  },
  {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "tags": ["fiction", "dystopian", "young adult"],
    "price": 110000,
    "stock": 5
  },
  {
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "tags": ["fiction", "inspirational"],
    "price": 95000,
    "stock": 2
  }
]
result = book_collection.insert_many(books)
print(result.inserted_ids)

# query buku dengan stock < 5 dan harga > 10000
query = { "stock": { "$lt": 5 }, "price": { "$gt": 10000 } }
books = book_collection.find(query)
for book in books:
  print(book)

# update one
query = { "title": "Sapiens: A Brief History of Humankind" }
new_values = { "$set": { "price": 175000 } }
result = book_collection.update_one(query, new_values)
print(result.modified_count)

# update many
query = { "stock": { "$lt": 5 } }
new_values = { "$set": { "price": 120000 } }
result = book_collection.update_many(query, new_values)
print(result.modified_count)

# delete one
query = { "title": "The Alchemist" }
result = book_collection.delete_one(query)
print(result.deleted_count)

# delete many
query = { "stock": { "$lt": 5 } }
result = book_collection.delete_many(query)
print(result.deleted_count)
