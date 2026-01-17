# The item's discount and stock status have been defined
discounted = False
lowStock = True

# Combine conditions to check if boolean variable movingProduct is True
# ('movingProduct') will become 'True' if either condition 'discounted' or 'lowStock' is 'True'
# Using the (or) logical operator

movingProduct = discounted or lowStock

# Use the 'and' operator to check if the item is eligible for 'promotion' that is 'True' 
# If the item is not 'discounted' and 'sufficiently stocked'
promotion = discounted and not lowStock

# Print the result
print("Is the item eligible for promotion?", promotion)

