import sys
import os
#! /usr/bin/python
# This line, starting with the #! (also known as a "shebang", allows us to run
# this script by doing just "./ptpp.py", instead of "python ptpp.py".  It informs
# linux that python is what will be used to run this script

# Type-checking functions - to guarantee that variables are a certain type
def assert_isInt(n):
    if not isinstance(n, int):
        raise Exception("ERROR: Invalid parameter type")
    pass

def assert_isList(v):
    # Demand that the parameter be a list
    if not isinstance(v, list):
        raise Exception("ERROR: Parameter must be a list")
    pass

def assert_isString(s):
    # Demand that the parameter be a string
    if not isinstance(s, str):      # python3; if python2, use basestr
        raise Exception("ERROR: Parameter must be a string")
    pass
    
###################################################
#   AN EXPLANATION OF BASIC TYPES AND FUNCTIONS   #
#  Use this section as REFERENCE as you practice! #
###################################################

# References Section

def defining_basic_types():
    ''' Integers! '''
    print
    2 + 3  # 2+3 = 5
    print
    2 - 3  # 2-3 = -1
    print
    2 * 3  # 2*3 = 6
    print
    14 / 7  # 14 divided by 7 = 2
    print
    13 / 7  # 13 divided by 7 = 1.  Remainders are not reported
    print
    13 % 7  # 13 modulus 7 = 6. This is the remainder!
    print
    101 % 2  # simple way to determine even or odd.  If remainder is 0:even, else:odd.
    print
    2 ** 3  # 2 to the power of 3 = 8 (2*2*2)

    a = 1  # a is an int, with the value of 1
    print
    type(a)  # prints <type 'int'>
    print
    a  # 1
    a + 1
    print
    a  # 1, notice we did not update the value of a
    a = a + 1
    print
    a  # 2, this time we did
    a += 1
    print
    a  # 3, this is another way of doing the same thing

    ''' Strings! '''
    b = "Hello, World!"  # b is a string, with the value of "Hello, World!"
    print
    type(b)  # prints <type 'str'>
    print
    b  # prints "Hello, World!"
    print
    len(b)  # prints the length of string b -> 13
    print
    b * 3  # multiplying a string, causes it to repeat -> "Hello, World!Hello, World!Hello, World!"
    print
    "Oh... " + b  # adding strings together concatonates -> "Oh... Hello, World!"

    ''' Lists are what they sound like, a list of values '''
    c = [1, "two", "three", 4]  # c is a list with 4 values of different types
    print
    type(c)  # prints <type 'list'>
    print
    len(c)  # print length of c -> "4"
    print
    c[0]  # value at offset 0 (first item in the list) -> 1
    print
    c[3]  # value at offset 3 (fourth item in the list) -> 4
    print
    c[-1]  # last value of the list -> 4
    print
    c[-2]  # 2nd to last value of thelist -> "three"
    print
    c[0:2]  # print values from offset 0 to 2, NOT INCLUDING offset 2 -> [1,"two"]
    print
    c[1:]  # print values from offset 1, through the end -> ["two","three",4]
    c[2] = 3
    print
    c  # [1,"two",3,4], you have changed the value of c[2]

    ''' Strings are "sort of" like a list of characters, you can operate on them similarly '''
    d = "I LOVE PYTHON!"
    print
    d[0:5]  # prints -> "I LOV"
    print
    d[5:]  # prints -> "E PYTHON!"
    print
    d[-1]  # prints -> "!".  -2, -3, -4, etc... iterate backwards!

    return


def booleans():
    ''' Booleans! True or False? '''
    a = True
    b = False
    if a:  # a == True...
        print(a)  # so this will run!
    if b:  # b == False
        print(b)  # so this will NOT run!
    if a == b:  # equality operator (==) returns "True" or "False"
        print(a, b)  # a does not equal b, this will not print
    if a != b:  # not equal (!=) also evaluates to "True" or "False"
        print(a, b) # this will print
    # Also keep in mind that <, <=, >, >=, will also evaluate to True or False

    ''' Basic types... used like booleans? What? '''
    a = 0  # ints with value 0
    b = ""  # empty strings
    c = []  # and empty lists ALL EVALUATE TO FALSE
    # ints > or < 0, non-empty strings, and non-empty lists all evalue to TRUE
    if a:
        print(a)  # will not run!
    if b:
        print(b)  # will not run!
    if c:
        print(c) # will not run!

    ''' and / or '''
    a = True
    b = False
    if (a and b):
        print(a)  # This will not run
    if (a or b):
        print(b)  # This will run

    return


