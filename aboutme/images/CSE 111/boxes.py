import math

no_of_items = int(input('Enter the number of items:   '))
items_per_box = int(input('Enter the number of items per box:  '))

no_of_boxes = math.ceil(no_of_items/items_per_box)

print()

print(f'For {no_of_items} items, packing {items_per_box} items in each box, you will need {no_of_boxes} boxes.')

