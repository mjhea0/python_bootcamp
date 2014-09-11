from calculations import calculate_tax, calculate_tip, total

def adder(item1, item2=5):
	return item1 + item2
	
subtotal = adder(10,20)
print(subtotal)

tax = calculate_tax(subtotal,0.1)
tip = calculate_tip(subtotal,0.2)
total = total(subtotal, tax, tip)

print(total)

