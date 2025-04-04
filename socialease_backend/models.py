from pymongo import MongoClient

# Connect to MongoDB with updated parameters
client = MongoClient("mongodb+srv://socialease:sgkl01031308@cluster0.yo2mm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0&tls=true&tlsAllowInvalidCertificates=false")
db = client["socialease"]

# Define collections
notifications_collection = db["notifications"]


