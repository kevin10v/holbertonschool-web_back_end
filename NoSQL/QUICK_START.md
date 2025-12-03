# NoSQL Quick Start Guide

## What is NoSQL?

**NoSQL** (Not Only SQL) databases are non-relational databases that provide flexible schemas and scale horizontally. They're designed for distributed data stores with very large data storage needs.

## SQL vs NoSQL

| Feature | SQL | NoSQL |
|---------|-----|-------|
| **Schema** | Fixed schema | Flexible/dynamic schema |
| **Scalability** | Vertical (scale-up) | Horizontal (scale-out) |
| **Data Model** | Tables with rows | Documents, key-value, graph, column |
| **ACID** | Strong ACID compliance | Eventual consistency (BASE) |
| **Examples** | MySQL, PostgreSQL | MongoDB, Cassandra, Redis |

## ACID Properties

**ACID** stands for:
- **Atomicity**: All operations in a transaction succeed or all fail
- **Consistency**: Database remains in consistent state before/after transaction
- **Isolation**: Concurrent transactions don't interfere with each other
- **Durability**: Committed transactions are permanently stored

NoSQL databases often follow **BASE** instead:
- **Basically Available**: System guarantees availability
- **Soft state**: State may change over time
- **Eventual consistency**: System will become consistent eventually

## NoSQL Types

1. **Document Stores** (MongoDB, CouchDB)
   - Store data as documents (JSON, BSON, XML)
   - Flexible schema
   - Good for content management, catalogs

2. **Key-Value Stores** (Redis, DynamoDB)
   - Simple key-value pairs
   - Very fast
   - Good for caching, sessions

3. **Column Stores** (Cassandra, HBase)
   - Store data in columns instead of rows
   - Good for analytics, data warehousing

4. **Graph Databases** (Neo4j, ArangoDB)
   - Store relationships between entities
   - Good for social networks, recommendations

## Document Storage (MongoDB)

MongoDB stores data in **documents** (similar to JSON objects):

```javascript
{
  "_id": ObjectId("507f1f77bcf86cd799439011"),
  "name": "John Doe",
  "age": 30,
  "email": "john@example.com",
  "address": {
    "street": "123 Main St",
    "city": "San Francisco"
  },
  "hobbies": ["reading", "coding", "hiking"]
}
```

### Benefits of Document Storage:
- **Flexible Schema**: Add/remove fields without migration
- **Nested Data**: Store complex objects naturally
- **Scalability**: Easy horizontal scaling
- **Performance**: Fast reads and writes
- **Developer Friendly**: JSON-like documents match application objects

## MongoDB Basics

### Hierarchy
- **Database**: Container for collections
- **Collection**: Group of documents (like a table)
- **Document**: Single record (like a row)
- **Field**: Key-value pair in document (like a column)

### Common Operations

#### Create/Read (CRUD)
```javascript
// Insert
db.collection.insert({ name: "Alice", age: 25 })
db.collection.insertOne({ name: "Bob" })
db.collection.insertMany([{ name: "Charlie" }, { name: "David" }])

// Find (Read)
db.collection.find()  // All documents
db.collection.find({ age: 25 })  // With filter
db.collection.findOne({ name: "Alice" })  // Single document

// Update
db.collection.update(
    { name: "Alice" },  // Filter
    { $set: { age: 26 } }  // Update
)
db.collection.updateMany({ age: { $lt: 30 } }, { $set: { young: true } })

// Delete
db.collection.deleteOne({ name: "Alice" })
db.collection.deleteMany({ age: { $lt: 18 } })
```

#### Query Operators
```javascript
// Comparison
{ age: { $gt: 25 } }  // Greater than
{ age: { $gte: 25 } }  // Greater than or equal
{ age: { $lt: 30 } }  // Less than
{ age: { $lte: 30 } }  // Less than or equal
{ age: { $ne: 25 } }  // Not equal
{ age: { $in: [25, 30, 35] } }  // In array

// Logical
{ $and: [{ age: { $gt: 25 } }, { age: { $lt: 30 } }] }
{ $or: [{ age: 25 }, { age: 30 }] }
{ $not: { age: 25 } }

// Array
{ hobbies: "coding" }  // Contains element
{ hobbies: { $all: ["coding", "reading"] } }  // Contains all
{ hobbies: { $size: 3 } }  // Array size
```

## Using MongoDB Shell

```bash
# Start MongoDB shell
mongo

# Show databases
show dbs

# Use/create database
use my_database

# Show collections
show collections

# Run commands
db.collection.find()

# Execute script
mongo my_database < script.js
cat script.js | mongo my_database
```

## Using PyMongo (Python)

