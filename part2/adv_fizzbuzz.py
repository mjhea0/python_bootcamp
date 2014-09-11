# print numbers from 1 to 100

def fizzbuzz(x):

    for num in range(1,x+1):
    	list=[]
        if (num%3==0 and num%5==0):
    	    return "FizzBuzz"
    	    list.append("FizzBuzz")
        elif num%5==0:
        	return "Buzz"
            list.append("Buzz")
        elif num%3==0:
        	return "Fizz"
            list.append("Fizz")
        else:        	
            return num
            list.append(num)

fizzbuzz(35)


