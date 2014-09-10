Qn1.	Why is whitespace important? 

Ans - The 4 spaces in Python (indenting) indicates when a block of code starts and ends

Qn2 - What do the following keywords do if, else, elif, while, and for?  Explain in English

Ans - These keywords allow data to flow in a particular direction by the use of conditional statements(depending on whether the condition met is True or False) and loops (in the case of “for” and “while”).

If/else/elif are conditional statements that are used to determine if a particular assertion or statement is true or false.  We can the n instruct the program to perform a particular task (like print something) if something is True or something else if the statement is False.  Elif allows multiple scenarios to be contemplated.

The for loop works through a string or a list (or other datatype like dictionary/tuple) or iterables till that finite item is exhausted.  The While loop works under a condition (ie ‘while’ something is or is not True.

Qn3. Provide an example of an if/elif/else conditional. 

Ans - 

    X = input(“Enter an integer between 0 and 10”)
    Int_X = int(X)
        If Int_X >0:
            Print (“you are out of range”)
        Elif Int_X <5:
            Print (“your number is less than 5”)
        Else:
            Print (“Your number is greater than 5”)

Qn4.  What’s the difference between a while and for loop? How do they work?  Explain in English, then provide examples. 

Ans - A while loop will keep executing as long as the Boolean expression that the while statements refers to is “True”.

    X = 10
    While x >5:
        Print (x)
        x= x-1

The above function will print x  till x = 6 and will no longer print it once it gets to 5.  Note if x does not iterate to less than 5, it will keep going as an infinite loop.

This contrasts with a for loop that iterates over a collection of item (list, dictionaries), where the items list is fixed. It goes to each item one by one and executes the code below it. Eg
   
   
    X = [1,2,3,4]
    For num in x:
       Print num

This will print the numbers 1-4.

Qn5. Look up the break and continue statements. How do you use them?  Again, explain in English, then provide a few examples. 

Ans - The “break” statement terminates the current loop and resumes execution at the next statement. The continue statement is used in a while or for loop to take the control to the top of the loop without executing the rest statements inside the loop. 

**Example of break statement:**

    list = [1,2,3,4,5,6]
    sum = 0
    count = 0
    for num in list:
	    sum = sum + num
	    count = count + 1
	    if count==3:
		    break
        print ('sum of first', count, 'integers is:', sum) 

The output will be:

**sum of first 3 integers is: 6 **

**Example of Continue statement:**

    for x in range(5):
	    if x==3:
		    continue
	    print (x)

**The output will be:**

0

1

2

4

Qn6 - What’s a function?

Ans - A function is a mini program.  It takes user input, process it based on the code it is meant to execute and then produces an output.  Once defined a function can be called at anytime and a function can also take another function as its input.

Qn7 - What’s a module? 

Ans - A module allows us to logically organize the python code. Grouping related code into a module makes the code easier to understand.  Eg the maths module contains various arithmetic functions within it.

Qn8 - How do you define a function? 

Ans - 

    Def function_name(arg1, arg 2):
    # when you call this function it is then activated
    
Qn9 - How do you import a module? 

Ans - 

    Import “module name” 
     eg import math
     or
     from random import randint
  

