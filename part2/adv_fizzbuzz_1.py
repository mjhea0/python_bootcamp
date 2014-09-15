# refactor to generate output to a list
def fizzbuzz(upper_limit):
    output_list = []
    for num in range(1, upper_limit+1):

        if (num % 3 == 0 and num % 5 == 0):
            output_list.append("FizzBuzz")

        elif num % 5 == 0:
            output_list.append("Buzz")

        elif num % 3 == 0:
            output_list.append("Fizz")
        else:
            output_list.append(num)
    print(output_list)        


print(fizzbuzz(35))

if __name__ == '__main__':