from flask import jsonify, request
from api_project import app


Categories = [
    {
        "id": 1,
        "name": "Food",
    },
]


@app.route("/categories")
def get_categories():
    return jsonify({"categories": Categories})


@app.route("/category", methods=['POST'])
def create_category():
    pass

