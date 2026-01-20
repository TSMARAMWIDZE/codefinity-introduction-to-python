seasonal = True
on_sale = False
selling_well = False
current_stock = 150
high_stock_threshold = 100

# Boolean logic using 'and', 'or' and 'not' operators
overstock_risk = seasonal and (current_stock > high_stock_threshold) # 'True'
discount_eligible = (not selling_well) and (not on_sale) # 'True'

# the make_discount variable will become 'True' only if overstock_risk or discount_eligible is 'True'
make_discount = overstock_risk or discount_eligible

print("Should the item be discounted?", make_discount)