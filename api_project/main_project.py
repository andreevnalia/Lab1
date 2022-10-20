from api_project.category import Category
from api_project.customer import Customer


def show_menu():
    print("Chose your function:")
    print("a - create customer")
    print("b - create category")
    return input()


"""Function of creation customer"""


def create_customer():
    print("Enter customer name:")
    customer_name = input()
    customer1 = Customer(1, customer_name)
    print(Customer.showme(customer1))


"""Function of creation category"""


def create_category():
    print("Enter category:")
    category = input()
    Category(1, category)


"""Function of creation note about costs"""


def create_notation():
    print("Create notation:")


"""Function of getting a list of categories"""


def get_list_of_categories():
    print("Enter the list of categories")


"""Function of getting information about customer"""


def get_information():
    print("Enter the customer:")


"""Function of getting notes in a category for customers"""


def get_notes():
    print("Enter the list in the category:")


def processing(text):
    if text == "a":
        create_customer()
    elif text == "b":
        create_category()
    elif text == "c":
        create_notation()
    elif text == "d":
        get_list_of_categories()
    elif text == "e":
        get_information()
    elif text == "f":
        get_notes()
    else:
        print("You enter wrong function!")
    show_menu()


user_input = show_menu()
processing(user_input)

"""match user_input:
    case"a":
        create_customer()
    case"b":
        create_category()"""
