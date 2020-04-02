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

## zad 2
Problem 1
Construct a generator which returns a sequence of prime numbers as a function, class and expression ().

def myprimef():
  (...)

class MyPrimeC(object):
  (...)

primeg = (...)
Problem 2
Fill in the Line class methods to accept coordinate as a pair of tuples and return the slope and distance of the line.

class Line(object):
    
    def __init__(self,coor1,coor2):
        """Initialize instance attributes with tuples (x1,y1)  and (x2,y2)
        """
        (...)
    
    def distance(self):
        """Calculate the length of the segment (line)
        """
        (...)
    
    def slope(self):
        """ Return the slope of a line going through the ends ( the 'a' in y=ax+b)
        """
        (...)
EXAMPLE OUTPUT
coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

li.distance()
9.433981132056603

li.slope()
1.6
________

Problem 3
Fill in the class

class Cylinder(object):
    
    def __init__(self,height=1,radius=1):
        (...)
        
    def volume(self):
        (...)
    
    def surface_area(self):
        (...)
EXAMPLE OUTPUT
c = Cylinder(2,3)

c.volume()
56.52

c.surface_area()
94.2
Problem 4
Write a class that takes a filename as an argument, opens it and reads its content into a 2D matrix of values (an array of arrays: [[1,2],[3,4]]). The class should define a function info() which prints out statistical information about values in columns. Assume that the first row in the file specifies the column names. Assume that the cells can be both numbers or strings (you should plan a conversion strategy for statistical data analysis).

class DataFile(object):

  def __init__(self, filename='undef'):
    (...)
  
  def info(self):
    (...)
    
  def avg(self, colnum=0, colname=''):
    """ The column name or colnum can be provided alternatively
    """
    (...)
    
  def min(self, colnum=0, colname=''):
      (...)  
      
  def max(self, colnum=0, colname=''):
      (...)  

  def distinc(self, colnum=0, colname=''):
     "Counts distinct number of values in a given column."
      (...)  
HINTS:
For pretty printing values in the table use formatted string literals (from python 3.6+): print(f“‘{(123+98+138)/3:^20.2f}’”);

EXAMPLE INPUT
Given the file content is:

Name;Age;Weight;Height
John;6;25;123
Mary;4;18;98
Jack;8;32;138
df = DataFile('myfile.csv')
df.info()
EXAMPLE OUTPUT
The info() function should produce the following Statistical Data information:

           Min      Max      Avg    Distinct
Name:       -        -        -         3 
Age:        4        8        6         3
Weight:     18       32       25        3
Height:     98      138     119.66      3


## Zad3

Task 1 (Generators and lists comprehensions refresher)
Calculate a value of a polynomial for a vector of x coordinates using single line list comprehension expression and a generator.

You must apply the enumerate() and sum() functions

Test code:

c = [1,2,3]
x = [0, 2, 4, 8]
p = _____
print(p)

Should print:
[1, 17, 57, 209]

Task 2
Generate a smooth polynomial plot from Task 1 using dense vector of x coordinates

n = 100
xd = [8*x/n for x in range(n)]
Example of using a plot:

import matplotlib.pyplot as plt
x = [8*i/100 for i in range(0,100)]
y = [x**2 for x in x]
plt.plot(x,y)
Expected result:
Zaznaczenie_194.png

Task 3
Using a conditiional list comprehension, convert all occurrences of the letter ‘e’ in the following string to uppercase: thepurposeoflife

You can use ''.join( alist ) to join a list of characters into a single string.

upperstr = 'thepurposeoflife'
upperstr = ______
print(upperstr)
Task 4 - tuples as records
Use the following tuple of tuples
records = ((‘Sam’, 19, ‘CS’),
(‘Nicole’, 21, ‘Biochemistry’),
(‘Paul’, 20, ‘Fine Arts’),
(‘Ashley’, 18, ‘History’))
iterate over the records, unpack them, and print the results
This might be useful syntax for printing:
print(‘%s and %d and %s’, % (‘a string’, 10, ‘another string’))
Make a function as well to complete the following:
 def showrecords(records): '''Unpack records stored in a tuple of tuples and print each one in a nice format''' ... showrecords(___) 
Task 5 - Closures
Make a nested function and a python closure to make functions to get multiple multiplication functions using closures. That is using closures, one could make functions to create multiply_with_5() or multiply_with_4() functions using closures.

def multiplier_of(n):
  ____

test code
multiply_with_5 = multiplier_of(5)
print(multiply_with_5(9))
should return 45

multiply_with_45 = multiplier_of(multiply_with_5(9))
print(multiply_with_45(2))
should return: 90
Task 6 - decorators with arguments
Make a decorator factory which returns a decorator that decorates functions with one argument. The factory should take one argument, a type, and then returns a decorator that makes function should check if the input is the correct type. If it is wrong, it should print(“Bad Type”) (In reality, it should raise an error, but error raising isn’t in this tutorial). Look at the tutorial code and expected output to see what it is if you are confused (I know I would be.) Using isinstance(object, type_of_object) or type(object) might help.

def type_check(correct_type):
    def check(old_function):

        ____

    return check
  
Use  isinstance(arg, correct_type) to check if arg is of correct type

@type_check(int)
def times2(num):
    return num*2

print(times2(2))
times2('Not A Number')

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])
Should produce:

4
Bad Type
H
Bad Type
Task 7 - Registering Plugins
Decorators don’t have to wrap the function they’re decorating. They can also simply register that a function exists and return it unwrapped. This can be used, for instance, to create a light-weight plug-in architecture:

import random
PLUGINS = dict()

def register(func):
    ______

@register
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)
  
randomly_greet('John')

## Zad3 optional
Optional exercises for L03

.1. Implement a list comprehension expression with with and open file which will return a list with sums of floating values in each line. The list comprehension should be universal and independent from the number of columns. It should work without modifying the code for the examples of files:

a b c d
1.2 3.4 
1 32.1 
2 1 9.0
Another file:

a b c d d
1.2 3.4 1 
3 2.32.1 2 
1 9.0 1.0
.2. Write a generator (in any form expression, function or class, smartly use filter - your choice) which will filter out the lines from the text file containing at least one value divisible without the rest (modulo ==0) by provided argument. Declaration can be:

def filter_divisible(v):
    pass
