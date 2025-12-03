# NoSQL Project

## Resources

**Read or watch:**
- [NoSQL Databases Explained](https://www.mongodb.com/nosql-explained)
- [What is NoSQL?](https://www.youtube.com/watch?v=qUV2j3XBRHc)
- [MongoDB with Python Crash Course - Tutorial for Beginners](https://www.youtube.com/watch?v=E-1xI85Zog8)
- [MongoDB Tutorial 2: Insert, Update, Remove, Query](https://www.youtube.com/watch?v=CB9G5Dvv-EE)
- [Aggregation](https://www.mongodb.com/docs/manual/aggregation/)
- [Introduction to MongoDB and Python](https://realpython.com/introduction-to-mongodb-and-python/)
- [mongo Shell Methods](https://www.mongodb.com/docs/v4.4/reference/method/)
- [The mongo Shell](https://www.mongodb.com/docs/v4.4/mongo/)

## Learning Objectives

At the end of this project, you should be able to explain:

### General
- What NoSQL means
- What is the difference between SQL and NoSQL
- What is ACID
- What is document storage
- What are NoSQL types
- What are benefits of a NoSQL database
- How to query information from a NoSQL database
- How to insert/update/delete information from a NoSQL database
- How to use MongoDB

## Requirements

### MongoDB Command File
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using MongoDB (version 4.4)
- All your files should end with a new line
- The first line of all your files should be a comment: `// my comment`
- A `README.md` file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using `wc`

### Python Scripts
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9) and PyMongo (version 4.8.0)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5.*)
- The length of your files will be tested using `wc`
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- Your code should not be executed when imported (by using `if __name__ == "__main__":`)

## Setup

### Install MongoDB 4.4 on macOS
```bash
# Install MongoDB 4.4
brew tap mongodb/brew
brew install mongodb-community@4.4

# Add to PATH (add to ~/.zshrc for persistence)
export PATH="/opt/homebrew/opt/mongodb-community@4.4/bin:$PATH"

# Start MongoDB
brew services start mongodb/brew/mongodb-community@4.4

# Verify installation
mongod --version
```

### Install PyMongo
```bash
pip3 install pymongo==4.8.0 --break-system-packages
```

## Tasks

### 0. List all databases
Write a script that lists all databases in MongoDB.

**File:** `0-list_databases`

### 1. Create a database
Write a script that creates or uses the database `my_db`.

**File:** `1-use_or_create_database`

### 2. Insert document
Write a script that inserts a document in the collection `school`:
- The document must have one attribute `name` with value "Holberton school"
- The database name will be passed as option of `mongo` command

**File:** `2-insert`

### 3. All documents
Write a script that lists all documents in the collection `school`:
- The database name will be passed as option of `mongo` command

**File:** `3-all`

### 4. All matches
Write a script that lists all documents with `name="Holberton school"` in the collection `school`:
- The database name will be passed as option of `mongo` command

**File:** `4-match`

### 5. Count
Write a script that displays the number of documents in the collection `school`:
- The database name will be passed as option of `mongo` command

**File:** `5-count`

### 6. Update
Write a script that adds a new attribute to documents in the collection `school`:
- The script should update only documents with `name="Holberton school"` (all of them)
- The update should add the attribute `address` with the value "972 Mission street"
- The database name will be passed as option of `mongo` command

**File:** `6-update`

### 7. Delete by match
Write a script that deletes all documents with `name="Holberton school"` in the collection `school`:
- The database name will be passed as option of `mongo` command

**File:** `7-delete`

### 8. List all documents in Python
Write a Python function that lists all documents in a collection:
- Prototype: `def list_all(mongo_collection):`
- Return an empty list if no document in the collection
- `mongo_collection` will be the pymongo collection object

**File:** `8-all.py`

### 9. Insert a document in Python
Write a Python function that inserts a new document in a collection based on kwargs:
- Prototype: `def insert_school(mongo_collection, **kwargs):`
- `mongo_collection` will be the pymongo collection object
- Returns the new `_id`

**File:** `9-insert_school.py`

### 10. Change school topics
Write a Python function that changes all topics of a school document based on the name:
- Prototype: `def update_topics(mongo_collection, name, topics):`
- `mongo_collection` will be the pymongo collection object
- `name` (string) will be the school name to update
- `topics` (list of strings) will be the list of topics approached in the school

**File:** `10-update_topics.py`

### 11. Where can I learn Python?
Write a Python function that returns the list of schools having a specific topic:
- Prototype: `def schools_by_topic(mongo_collection, topic):`
- `mongo_collection` will be the pymongo collection object
- `topic` (string) will be topic searched

**File:** `11-schools_by_topic.py`

### 12. Log stats
Write a Python script that provides some stats about Nginx logs stored in MongoDB:
- Database: `logs`
- Collection: `nginx`
- Display:
  - First line: `x logs` where `x` is the number of documents in this collection
  - Second line: `Methods:`
  - 5 lines with the number of documents with the method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
  - One line with the number of documents with: method=GET, path=/status

**File:** `12-log_stats.py`

## Usage Examples

### MongoDB Shell
```bash
# Run a MongoDB script
mongo my_database < 0-list_databases

# Or with cat
cat 0-list_databases | mongo
```

### Python Scripts
```bash
# Make executable
chmod +x 8-all.py

# Run
./8-all.py
```

## Author
Holberton School - NoSQL Project

