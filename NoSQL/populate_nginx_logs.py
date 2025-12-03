#!/usr/bin/env python3
"""
Script to populate nginx logs collection for testing 12-log_stats.py
"""
from pymongo import MongoClient


def populate_logs():
    """Populates the nginx collection with sample logs"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Clear existing data
    nginx_collection.delete_many({})

    # Sample logs
    logs = [
        {"method": "GET", "path": "/"},
        {"method": "GET", "path": "/status"},
        {"method": "GET", "path": "/status"},
        {"method": "GET", "path": "/api/users"},
        {"method": "POST", "path": "/api/users"},
        {"method": "POST", "path": "/api/login"},
        {"method": "PUT", "path": "/api/users/1"},
        {"method": "PUT", "path": "/api/users/2"},
        {"method": "PATCH", "path": "/api/users/1"},
        {"method": "DELETE", "path": "/api/users/1"},
        {"method": "GET", "path": "/status"},
        {"method": "GET", "path": "/health"},
        {"method": "POST", "path": "/api/posts"},
        {"method": "GET", "path": "/status"},
    ]

    # Insert logs
    nginx_collection.insert_many(logs)
    print(f"Inserted {len(logs)} logs into logs.nginx collection")


if __name__ == "__main__":
    populate_logs()

