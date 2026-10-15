# ByteBites

A Python backend for the AI110 Week 3 campus food ordering lab.

## Classes

- Customer: name and purchase history.
- MenuItem: name, price, category, and popularity rating.
- Menu: add items, filter categories, and sort by popularity.
- Order: selected items and total cost.

## Run Tests

    python3 -m venv .venv
    source .venv/bin/activate
    python -m pip install pytest
    python -m pytest

## Verification

All 6 tests passed, covering totals, empty orders, filtering, missing categories, sorting, and empty menus. Sorting preserves the original menu.

## AI Collaboration

AI helped draft the diagrams, classes, methods, and tests. I verified the behavior with manual examples and pytest.

## Class Diagram

[Mermaid source](bytebites_design.mmd)

```mermaid
classDiagram
    class Customer {
        +str name
        +list purchase_history
    }

    class MenuItem {
        +str name
        +float price
        +str category
        +int popularity_rating
    }

    class Menu {
        +list items
        +add_item(item) None
        +filter_by_category(category) list
        +sort_by_popularity() list
    }

    class Order {
        +list items
        +add_item(item) None
        +calculate_total() float
    }

    Customer "1" --> "0..*" Order : purchase_history
    Menu "1" --> "0..*" MenuItem : items
    Order "1" --> "0..*" MenuItem : items
```
