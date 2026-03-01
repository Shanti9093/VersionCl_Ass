from flask import Flask, request, render_template
from datetime import datetime
from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

db = client.test
collection = db["flask_learn"]

app = Flask(__name__)

@app.route('/')
def home():
    day_of_week = datetime.today().strftime('%A')
    current_time = datetime.now().strftime('%H:%M:%S')
    return render_template(
        'index.html',
        day_of_week=day_of_week,
        current_time=current_time
    )

@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.form)
    result=collection.insert_one(form_data)
    form_data["_id"] = str(result.inserted_id)

    return "Data sumbimted successfully"
@app.route('/view')
def view():
    data = collection.find()
    
    for item in data:
        print(item)
        del item['_id']
    return "Data retrieved successfully"

if __name__ == '__main__':

    app.run(debug=True)
