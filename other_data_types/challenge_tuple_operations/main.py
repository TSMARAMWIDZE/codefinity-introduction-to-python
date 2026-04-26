# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")
# Count method
apple_count = shelf.count("apples")
print("Number of Apples:", apple_count)
# Index method
banana_index = shelf.index("bananas")
print("First Banana Index:", banana_index)
# Conditional statements
if apple_count < 5:       
        print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")
# Count and Index method and conditional statements
grapes_count = shelf.count("grapes")
if grapes_count == 1:
    print("Grapes need to be restocked.")
else:
    print("Grapes are sufficiently stocked.")
# Membership operators
has_oranges = "oranges" in shelf
orange_index = shelf.index("oranges")
if has_oranges:
        print("Oranges are at index:", orange_index)
else:
        print("Oranges are out of stock.")


