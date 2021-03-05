# # INTRO
# In the intro lesson we went over the basics of the
# string data type, used to represent textual data, and
# some of the things that make strings unique in Python.
# This lesson will include some more properties of strings
# ordered towards understanding the data type even more.
# In order to do this, we are going to look first at functions.

# #1. FUNCTIONS
# Functions in programming are self-contained scopes of code
# designed to accomplish a specific, limited, and clearly defined
# action. Functions frequently have input data, processing, and
# output data. Put in linguistic terms, functions relate and translate
# inputs to outputs.

# Not all functions in programming are obviously and explicitly
# mathematical (side note: there is a whole application of algorithmic
# studies that represents non-explicitly mathematical functional
# relationships and expresses them in mathematic terms. If you 
# are interested in this, google 'NP Completeness'), but the basic
# premise of mathematical functions can help illustrate the relationship
# between inputs and outputs in programming functions as well.

# For example, the following line gives an example of a simple
# function that might appear in grade school math:

# f(x) = x * 2

# The input in this function is x. The output is the calculated
# value of x * 2 and the function is the relationship between that
# input and that output. If the input is 1, then then output is 2;
# if the input is 2 then the output is 4 and so on and so forth. The
# function can be abstracted into the format above because the function
# represents a stable relationship: whatever the input to the function,
# the output will always be transformed in a stable way (in this case,
# multiplied by 2). 

# The same basic concept can be represented in Python. Functions are very
# easy to define in Python, though the format is different than above. Every function in
# Python, at the most basic, is defined with a header that takes this format:

# def function_name(arg1, arg2):
#     # code goes here for function scope

# The keys to note here in the syntax are these:
#     - the def keyword: always lowercase 'def' and never 'Def'; def
#       indicates the definition of a new function
#     - function name: the function name can be roughly anything within
#       reason with certain rules applied. Please cross reference the Pep8
#       guide on naming. https://www.python.org/dev/peps/pep-0008/#function-and-variable-names
#     - arguments: arguments are always enclosed within parentheses. There is theoretically
#       no limit to how many arguments you can pass, but the more arguments, the more complex
#       a function. The more complex a function, the easier it is to make mistakes and the harder
#       it is to have a function do just one thing. Arguments can be named anything within reason.
#       Please cross reference Pep8 on naming conventions. Functions call also take zero arguments.
#     - the closing colon: this colon after the closing parentheses is required. You will raise
#       a syntax error without it.

# Given this format, if I wanted to write a Python function that took in two integer arguments,
# multiplied them together, and then subtracted 5 and returned the output, it would look
# something like this:

def multiply_and_subtract_five(num1, num2):
    return ((num1 * num2) - 5)


# The only new syntax in this example is that 'return' keyword. The 'return' keyword is
# what allows Python functions to to make available the output of the relationship outside
# the scope of the function definition.

# In order to use a function in Python code, the function must be "called", which means that
# the function is provided with appropriate input and syntax is specified on the function
# in such a way that the input can be validly related to output. What does that mean? Let's
# look at an example. 

# Say I have a function that takes no arguments like this one:

def my_cool_function(pet_name):
    return f"{pet_name} is a cool pet."

# The correct way to call this function is this syntax:

# my_cool_function("JJ")

# The following would be incorrect:

# my_cool_function()
# my_cool_function("JJ", "Dobby")
# my_cool_function(cat="JJ")
# my_cool_function: "JJ"
# ...etc.

# All of those would provide you with errors. As a final note, simply
# calling 'my_cool_function("Dobby")' would not maintain the correct
# output in state, even though it is a valid function call.  
# The output must be used in some way, or assigned to 
# a variable in order to be used at a later time. Thus, both of these
# are valid:

# sentence = my_cool_function("Dobby")
# print(sentence) # > "Dobby is a cool pet"
# print(my_cool_function("Dobby")) # > "Dobby is a cool pet."

# And while this is valid, the output is not used in any way
# discernible to the program or programmer:

# my_cool_function("Toby")

# Exercises:
# A. Use the function named multiply_and_subtract_five. Given that num1 is equal to 7 and num2 is 3,
#    what do you expect the output of the function to be? Call the function and test it.
# # ANSWER A GOES HERE
# # # MH guess: (7*3)-5=16
# # ANSWER A CODE GOES HERE
print("the answer to exercise 1A is:",multiply_and_subtract_five(7,3))
print("the answer to exercise 1A is: {}.".format(multiply_and_subtract_five(7,3)))

name = "Emily"
food = "tacos"
print("{} would like to eat some {}".format(name, food))

print("{name} would like to eat some {food}.")
# # # MH why isn't this f-string working?

