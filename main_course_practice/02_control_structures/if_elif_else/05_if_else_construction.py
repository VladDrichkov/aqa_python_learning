candies = 96
capacity = 12

box_count = candies // capacity
print(box_count)
residue = candies % capacity

if residue > 0:
    print(residue)
