from models import MenuItem, Menu, Order

# Check that an order adds item prices correctly.
# Check that an empty order totals zero.
# Check that category filtering returns only matching items.
# Check that popularity sorting leaves the original menu unchanged.

def test_calculate_total_with_multiple_items():
    order = Order()
    order.add_item(MenuItem("Spicy Burger", 10.0, "Meals", 95))
    order.add_item(MenuItem("Large Soda", 5.0, "Drinks", 80))

    assert order.calculate_total() == 15.0


def test_order_total_is_zero_when_empty():
    assert Order().calculate_total() == 0.0


def test_filter_by_category():
    menu = Menu()
    burger = MenuItem("Spicy Burger", 10.0, "Meals", 95)
    soda = MenuItem("Large Soda", 5.0, "Drinks", 80)
    menu.add_item(burger)
    menu.add_item(soda)

    assert menu.filter_by_category("Drinks") == [soda]
    assert menu.items == [burger, soda]


def test_filter_with_no_matches():
    menu = Menu()
    menu.add_item(MenuItem("Spicy Burger", 10.0, "Meals", 95))

    assert menu.filter_by_category("Desserts") == []


def test_sort_by_popularity_preserves_original_menu():
    menu = Menu()
    soda = MenuItem("Large Soda", 5.0, "Drinks", 80)
    burger = MenuItem("Spicy Burger", 10.0, "Meals", 95)
    cookie = MenuItem("Cookie", 2.0, "Desserts", 90)
    for item in [soda, burger, cookie]:
        menu.add_item(item)

    assert menu.sort_by_popularity() == [burger, cookie, soda]
    assert menu.items == [soda, burger, cookie]


def test_empty_menu():
    menu = Menu()

    assert menu.filter_by_category("Drinks") == []
    assert menu.sort_by_popularity() == []