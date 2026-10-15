# Customer stores a name and past orders.
# MenuItem stores a name, price, category, and popularity rating.
# Menu holds items and supports filtering and sorting.
# Order holds selected items and calculates their total.

class Customer:
    def __init__(self, name):
        self.name = name
        self.purchase_history = []


class MenuItem:
    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        pass

    def filter_by_category(self, category):
        pass

    def sort_by_popularity(self):
        pass


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        pass

    def calculate_total(self):
        pass