def if_elif_else():
    a, b, c = 1, 2, 3  # defining similar types this way is allowed, a=1, b=2, c=3

    ''' the basics of logic are if->then statements, here are some examples '''
    if a == 1:  # if the value of a is equal to 1
        print(a)  # then do this

    ''' if the condition of "if" is NOT met, we can use alternate conditions '''
    if a == 2:  # if a equals 2
        print(a)
    elif b == 2:  # else if b equals 2
        print(b)  # this will run
    # However, if the condition of "if" IS met, then elif will NOT be run.
    # if BOTH checks are needed, use two "if"s.

    ''' else is a "catchall", and will run if no other conditions are met '''
    if a == 3:  # nope
        print(a)  # will not run
    elif b == 3:  # nope
        print(b)  # will not run
    else:
        print(c)  # will run

    return


def loops_and_iteration():
    ''' there are two basic loops in python, "while" and "for" '''
    a = 0  # this is a counter-loop
    while (a < 100):  # while a is less than 100
        print(a)  # print a
        a += 1  # add one to a
        # prints 0->99.  Will not print 100, why?

    st = "Hello, World!"  # this is standard iteration
    for ch in st:  # read it like this "For character in string"
        print(ch)  # print character.  Try this in the interpreter
        # prints each character in "Hello, World!" on a new line

    '''Sometimes we'll want to use a counter for iterating a list'''
    ls = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    for n in range(len(ls)):  # xrange returns a range of numbers from 0 to the number provided.
        print(ls[n])  # in this case, n equals 0-8.  Notice there are 9 items in ls, but the iteration starts at 0!
    # this will print each character in ls on a new line
    return


def how_to_pause_your_program():
    # the input() cheat - makes the script stop until you press a key
    # this can be useful for debugging, or if you just want to pause for a moment
    print("I AM ON YOUR SCREEN")
    input()
    print("TAKING UP YOUR SPACE")
    input("(this time there is a message)")
    print("HERP HERP")
    a = input("now type a bunch of things and press enter")
    print(a)
    input("paused again")
    return


# End of References

# Start of Assignments

###########################################################
#                  STRING PRACTICE                        #
#         Refer to CodingBat.com 's String Basics         #
###########################################################
def greet(name):
    # First, die if the name is zero characters
    # long or if it is not even a string in the first
    # place
    if not isinstance(name, str) or len(name) == 0:
        raise Exception("<invalid input>")
    
    # We are guaranteed here that name is a string variable
    # with length greater than zero.
    return "Hello " + name + "!"

# Given a string name, return a greeting of the form "Hello Name!"
# str1('Bob')-> 'Hello Bob!'
# str1('Alice')-> 'Hello Alice!'
# str1('X')-> 'Hello X!'


def abba(a, b):
    # Input checking
    assert_isString(a)
    assert_isString(b)

    return a + b + b + a

# Given two strings, a and b, return the result of putting them in
# the order of abba.  e.g. "Hi" and "Bye" returns "HiByeByeHi"


def slice_us(out, word):
    assert_isString(out)
    assert_isString(word)
    if len(out) != 4:
        raise Exception("Out string can only be of length 4")

    return out[0:2] + word + out[2:4]

# Given an "out" string length of 4, such as "<<>>", and a word
# return a new string (c)  where the word is in the middle of the out
# string.  e.g. slice_us("<<>>", "word") -> "<<word>>"


