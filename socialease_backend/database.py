import os
from pymongo import MongoClient

# Get MongoDB URI from environment variable
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://socialease:sgkl01031308@cluster0.yo2mm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Create MongoDB Client with updated parameters
try:
    client = MongoClient(
        DATABASE_URL,
        serverSelectionTimeoutMS=5000,
        connectTimeoutMS=10000,
        socketTimeoutMS=20000,
        tlsInsecure=True,  # Important for fixing SSL issues on some platforms
        connect=False  # Connect lazily when needed
    )
    
    # Test connection
    client.admin.command('ping')
    print("MongoDB connection successful")

    # Access the database
    db = client["socialease"]
    
    # Test document code only for local development - comment this out for production
    # collection = db["progress"]
    # document = {"user_id": "kabiz", "day": 7, "score": 100}
    # insert_doc = collection.insert_one(document)
    # print("inserted doc id = " + str(insert_doc.inserted_id))

except Exception as e:
    print(f"MongoDB connection error: {e}")
    # Use a fallback or raise an error depending on your needs
    db = None

# Dependency to get a database connection
def get_db():
    try:
        if db is None:
            raise Exception("Database connection failed")
        yield db
    finally:
        pass