# B. Look at the following function definition  and subsequent code and then 
#    predict what will be printed by the print function. Uncomment the code
#    and test your prediction.

def is_double_digits(number):
    number = abs(number)
    return number >= 10 and number <= 100
 
print(is_double_digits)

# # ANSWER B GOES HERE
# # MH prediction:
# # it ensures the number is positive by giving the absolute value of the number,
# # then you can see if it is between 10 & 100
# # (where the latter is inclusive and the former is not?)
# # and you get a yes if it is?
# # 
# # except... what is it doing to print the function without giving it any input?
# # ran it & got:
# # <function is_double_digits at 0x7fdc4e268820>

print(is_double_digits(4))
# # 10 gives me a "True"
# # 4 gives a "False"

# C. Practice learning to read code. Based on reading the function name and code definition
#    of is_double_digits, what do you think the the function call abs(arg) does? 
# # ANSWER C GOES HERE
# # MH: oh, i was too quick. i guessed absolute in 1B, but i then Googled to confirm

# D. Imagine that someone has asked you to write a function that will determine if 
#    a number is negative or positive. Your function should return a Boolean data type
#    (i.e. either return True, return False, or an expression that evaluates to a boolean,
#     for example, return 5 < 7) indicating if the number is positive or negative. It should
#     return a string that says "Neither" for 0 values. Write that function below. It should be named 
#     is_number_positive. You may want to google python if statements to finish this function. 

# # ANSWER D GOES HERE

def is_number_positive(number):    
    if number == 0:
        return "Neither"
    return number >=1

print(is_number_positive(0))
        


# 1.5 A clarification on scope
# The word scope was used to refer above in a way that denoted a limiting
# of functional relevance. Scope is a fairly important concept in programming
# so let's consider scope briefly.

# Scope refers to the availability of a defined variable, object or function
# within a program. Things that are defined inside of functions, for example,
# are limited to the scope of that function. This scope is generally referred to as
# the "local" scope. Things that are defined generally within a file are referred
# to as within the global scope. Availability of defined objects narrows correlating
# with definition. That is to say, things that are defined on a global level are 
# available in more narrow scopes because the local scope inherits the global scope.
# But the global scope won't inherit the local scope in return. 

# So for example, let's consider this code:

NAME = "ED"

def name_func():
    print("I am inside the scope of name_func")
    print("I am going to print NAME, then redefine, defined a new variable, then print again.")
    global NAME
    print(NAME)
    NAME = "SAK"
    other_variable="asdfasdf"
    print("this is the NAME variable: ", NAME, "; but this is the other_variable:", other_variable)

print("I am going to call name_func")
name_func()
print("I am now back on the global scope.")
print(NAME)
# # print(other_variable)

# Let's define this code in terms of scope terminology:
#     - NAME: this is a global variable. It can be accessed
#             on the global scope and is accessed on 
#             the global scope by the print function. It is
#             also available  
#     - name_func: this is a function and much like the variable
#                  NAME it has a global scope
#     - other_variable: this is a variable whose scope is local
#                       to the function name_func. It is not
#                       available globally and it's existence
#                       "ends" after name_func is called and 
#                       the local scope no longer exists.

# Exercises
# A. What is the value of NAME before name_func is called. What are the values of NAME inside the
# name_func local scope? Will the change to NAME persist when the name_func scope ends? Write
# your predictions and test them.  Uncomment the code above and run it.  
# # ANSWER TO A GOES HERE
# # MH: before name_func is called, Name = "ED"
# # inside name_func, Name is redifined to "SAK",
# # but once we are outside name_func,
# # Name will revert to "ED"

# B. Given the following code, list all names that will be available at the global level.

var1 = "JJ Flewellen"

def cool_func():
    var2 = "CAT"
    def inner_func():
        print("I am the inner")
    return "cool"

# Please list the globally available names in this list, with comman separation and quotes
# i.e. like this STUFF = ["FIRST THING", "SECOND THING", "ETC"]

GLOBAL_NAMES = ["var1", "cool_func"]
# # cool_func added after failing test.py.
# # SHOULD HAVE BEEN RUNNING THE TEST, because until this moment i had not realized that
# # functions define a variable. that's how the return works?
# # # putting this here instead of just the pull request: names can be defined as a function or a variable?

# 3. Iterable Properties of Strings
# An iterable in Python is any data structure that contains data as a collective and where
# the individual components of that collective can be accessed one at a time. From the last
# lesson we learned that strings used to be represented as an array/list data type made up of
# individual char data types. We also learned that this is not technically the case in Python,
# as the string is a dedicated and official data type, but the properties of this representation
# mean that strings in Pythons are iterables. 

# Let's consider for example the following string:

my_string = "abcdefghijklm"