def duplicate(s, n):
    assert_isString(s)
    assert_isInt(n)
    if len(s) < 2:
        raise Exception("ERROR: first argument must be 2 characters or longer")
    if n <= 0:
        raise Exception("ERROR: second argument must be a positive integer")
 
    return s[-2:] * n

# Given a string s and a number n, return a new string made of
# n copies of the last 2 chars in the original str. (hint: slicing)
# e.g. duplicate("word", 4) -> "rdrdrdrd"


def shortlongshort(s1, s2):
    assert_isString(s1)
    assert_isString(s2)

    if len(s1) == 0:
        raise Exception("String s1 must not be blank")
    if len(s2) == 0:
        raise Exception("String s2 must not be blank")

    return s1 + s2 + s1 if len(s2) >= len(s1) else s2 + s1 + s2

# Given 2 strings, return a new string in the form of shortlongshort
# use len(s) to figure out the length of a str


#########################################################
#                    INTEGER PRACTICE                   #
#########################################################

def adding(a, b):
    assert_isInt(a)
    assert_isInt(b)

    return a+b if a != b else 2*(a+b)


# return the sum of the two values
# unless the values are the same, then double their sum

def abs_dif(n):
    assert_isInt(n)

    return abs(n-21) if n <= 21 else 2*(n-21)

# given an int n, return the absolute value of the difference between n and 21
# double it if n is over 21
# use abs(calculation) to give you the absolute value


def tens(a, b):
    assert_isInt(a)
    assert_isInt(b)

    return a==10 or b==10 or a+b==10

# given 2 ints, return True if one of them is 10, or if their sum is 10
# else return false


def hundreds(n):
    assert_isInt(n)
    
    return abs(100-n) <= 10

# given an int n, return True if it is within 10 of 100
# note: abs(num) computes the absolute value of a number


def negatives(a, b, negative):
    assert_isInt(a)
    assert_isInt(b)

    return a*b < 0 if not negative else a < 0 and b < 0

# given 2 int values, return True if one is negative and one is positive
# Except if the paramater "negative" is True, then return True only if both are negative
# otherwise return false


#######################################################
#                     LIST PRACTICE                   #
#######################################################

def sixes(a):
    assert_isList(a)
    if len(a) < 2:
        return False     # Due to the requirements, pointless to proceed if we don't have at least two elements

    return a[0] == 6 or a[-1]==6


# given a list of integers a, return True if 6 appears as either
# the first or last element.  The array length will be one or more
# hint: use a for loop

def same_length(a):
    assert_isList(a)
    if len(a) < 1:
        return False

    return len(a) > 1 and a[0] == a[-1]

# given an array of ints, return True if the array is greater than length 1
# and the first element and the last element are the same value
# list2([1,2,3,4]) -> False
# list2([1,2,3,1]) -> True


def sum_list(l):
    assert_isList(l)# assert that l is a list
    for num in l:   # also assert list is a list of numbers
        assert_isInt(num)
    return sum(val for val in l)

# given an array of integers, return the sum of those integers
# there is a built in function that does this already, bonus points if you use it
# type "dir(__builtins__)" in the python console to view a list of builtin functions


def rotate_slice(l):
    assert_isList(l)
    for num in l:   # also assert list is a list of numbers
        assert_isInt(num)

    return l[2:] + l[:2]

# given a list l, rotate it left by 2 spaces
# [1,2,3,4] -> [3,4,1,2]
# use slicing, do not create a new list


def pop_append(l):
    assert_isList(l)
    for num in l:   # also assert list is a list of numbers
        assert_isInt(num)

    if len(l) < 2:  # will not work for lists shorter than length 2
        return []

    x = l.pop()
    y = l.pop()
    
    l.append(x*y)
    l.append(l[0] + l[1])
    return l

# given a list l of integers, do the following:
# 1. remove the last 2 items from the list (use l.pop())
# 2. append the product of the popped values (use l.append(value))
# 3. append the sum of the first 2 items in the list.


#########################################
#           BOOLEAN PRACTICE            #
#########################################
def basic_bool(a, b, c):
    count = 0
    if a: count += 1
    if b: count += 1
    if c: count += 1
    return count

