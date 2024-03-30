import math
items = int(input("Enter the number of items: "))
box_items = int(input("Enter the number of items per box: "))
num_boxes = math.ceil(items / box_items)
print()

print(f"For {items} items, packing {box_items}"
    f" items in each box, you will need {num_boxes} boxes.")