# NoSQL Project - Tasks Overview

## 📋 All Tasks Summary

### ✅ Task 0: List all databases
**File:** `0-list_databases`  
**Type:** MongoDB Shell Script  
**Description:** Lists all databases in MongoDB  
**Command:** `mongo < 0-list_databases`

---

### ✅ Task 1: Create a database
**File:** `1-use_or_create_database`  
**Type:** MongoDB Shell Script  
**Description:** Creates or uses the database `my_db`  
**Command:** `cat 1-use_or_create_database | mongo`

---

### ✅ Task 2: Insert document
**File:** `2-insert`  
**Type:** MongoDB Shell Script  
**Description:** Inserts a document with name "Holberton school" in collection `school`  
**Command:** `cat 2-insert | mongo my_db`

**Example Output:**
```
WriteResult({ "nInserted" : 1 })
```

---

### ✅ Task 3: All documents
**File:** `3-all`  
**Type:** MongoDB Shell Script  
**Description:** Lists all documents in the collection `school`  
**Command:** `cat 3-all | mongo my_db`

**Example Output:**
```
{ "_id" : ObjectId("..."), "name" : "Holberton school" }
```

---

### ✅ Task 4: All matches
**File:** `4-match`  
**Type:** MongoDB Shell Script  
**Description:** Lists all documents with name="Holberton school"  
**Command:** `cat 4-match | mongo my_db`

---

### ✅ Task 5: Count
**File:** `5-count`  
**Type:** MongoDB Shell Script  
**Description:** Displays the number of documents in collection `school`  
**Command:** `cat 5-count | mongo my_db`

**Example Output:**
```
1
```

---

### ✅ Task 6: Update
**File:** `6-update`  
**Type:** MongoDB Shell Script  
**Description:** Adds attribute `address` with value "972 Mission street" to all documents with name="Holberton school"  
**Command:** `cat 6-update | mongo my_db`

**Example Output:**
```
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
```

---

### ✅ Task 7: Delete by match
**File:** `7-delete`  
**Type:** MongoDB Shell Script  
**Description:** Deletes all documents with name="Holberton school"  
**Command:** `cat 7-delete | mongo my_db`

**Example Output:**
```
{ "acknowledged" : true, "deletedCount" : 1 }
```

---

### ✅ Task 8: List all documents in Python
**File:** `8-all.py`  
**Type:** Python Script  
**Description:** Function that lists all documents in a collection  
**Prototype:** `def list_all(mongo_collection):`  
**Test:** `./8-main.py`

**Example Code:**
```python
def list_all(mongo_collection):
    """Lists all documents in a collection"""
    documents = []
    for doc in mongo_collection.find():
        documents.append(doc)
    return documents
```

**Example Output:**
```
[6930026ff83275a1cd40c74b] Holberton school
```

---

### ✅ Task 9: Insert a document in Python
**File:** `9-insert_school.py`  
**Type:** Python Script  
**Description:** Function that inserts a new document based on kwargs  
**Prototype:** `def insert_school(mongo_collection, **kwargs):`  
**Test:** `./9-main.py`

**Example Code:**
```python
def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
```

**Example Output:**
```
New school created: 693002c326532d5d95e306d1
[6930026ff83275a1cd40c74b] Holberton school 
[693002c326532d5d95e306d1] UCSF 505 Parnassus Ave
```

---

### ✅ Task 10: Change school topics
**File:** `10-update_topics.py`  
**Type:** Python Script  
**Description:** Function that changes all topics of a school document  
**Prototype:** `def update_topics(mongo_collection, name, topics):`  
**Test:** `./10-main.py`

**Example Code:**
```python
def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school document"""
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )
```

**Example Output:**
```
[6930026ff83275a1cd40c74b] Holberton school ['Sys admin', 'AI', 'Algorithm']
```

---

### ✅ Task 11: Where can I learn Python?
**File:** `11-schools_by_topic.py`  
**Type:** Python Script  
**Description:** Function that returns schools having a specific topic  
**Prototype:** `def schools_by_topic(mongo_collection, topic):`  
**Test:** `./11-main.py`

**Example Code:**
```python
def schools_by_topic(mongo_collection, topic):
    """Returns list of schools having a specific topic"""
    return list(mongo_collection.find({ "topics": topic }))
```

**Example Output:**
```
[69300312e3693ceb3d58de19] Holberton school ['Algo', 'C', 'Python', 'React']
[69300312e3693ceb3d58de1b] UCLA ['C', 'Python']
```

---

### ✅ Task 12: Log stats
**File:** `12-log_stats.py`  
**Type:** Python Script  
**Description:** Script that provides stats about Nginx logs  
**Database:** `logs`  
**Collection:** `nginx`  
**Test:** `./populate_nginx_logs.py` then `./12-log_stats.py`