# The entire string is one object. What this means is that each individual part of the string
# is not a separate object from the whole. So 'a', the first letter in the string, is not an entirely
# separate data entity from the next letter b. However, strings are also made up of individual component
# parts. The Python builtin function call len() returns the number of individual component parts in an iterable.
# For the variable my_string, this means that len() will return how many characters are present in the string:

num_letters = len(my_string)
print(f"There are {num_letters} total letters in the variable my_string.")


# 'Indexing' is the word used to refer to accessing one member of an iterable by referencing that member's position within the iterable.
# All indexes in Python start at 0 (that is, you start counting 0, 1, 2, 3 etc. and NOT 1, 2, 3, etc.). Indexing allows
# us to access the individual parts. Be careful not to confuse this! The total number of individual components is always
# one more than the numerical value of the final index on account of starting with zero. That is, given a string with four letters
# called 'letters', accessing the fourth and final letter should be done with index 3.

first_letter = my_string[0]
print(first_letter)
last_letter = my_string[12]
print(last_letter)

# What do you predict first_letter will be when printed? Last letter? Uncomment the code and test it. 
# # first will be "a"
# # last will be m

# There is a similar idea to indexing called slicing. Slicing allows us to take subparts of strings based on indexes.
# Consider the following string:

names = "Ed Mad Dob JJ"
mad = names[3:6]
print(mad)

# Much like with the find() str method, the first index is inclusive and the last index is exclusive, which is why,
# even though the 'd' in Mad is at index 5, the slice goes through index 6.

# What do you think these will print? Write your predictions then test the code.
# # "Dob JJ"
# # i have idea about these negatives? because the index starts at zero...
# # maybe "Ed Mad"
# # "Ed"?

print(names[7:])
print(names[:-7])
print(names[-2:])

# # ah, so negative indexes count from the right!

# In the above example, variables are set to equal the indexed value of certain positions in my_string. iterables
# can also be "unpacked," that is, correlated with names on index basis. Consider the much shorter string "short":

short = "xyz"

first, middle, last = short
print(first)
print(middle)
print(last)

# What do you predict will happen when short is unpacked into the individual variables first, middle and last? 
# # will it distribute the list into three separate lists?

# Uncomment the code and test it. 

# Sometimes in code we want to use all individual components of an iterable on a case by case basis
# without caring about what the numeric value of the component's index is. Consider for example, if you
# needed to take every letter of my_string, capitalize it, and then print that capitalized letter. To
# solve this problem you want to be able to access every single index, but it doesn't matter in particular
# what the index happens to be. That is to say, something like this would be exhausting to code and very brittle:

# total_letters = len(my_string)
# current_index = 0
# while current_index < total_letters:
#   capitalized = my_string[current_index].capitalize()
#   print(capitalized)
#   current_index = current_index + 1

# That code works, but it is significantly more complex than it needs to be. The current_index variable is only
# being using to keep track of where you are; it isn't particularly useful otherwise. Situations like these benefit
# from the use of what is called a for loop. Consider this much cleaner code:

# for letter in my_string:
#     print(letter.capitalize())


# Before looking at some Python builtin functions that operate on iterables, let's consider a special case: the empty string.

empty_string = ""
non_empty_string = "abc"

# An empty string has type str, the same as a non-empty string:

print(type(empty_string))
print(type(non_empty_string))

# Like other strings, an empty string is an iterable which has a length property referring to how many individual
# components make up the string. An empty string simply happens to have zero individual components

print(len(empty_string))

# These properties of empty strings, while somewhat of an edge case, are fairly easy to deduce based on everything
# else we have learned about strings. However, in Python any object (including, but not limited to, strings) also has a truthiness value.
# What this means is that non-Boolean objects (i.e. things like strings, integers, floats, dictionaries, etc. Booleans, if you recall from
# earlier, are True and False) can evaluate to True or False under certain circumstances. 

# Let's consider some data types we're already familiar with: strings and integers. In this example we are going to take data
# and typecast that data (typecasting is to transform one piece of data into a different type) into a Boolean. 

zero = 0
negative = -1
positive = 1
empty = ""
non_empty = "JJ Flewellen"

print(bool(zero))
print(bool(negative))
print(bool(positive))
print(bool(empty))
print(bool(non_empty))

# Based on previous examples we should be able to predict what will happen if we print one of these variables
# without the bool() typecast function call (i.e. print(zero) will print 0). The bool() typecast call will convert
# these values into either True or False. Before reading the next paragraph, what do you predict the truthieness
# value of each of these variables will be?

# # so... i have no idea.

# If you predicted that zero, negative and empty would be False and positive and non_empty would be True, then you are
# correct. Empty-strings are falsey values. This allow us to use individual objects in truthiness statements like this:
# # NOPE, only zero and empty are false; any number and anything nonempty are true.