### Connect to MongoDB
```python
from pymongo import MongoClient

# Connect
client = MongoClient('mongodb://127.0.0.1:27017')

# Get database
db = client.my_database
# Or
db = client['my_database']

# Get collection
collection = db.my_collection
# Or
collection = db['my_collection']
```

### CRUD Operations
```python
# Insert
doc = { "name": "Alice", "age": 25 }
result = collection.insert_one(doc)
print(result.inserted_id)

# Find all
for doc in collection.find():
    print(doc)

# Find with filter
for doc in collection.find({ "age": 25 }):
    print(doc)

# Find one
doc = collection.find_one({ "name": "Alice" })

# Update
collection.update_one(
    { "name": "Alice" },
    { "$set": { "age": 26 } }
)

# Delete
collection.delete_one({ "name": "Alice" })

# Count
count = collection.count_documents({ "age": { "$gt": 18 } })
```

### Aggregation
```python
# Group and count
pipeline = [
    { "$group": { "_id": "$status", "count": { "$sum": 1 } } }
]
results = collection.aggregate(pipeline)

# Match, group, and sort
pipeline = [
    { "$match": { "age": { "$gt": 18 } } },
    { "$group": { "_id": "$city", "avg_age": { "$avg": "$age" } } },
    { "$sort": { "avg_age": -1 } }
]
```

## Testing Your Project

### MongoDB Shell Scripts
```bash
cd NoSQL

# List databases
mongo < 0-list_databases

# Create database
cat 1-use_or_create_database | mongo

# Insert document
cat 2-insert | mongo my_db

# Find documents
cat 3-all | mongo my_db

# Count documents
cat 5-count | mongo my_db
```

### Python Scripts
```bash
cd NoSQL

# List all documents
./8-main.py

# Insert a school
./9-main.py

# Update topics
./10-main.py

# Find by topic
./11-main.py

# Log stats (after populating)
./populate_nginx_logs.py
./12-log_stats.py
```

## Common MongoDB Commands

```javascript
// Database commands
show dbs                    // List all databases
use <database>              // Switch/create database
db.dropDatabase()           // Delete current database

// Collection commands
show collections            // List all collections
db.createCollection("name") // Create collection
db.collection.drop()        // Delete collection

// Document commands
db.collection.count()       // Count documents
db.collection.find().pretty() // Pretty print results
db.collection.find().limit(5) // Limit results
db.collection.find().sort({ age: -1 }) // Sort descending

// Indexes
db.collection.createIndex({ name: 1 }) // Create index
db.collection.getIndexes()  // List indexes
```

## Troubleshooting

### MongoDB Not Running
```bash
# Start MongoDB
brew services start mongodb/brew/mongodb-community@4.4

# Check status
brew services list

# Restart if needed
brew services restart mongodb/brew/mongodb-community@4.4
```

### Connection Issues
```python
# Test connection
from pymongo import MongoClient
try:
    client = MongoClient('mongodb://127.0.0.1:27017', serverSelectionTimeoutMS=2000)
    client.server_info()
    print("Connected!")
except Exception as e:
    print(f"Connection failed: {e}")
```

### PATH Issues
```bash
# Temporarily add to PATH
export PATH="/opt/homebrew/opt/mongodb-community@4.4/bin:$PATH"

# Permanently add to PATH (add to ~/.zshrc)
echo 'export PATH="/opt/homebrew/opt/mongodb-community@4.4/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

## Best Practices

1. **Schema Design**
   - Embed related data for faster reads
   - Reference data when it's large or frequently updated
   - Denormalize for read-heavy workloads

2. **Indexing**
   - Create indexes on frequently queried fields
   - Use compound indexes for multi-field queries
   - Monitor index performance

3. **Security**
   - Enable authentication in production
   - Use role-based access control
   - Encrypt sensitive data

4. **Performance**
   - Use projection to limit returned fields
   - Avoid large documents (max 16MB)
   - Use aggregation pipeline for complex queries
   - Monitor with profiler

## Resources

- [MongoDB Official Documentation](https://docs.mongodb.com/)
- [PyMongo Documentation](https://pymongo.readthedocs.io/)
- [MongoDB University](https://university.mongodb.com/) - Free courses
- [MongoDB Cheat Sheet](https://www.mongodb.com/developer/products/mongodb/cheat-sheet/)

## Project Checklist

- [x] MongoDB 4.4 installed
- [x] PyMongo 4.8.0 installed
- [x] All MongoDB shell scripts created (0-7)
- [x] All Python scripts created (8-12)
- [x] Test files created
- [x] Scripts are executable
- [x] Documentation complete

Good luck with your project! 🚀

