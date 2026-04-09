# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"
# Slicing items string to extract
candy1 = items[0:9] #'Bubblegum'
candy2 = items[10:20] #'Chocolate'
dry_goods = items[21:] #'Pasta'
# Slicing categories string to extract
category1 = categories[0:11] # 'Candy Aisle'
category2 = categories[12:24] # 'Pasta Aisle'
# Creating price variables
bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price = "$5.40"

print("We have " + candy1 + " " +"for"+ " " + bubblegum_price + " in the " + category1)
print("We have" + candy2 + " " +"for"+ " " + chocolate_price + " in the " + category1)
print(F"We have{dry_goods} for {pasta_price} in the{category2}")