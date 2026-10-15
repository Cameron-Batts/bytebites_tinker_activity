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
        self.items.append(item)

    def filter_by_category(self, category):
        # Return matching items without changing the menu.
        return [item for item in self.items if item.category == category]

    def sort_by_popularity(self):
        # Return a new list with the most popular items first.
        return sorted(
            self.items,
            key=lambda item: item.popularity_rating,
            reverse=True,
        )


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        # An empty order returns 0.0.
          return sum((item.price for item in self.items), start=0.0)