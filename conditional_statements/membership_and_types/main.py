# Product details
description = "Imported honey, raw and unfiltered"
price = "5.99"
count = 120

# Write your code here
# Check if the "raw" and "Imported" keywords exists in description
contains_raw = "raw" in description
contains_Imported = "Imported" in description

# Use the type() function to check if price is of type float
price_is_float = type(price) == float

# Use the type() function to check if count is of type int
count_is_int = type(count) == int

print("Contains 'raw':", contains_raw)
print("Contains 'Imported':", contains_Imported)
print("Is price a float?:", price_is_float)
print("Is count an integer?:", count_is_int)