
#Create a separate function for asking the user for prices.

def prices():
	price_list = [] #create empty list
	
	while True: #infinite loop
		user = input("input a price one at a time:")
		if user=="no":
			break # stops the loop
		else:
			price_list.append(user) # appends input to list
		
	print (price_list)

prices()


#In that function, only ask for one price at a time.
#Use a while loop, to continue to ask for prices until the user enters "no".
#Pass the list to the sum_cart() function.
#Why two for loops. Refactor to one.