# write "if" statements that check if a,b,c are true or false
# note: do not do a==False or a==True
# return the number of True's

def multi_bool(a, b):
    assert_isInt(a)
    assert_isInt(b)

    return a*b > 0

# write an "if" statement that checks if the product of a and b
# is greater than 0 if so return True, else return False

def iter_bool(a):
    assert_isList(a)
    
    if len(a) == 0:
        return 1337  # No 7's can possibly exist in a list of zero length

    # demand that each element of the list 'a' be an int, or else raise
    # an exception
    for i in range(len(a)):
        assert_isInt(a[i])
        
    # iterate through the list and test values
    result = 1337               # default value
    for i in range(len(a)):
        if a[i] == 6:
            break

        if a[i] == 7:
            if result == 1337:
                result = 1
            else:
                result += 1
    return result

# a is a list of integers, using a for loop, iterate through a to find
# all instances of the number 7.  If a 6 appears, break out of the for loop.
# if the number of 7's found is 0, return the number 1337

def complex_bool_one(a, b, c):
    assert_isInt(a)
    assert_isInt(b)
    assert_isInt(c)

    return a > b and a > c


# write a SINGLE return statement, an no other lines of code
# return true if a is greater than b and c


def complex_bool_two(a, b, c):
    assert_isInt(a)
    assert_isInt(b)
    assert_isInt(c)

    return (abs(a-c) <= 1 or abs(b-c) <= 1) and (abs(a-b) >= 2 or abs(a-c) >= 2 or abs(b-c) >= 2)

# write a single return statment: return true if -
# 1- one of a OR b is close to c (within 1 number) AND
# 2- one of a OR b is far from the other two (>= 2 away)

##################################################
#              LOOPING AND ITERATION             #
##################################################
def count_for(l):
    # Demand that we have a list of strings
    assert_isList(l)
    for i in range(len(l)):
        assert_isString(l[i])
        if l[i].startswith("xkcd"):
            l[i] = l[i].replace("xkcd", "CAD")

    return l

# given a list of strings (l), iterate through each item using a counter
# if the item begins with "xkcd", strip off "xkcd" frrom the beginning
# and replace it with "CAD".  Return the changed list.
# Note: Do not create a second list.  Operate on the exiting one.


def iter_for(l):
    #Demand that we have a list of ints
    assert_isList(l)
    even_sum = 0
    odd_sum = 0
    for i in range(len(l)):
        assert_isInt(l[i])      # ith item must be an int
        if l[i] % 2 == 0:
            even_sum += l[i]
        else:
            odd_sum += l[i]
    
    print("even_sum = {}".format(even_sum))
    print("odd_sum = {}".format(odd_sum))
    return even_sum*odd_sum 

# given a list of integers (l), iterate through each item
# if the int is even, add it to even_sum
# if the int is odd, add it to odd_sum
# After summing all the numbers, return the product of even_sum and odd_sum


def pop_while(l):
    if len(l) == 0:
        return (l, 0)  # define the sum of an empty list to be zero
        
    assert_isList(l)
    for i in range(len(l)):
        assert_isInt(l[i])
        
    m = 0
    while(l):
        m += l.pop()
        
    return (l, m)

# Given a list of integers (l), use a while loop that tests if l evalutes to True (not empty)
# If l is not empty, use l.pop() to add the numbers in the list to m
# return l and m


###############################################
#               FUNCTIONS!                    #
###############################################

def my_first_function():
    return True

def functions_one():
    my_first_function()

# write a function named my_first_function
# have it accept no parameters, and return True
# use "def" to define a function, just like this function!
# call the function from functions_one()
# Hint: make sure you define it above this one

def my_second_function(a,b):
    assert_isInt(a)
    assert_isInt(b)

    return a*b

def functions2():
    return my_second_function(2,3)

# write a function named my_second_function
# have it return the product of a,b

def main():
    print(greet('Bob'))
    print(greet('Alice'))
    print(greet('X'))
    print(greet(26))
    input()
    return 0

if __name__ == "__main__":
    os._exit(main())
