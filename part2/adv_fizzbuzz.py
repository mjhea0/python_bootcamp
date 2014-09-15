# print numbers from 1 to 100
def fizzbuzz(upper_limit):
    for num in range(1, upper_limit+1):

        if (num % 3 == 0 and num % 5 == 0):
            print("FizzBuzz")

        elif num % 5 == 0:
            print("Buzz")

        elif num % 3 == 0:
            print("Fizz")
        else:
            print(num)    

print(fizzbuzz(100))


if __name__ == '__main__':