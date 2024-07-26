print("hello world")
print("Update")

from calculator import *
print("Calculator.py")
print("------------")
print(add(5,7))
print(substract(5,7))
print(multiply(5,7))
print(divide(5,7))
print("------------")

from lambda_calculator import *
print("Lambda_Calculator.py")
print("------------")
x=5
y=7
l_add(x,y)
l_sub(x,y)
l_mul(x,y)
l_div(x,y)
print("------------")

from string_operations import *
print("String_Operation.py")
print("------------")
sample_string = "hello World"
print("Original:", sample_string)
print("Reversed:", reverse_string(sample_string))
print("Capitalized:", capitalize_string(sample_string))
print("Lowercase:", lowercase_string(sample_string))
print("Uppercase:", uppercase_string(sample_string))
print("------------")

from utilities.calculator import add as add_def, substract as subtract_def, multiply as multiply_def, divide as divide_def
from utilities.string_operations import reverse_string as revs, capitalize_string as caps, lowercase_string as lows, uppercase_string as ups

# Sample inputs and printing results using calculator.py
print("Using calculator.py:")
print("Addition:", add_def(10, 5))
print("Subtraction:", subtract_def(10, 5))
print("Multiplication:", multiply_def(10, 5))
print("Division:", divide_def(10, 5))

# Sample strings and printing results using string_operations.py
sample_string = "hello World"
print("\nUsing string_operations.py:")
print("Original:", sample_string)
print("Reversed:", reverse_string(sample_string))
print("Capitalized:", capitalize_string(sample_string))
print("Lowercase:", lowercase_string(sample_string))
print("Uppercase:", uppercase_string(sample_string))