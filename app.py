from flask import Flask, request, render_template
from pymongo import MongoClient
import os

client = MongoClient(os.getenv("MONGO_URI"))
db = client.todo_db
collection = db.todo_collection


@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    item_name = request.form.get("itemName")
    item_description = request.form.get("itemDescription")

    data = {
        "itemName": item_name,
        "itemDescription": item_description
    }

    collection.insert_one(data)

    return "To-Do Item Submitted Successfully!"

@app.route("/todo")
def todo():
    return render_template("todo.html")

if __name__ == '__main__':

    app.run(debug=True)