**Example Code:**
```python
def log_stats():
    """Provides stats about Nginx logs"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")
    
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    
    status_check = nginx_collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_check} status check")
```

**Example Output:**
```
14 logs
Methods:
	method GET: 7
	method POST: 3
	method PUT: 2
	method PATCH: 1
	method DELETE: 1
4 status check
```

---

## 🧪 Testing Workflow

### Step-by-Step Testing

1. **List databases**
   ```bash
   mongo < 0-list_databases
   ```

2. **Create database and insert data**
   ```bash
   cat 2-insert | mongo my_db
   ```

3. **Verify insertion**
   ```bash
   cat 3-all | mongo my_db
   ```

4. **Count documents**
   ```bash
   cat 5-count | mongo my_db
   ```

5. **Update documents**
   ```bash
   cat 6-update | mongo my_db
   cat 3-all | mongo my_db  # Verify update
   ```

6. **Test Python scripts**
   ```bash
   ./8-main.py   # List all
   ./9-main.py   # Insert
   ./10-main.py  # Update topics
   ./11-main.py  # Find by topic
   ```

7. **Test log stats**
   ```bash
   ./populate_nginx_logs.py
   ./12-log_stats.py
   ```

---

## 📊 Project Statistics

- **Total Tasks:** 13 (0-12)
- **MongoDB Shell Scripts:** 8 files
- **Python Scripts:** 5 files
- **Test Files:** 4 files
- **Documentation Files:** 4 files (README.md, QUICK_START.md, PROJECT_SUMMARY.md, this file)

---

## 🎯 Skills Demonstrated

### MongoDB Shell
- ✅ Database creation and selection
- ✅ Document insertion (insert, insertOne, insertMany)
- ✅ Document querying (find, findOne)
- ✅ Document counting (count, count_documents)
- ✅ Document updating (update, updateMany)
- ✅ Document deletion (deleteOne, deleteMany)
- ✅ Query filtering

### PyMongo (Python)
- ✅ MongoDB connection
- ✅ Collection operations
- ✅ CRUD operations
- ✅ Query operators
- ✅ Aggregation basics
- ✅ Error handling

### Python Best Practices
- ✅ Module documentation
- ✅ Function documentation
- ✅ PEP 8 style (pycodestyle)
- ✅ Proper imports
- ✅ Shebang line
- ✅ Main guard (`if __name__ == "__main__":`)

---

## 🔍 Key Concepts Covered

### NoSQL Fundamentals
1. **NoSQL Definition** - Not Only SQL, non-relational databases
2. **SQL vs NoSQL** - Schema flexibility, scalability, data models
3. **ACID Properties** - Atomicity, Consistency, Isolation, Durability
4. **Document Storage** - JSON-like documents in MongoDB
5. **NoSQL Types** - Document, Key-Value, Column, Graph
6. **Benefits** - Flexibility, horizontal scaling, performance

### MongoDB Specifics
1. **Hierarchy** - Database → Collection → Document → Field
2. **BSON** - Binary JSON format used internally
3. **ObjectId** - Unique identifier for documents
4. **Query Operators** - $gt, $lt, $in, $set, etc.
5. **Update Operators** - $set, $unset, $inc, $push, etc.
6. **Aggregation** - Pipeline for complex queries

---

## 📚 Additional Features

### Helper Scripts
- **populate_nginx_logs.py** - Creates sample nginx logs for testing task 12

### Documentation
- **README.md** - Project requirements and task descriptions
- **QUICK_START.md** - Comprehensive NoSQL and MongoDB guide
- **PROJECT_SUMMARY.md** - Setup verification and quick reference
- **TASKS_OVERVIEW.md** - This file - detailed task breakdown

---

## 🚀 Quick Commands Reference

```bash
# MongoDB Shell
mongo                          # Start MongoDB shell
show dbs                       # List databases
use my_db                      # Use database
show collections               # List collections
db.collection.find()           # Find all documents
db.collection.count()          # Count documents

# Run Scripts
mongo < script.js              # Execute script
cat script.js | mongo db_name  # Execute with database

# Python
./script.py                    # Run Python script
python3 -m py_compile file.py  # Check syntax
python3 -c 'print(__import__("module").__doc__)'  # Check docs

# MongoDB Service
brew services start mongodb/brew/mongodb-community@4.4   # Start
brew services stop mongodb/brew/mongodb-community@4.4    # Stop
brew services restart mongodb/brew/mongodb-community@4.4 # Restart
```

---

## ✨ Project Status: COMPLETE

All 13 tasks have been implemented, tested, and documented. Your NoSQL project is ready for submission! 🎉

**Last Updated:** December 3, 2025  
**MongoDB Version:** 4.4.29  
**PyMongo Version:** 4.8.0  
**Python Version:** 3.14.0

