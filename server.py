from flask import Flask, jsonify
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend requests

# MongoDB Setup
MONGO_URI = "mongodb+srv://artemnebel:<NeardsProud2005%40>@cluster0.ugrnp.mongodb.net/"

client = MongoClient(MONGO_URI)

try:
    db = client["dealsDB"]
    collection = db["deals"]
    print("✅ Connected to MongoDB successfully!")
except Exception as e:
    print("❌ MongoDB Connection Error:", str(e))

@app.route('/deals', methods=['GET'])
def get_deals():
    try:
        deals = list(collection.find({}, {"_id": 0}))  # Exclude MongoDB ID
        print("✅ Fetched Deals:", deals)  # Debugging
        return jsonify(deals)
    except Exception as e:
        print("❌ Error fetching deals:", str(e))
        return jsonify({"error": "Failed to fetch deals"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)