#!./venv/bin/python
# ------------------------------------------------------------------------------
#  Copyright (c) 2019. Anas Abu Farraj
# ------------------------------------------------------------------------------

item_a = {'name': 'book', 'price': 17.99}
item_b = {'name': 'piano', 'price': 524.00}

item_a.update(item_b)

print(item_a)  # {'name': 'piano', 'price': 524.0}
