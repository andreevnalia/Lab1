from flask import jsonify, request
from api_project import app

Customers = [
    {
        "id": 1,
        "name": "Olga"
    },
    {
        "id": 2,
        "name": "Oleg",
    },
    {
        "id": 3,
        "name": "Alla",
    },
    {
        "id": 4,
        "name": "Stanislav",
    },
    {
        "id": 5,
        "name": "Anastasia",
    },
]

Categories = [
    {
        "id": 1,
        "name": "Food",
    },
    {
        "id": 2,
        "name": "Drinks",
    },
    {
        "id": 3,
        "name": "Flowers",
    },
    {
        "id": 4,
        "name": "Books",
    },
]

Notation = [
    {
        "id": 1,
        "customer_id": 1,
        "category_id": 1,
        "date_time": "20.10.2022",
        "cost_amount": 2000,
    },
    {
        "id": 2,
        "customer_id": 3,
        "category_id": 2,
        "date_time": "15.09.2022",
        "cost_amount": 500,
    },
    {
        "id": 3,
        "customer_id": 2,
        "category_id": 3,
        "date_time": "19.10.2022",
        "cost_amount": 1300,
    },
    {
        "id": 4,
        "customer_id": 4,
        "category_id": 2,
        "date_time": "11.10.2022",
        "cost_amount": 350,
    },
    {
        "id": 5,
        "customer_id": 5,
        "category_id": 4,
        "date_time": "15.09.2022",
        "cost_amount": 1000,
    },
]


@app.route("/customers")
def get_customers():
    return jsonify({"customers": Customers})


@app.route("/customers", methods=['POST'])
def create_customers():
    pass


@app.route("/categories")
def get_categories():
    return jsonify({"categories": Categories})


@app.route("/category", methods=['POST'])
def create_category():
    pass


@app.route("/notation")
def get_information():
    return jsonify({"notation": Notation})


@app.route("/notation", methods=['POST'])
def customer_information():
    pass
