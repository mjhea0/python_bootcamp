Qn 1. *What does it mean that Python is a strong, dynamically typed language?*

Ans:
Strongly typed means that it enforces data types.  Data types are a set of values and the type of operations you can perform on those values.  In Python data types consist of numbers, strings, Booleans etc.  A strongly typed language like Python does not allow the mixing or concatenating of different data types without first converting one data type into another.

A dynamically typed language is one that does not check or enforce type-safety at compile-time.  Statically typed languages typically have clearly distinct compile-time and run-time phases, with program code converted by a compiler into a binary executable which is then run separately. In most dynamically typed languages  ‘running’ a file both compiles and executes it

*Qn 2. How do you access the Python Shell?*

ANS:
I use a Mac.  I access all Python files via the Terminal.  I type in 
Python filename.py 
to run the code in the filename.py.  
To access the Python shell (which I cannot use to open .py files), I opened the Python IDLE from the python 3.4.1 file I downloaded.

*QN3. How do you declare a variable?*

ANS:

Simply by assigning a variable name to a value.  The value will be dependent on the data type of the value and you need not specifiy the data type so
Name = “Brin” (value automatically recognised as a string) while
Num = 42 (recognises the value as a number) – you don’t need to speicify to python that 42 is a number.

*Qn4.  What’s the difference between a variable name and a variable value?*

ANS:

A variable value gets assigned to a variable name

*Qn5. What are Python’s built-in data types?*

Ans: 

Strings
Numbers (int, floats, complex numbers),
Lists,
Tuples,
Dictionaries

*Qn6. What’s the difference between an integer and a floating point number?*

Ans: Int – whole numbers (both negative and positive).Floating point numbers have decimals.

*Qn7.What are boolean values?*

Ans: True and False

*Qn8. What does the % operator do?*

Ans:
Modulus – returns the remainder of a division (so 7%2 = 1)

*Qn9. What’s the difference between a list and a tuple?*

Ans: A List collection of different types of data grouped together. Denoted by [].
Once various data points are gathered in a List, you can then manipulate the data within (you can add to, amend, slice data).

A tuple is a List that is immutable and so many functions/actions that can be performed on a List cannot be done on a Tuple. As an example you cannot append or sort a tuple as such an action would change the Tuple.  However such an action could be performed on a List.

*Qn10. What’s a dictionary?*

A dictionary is a collection of key-value pairs. The key & value pairs are listed between curly brackets " { } "

*Qn11. What’s the role of comments in your code?*

Ans: Comments are used to clarify code and help the programmer understand the intention.  The program does not interpret it.  Single line comments are one using ‘#’ and multiline using “””.

*Qn12. Test out the help() function. What did you learn?*

Ans: The function gives a one-line summary of the function or datatype that would need help with.  If you type in a datatype like List it will explain what a list is and give all the functions that can act or be used on that datatype.

*Qn13. Pass in float to the dir() function. What did you learn?*

Ans: 

It gives all the names/actions that can be undertaken in the float function

'__abs__', '__add__', '__bool__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getformat__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__int__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__setattr__', '__setformat__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']

*Qn14. One primitive that we didn’t go over is None. What does it represent?*

Ans: None is  a  data type in Python and it is a value that indicates no value, not existent.

*Qn15. You can check the data type of a variable or a value by using the type()
function. Test this out using various data types and variables. What did
you learn?*

Ans: 

Type(2.10) = float

Type(2) = int

Type(True) = Boolean

Type(“my”) = str

The function type() describes the data type of the argument fed to it.