# my_str = ""

# if my_str:
#     print(f"The first letter of my_str is {my_str[0]}")

# Do you predict that the sentence will be printed? Uncomment the code and find out.
# # the if will come out false (because empty strings are falsey), so nothing will print.

# With all of this, we can finally look at some function methods that work on strings qua iterables. These
# functions will work on other iterables we will learn about in future lessons, so be careful not
# to associate these functions _only_ with strings. They are functions for iterables.

my_random_chars = "l;k2;34lksd;lkfg"

sorted_chars = sorted(my_random_chars)
any_truthiness = any(my_random_chars)
all_chars_truthy = all(my_random_chars)
min_char = min(my_random_chars)
max_char = max(my_random_chars)

# - sorted(): takes in an iterable and returns a list with the individual components sorted
#             from least to greatest. With text data, the sorting is based on the corresponding
#             ordinal value of the Unicode character. (Try to run ord('x') and chr(120) in your python shell)
# - any(): takes in an iterable and returns a Boolean indiciating if any individual component
#          of that iterable is Truthy. In the case of strings, since only non-empty strings
#          are False, any('string') will almost always return True
# - all(): takes in an iterable and returns a Boolean indicating if each and every individual component
#          of that iterable is Truthy. Same caveat for strings as any()
# - min(): takes in an iterable and returns the individual component of that iterable with the minimum
#          value. In strings, this is based on the ordinal value of the Unicode character.
# - max(): takes in an iterable and returns the individual component of that ierable with the maximum
#          value. In strings, this is based on the ordinal value of the Unicode character.

# Exercises:

# Instructions: write all functions at the bottom of this file. If a function name is specified, use
# that function name. You may benefit from using some of the string methods learned in lesson 1/intro.
# You may write helper functions (i.e. a function that you call from inside your own function) but
# these helper functions will not be directly tested so it is up to you to ensure they work correctly.

# 1. Write a function that takes a string, sorts the characters in the string, and returns a string
#    with the individual characters sorted. Name this function sort_chars.

def sort_chars(string):
    string_sorted = sorted(string)
    string_sorted = "".join(string_sorted)
    return string_sorted

print(my_random_chars, "sorted is", sort_chars(my_random_chars))
print("{my_random_chars} sorted is {sort_chars(my_random_chars)}")
# # # MH what's wrong with my f string?

# # i realized this literally returns e.g. 'the total length of the string', 'l;k2;34lksd;lkfg', 'is', 16
# # how do i have it return e.g. the total length of the string l;k2;34lksd;lkfg is 16

# # # this seems to be why it is failing test.py
# # # i think i fixed it, by just pulling the commentary out of the function and into the print.

# 2. Write a function that takes a string and returns the value of the character at the index which is
#    half of the total length of the string  if the string is even,
#    the value of the penultimate character if the string is odd, 
#    and 'Dobby' if an empty-string or length 1. Name this function dobby_search.

def dobby_search(string):
    if len(string) <= 1:
        return "Dobby"
    elif (len(string) % 2) == 0:
        return string[len(string)//2]
    else:
        return string[len(string)-1]
    return "Dobby"

print(dobby_search(my_random_chars))
print(dobby_search(''))

# # # this one is failing the test, but i am not sure why.

# 3. Write a function that takes in a string and return the ordinal value of the minimum char in the string
#    or -1 if it is an empty string. Name the function min_to_ord.

def min_to_ord(string):
    if not string:
        return -1
    return ord(min(string))

print(min_to_ord(my_random_chars))


# 4. Write a function takes in a string and returns the ordinal value of the maximum char in the string
# or -1 if it is an empty string. Name the function max_to_ord.

def max_to_ord(string):
    if not string:
        return -1
    return ord(max(string))

print(max_to_ord(my_random_chars))

# 5. Write a function that takes in two arguments: the first a string and the second a character. Return
# how many times that character is found in the string. Name the function char_count.

def char_count(string, char):
    char_count = 0
    for characters in string:
        if characters == char:
            char_count = char_count + 1
        else:
            char_count = char_count
    return char_count

print(char_count(my_random_chars, "2"))


# 6. Imagine that you are scraping text data from the internet and want to print that data to your console. 
#    Write a function that takes one argument, the data, and will return the data with all extra space stripped 
#    away if any data is found and which returns "No data found!" if no data was found from scraping the internet. 
#    Name the function pretty_format.

def pretty_format(string):
    if not string:
        return "No Data Found!"
    return string.strip()

print(pretty_format(my_random_chars))
print(pretty_format(empty))
print(pretty_format("         For the low, low price of some cheese, you too can can get in on the nacho party.      "))


