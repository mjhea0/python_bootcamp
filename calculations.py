#creating our own calculation module for pricing a product

def calculate_tax(product_price, tax_rate):
	tax = product_price*tax_rate
	return tax

def calculate_tip(product_price, tip_rate):
	tip = product_price*tip_rate
	return tip

def total(product_price, tax, tip):
	return product_price+tax+tip	
