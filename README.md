# PPDA
 Python programming and data analysis

## lab 1
Introduction to python

## zad 1
What is 7 to the power of 4?

Split this string:
s = “Hi there Sam!”
into a list and replace Sam with dad.

Given the variables:
planet = “Earth”
diameter = 12742
Use .format() to print the following string:
The diameter of Earth is 12742 kilometers.

Given this nested list, use indexing to grab the word “hello”
lst = [1,2,[3,4],[5,[100,200,[‘hello’]],23,11],1,7]

Given this nested dictionary grab the word “hello”. Be prepared, this will be annoying/tricky
d = {‘k1’:[1,2,3,{‘tricky’:[‘oh’,‘man’,‘inception’,{‘target’:[1,2,3,‘hello’]}]}]}
​

What is the main difference between a tuple and a list? Intentionally generate an error by changing a tuple value.
Create a function that grabs the email website domain from a string in the form:
super_user@ee.pw.edu.pl
So for example, passing “super_user@ee.pw.edu.pl” would return: ee.pw.edu.pl

Create a basic function that returns True if the word ‘car’ is contained in the input string. Don’t worry about edge cases like a punctuation being attached to the word car, but do account for capitalization.

Create a function that counts the number of times the word “car” occurs in a string. Again ignore edge cases.
Example:
countCar(‘This car runs faster than the other car dude!’)
2

Use lambda expressions and the filter() function to filter out words from a list that don’t start with the letter ‘s’. For example:
seq = [‘soup’,‘dog’,‘salad’,‘cat’,‘great’]
should be filtered down to:
[‘soup’,‘salad’]

Final Problem
You are driving a little too fast, and a police officer stops you. Write a function to return one of 3 possible results: “No ticket”, “Small ticket”, or “Big Ticket”. If your speed is 60 or less, the result is “No Ticket”. If speed is between 61 and 80 inclusive, the result is “Small Ticket”. If speed is 81 or more, the result is “Big Ticket”. Unless it is your birthday (encoded as a boolean value in the parameters of the function) – on your birthday, your speed can be 5 higher in all cases.

def caught_speeding(speed, is_birthday):
pass

caught_speeding(81,True)
‘Small Ticket’

caught_speeding(81,False)
‘Big Ticket’

## lab 2
Quick repetition from lab 1.
More information about lists, generators and classes in python
