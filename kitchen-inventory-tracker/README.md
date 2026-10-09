# Kitchen Inventory Tracker

Tracks kitchen ingredients and updates the stock as they're used.

- `check_kitchen_stock()` prints the total number of items and each ingredient's amount
- `use_eggs(available_eggs, eggs_to_use)` uses eggs if there are enough, and returns the new count
- `make_fried_egg(available_eggs)` makes a fried egg when at least one egg is available

The project shows the difference between printing a value and returning it: the egg count
only changes when the returned value is saved back into `available_eggs`.

Run it: `python kitchen_inventory_tracker.py`
