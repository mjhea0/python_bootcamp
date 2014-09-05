#########################################################################
     #### Modify the variables so that all of the statements output True. ####
     #########################################################################
var1 = [1,2,3,0]
     ###############################################
     #### Don't edit anything below this comment ###
     ###############################################
if type(var1) is list:
	print(True) 
else:
    print(False)

for num in var1:
	if not type(num) is int:
		print(False) 
	else:
		print(True)
for num2 in range(var1[3]): 
	if num2 in var1:
		print(False) 
	else:
		print(True)

#Built in Functions:

#str() converts any value to a string
#int() converts a number value (float or a string) to an integer.For a float it drops the decimals.
#len() shows the number of characters in the string
#type() gives the data type of the argument
#min() gives the smallest number or earliest alphabet
#max() gives the largest number or latest alphabet

# Exercise 3

def my_factorial(num):
	factorial = 1
	for item in range(1,num+1):
		factorial = item*factorial
	return factorial
	
print my_factorial(4)		

def my_sqrt(num):
	return num**0.5
print my_sqrt(25)	


