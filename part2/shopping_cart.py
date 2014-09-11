#calculate product total
prices = []
user_input = input("What are the prices, separate them by comma?")
prices.append(user_input)
def sum_cart(x):
	for item in prices:
		sum = 0
		for num in item:
			sum = sum+ num
		return sum
print (sum_cart(prices))		
	




# add tax to the product total
#def add_tax(product_price, tax_rate):
#	new_price = product_price/100 * (100 + tax_rate)
#	return new_price

	## --- run code --- ##

# calculate pre-tax price
#product_total = sum_cart(10,20)

#print("The pre-tax price is: ${}".format(product_total))	

#calculate post-tax price
#after_tax = add_tax(product_total, 7.5)
#print ("The after-tax price is: ${}".format(after_tax))



