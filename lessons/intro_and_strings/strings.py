# INTRO
# This is intended to be an introduction to strings.
# On account of the fact that this is also the first
# Python file I've ever used to interact with you, there
# will also be additional little snippets explaining what
# I'm doing.

# 1. COMMENTS
# This is a comment. Comments in Python
# are always preceded by the '#' symbol.
# Comments don't "run" as part of code.
# So, for example, I have the following line of code
# print("Will this line print?")
# And it will not run unless you remove the '#'
# Exercise:
# A. Try to run this file and see if the code in line
#    13 will print. 
# B. Try removing the '#' before line 13 and running
#    this file again.
# C. Look up how to comment in another programming language.
#    For example, try C++. How does the comment syntax differ?

# 2. VARIABLES (And equal signs)
# Variables are a human readable way to maintain
# and reuse data within programs. Variables work by
# associating a name with a data object. In Python, variables
# are very easy to create. For example, the following lines
# are all variables

my_int = 7
my_float = 1.5
my_string = "Hello Dobby. How are you?"
my_list = [1, 2, 3, 4, 5, 6, 7]
my_dictionary = {"a": "A", "b": "B", "c": "C"}

# This isn't an exhaustive list of all the data types in Python
# (this is impossible as you can make your own data types too)
# but variable assignment always works in this way. That is,
# name equalsign data.

# When you assign data to a name, and use that name, you are
# actually using the data associated with that name. For example:

# my_num + 5 > 12 (because my_num is set to 7)
# print(my_num) > 7

# Be sure to distinguish the '=' assignment operator from the
# '==' comparison operator. '=' allows you to assign data to
# variable names, like in the examples above. '==' allows you
# to compare data, and will results in True or False.
# So, for example:
# print(5 == 5) > True
# print(3 == 5) > False

# There are rules for variable names in Python. Because they are instinctual for me
# I am including a link here for you to read about the rules:
# https://www.w3schools.com/python/gloss_python_variable_names.asp

# Exercise:
# A. An example above uses code that looks like print(5 == 5). What do you think will happen
#    if you changed to a single equal sign operator? Test out your prediction by running the
#    following line of code:
# print(5 = 5)
# B. Define a variable called "num" Set it equal to any number value. Perform any mathematical
# operation on your variable. Leave that code in this file.
# C. Define a variable called "my_var". Set it eequal to any valid Python data type. Print the
#    variable. After the print, reassign the same variable name to any different valid Python data type.
#    What do you think will happen if you re-print the variable? Test your theory.  

# 3. STRINGS
# I am defining a variable called 'my_sentence'
# and setting that variable equal to this sentence.
# This sentence is an example of a data type called
# a string. The string data type is made up of a sequence
# of characters and is usually used to manage textual data.

my_sentence = "JJ Flewellen is super cute."

# In many programming languages, there is a separate char data type
# to refer to characters. This data type doesn't exist in Python.
# So, for example, even this variable declaration:
# my_char = "A"
# has a data type that is a string.
# print(type(my_char)) > str

# It's important, I think, to remember the history of programming languages here.
# In many languages with a char data type, the string data type is actually what
# is known as an array (or list, in Python arrays are called lists). Strings, then,
# are a special implementation of the array data type in many languages. Since
# Python does not have a char data type, this implementation detail is not
# as important. However, it is important to remember that strings are sequences/arrays/lists
# of characters because this gives us insight into what kinds of properties strings have.

# Here is a link to the string methods documentation for Python 3.9:
# https://docs.python.org/3/library/stdtypes.html#string-methods
# You can read all of it, if you want, but I recommend reading about 
# these methods for the String exercise:
# find, index, join, strip, replace, split
# Exercise:
# A. Below is declared a variable called my_letters. Using the 'find' method, 
#    write code that will find the first index of the letter 'a' in my_letters.
my_letters = 'abcdefghabalmnoap'
# PUT THE ANSWER TO A HERE
# B. Using the variable my_letters again and the find method again, find the first instance
#    of the letter 'a' from index 2 onward.
# PUT THE ANSWER TO B HERE
# C. Using the variable my_letters again and the find method again, find the first instance
#   of the letter 'a' from index 11 through index 16. 
# PUT THE ANSWER TO C HERE
# D. Using the variable my_letters and the find method, try to find the letter 'z' which is not
#    in the string. What do you think will happen?
# PUT THE ANSWER TO D HERE
# E. There is a letter 'a' at index 10 in my_letters. What do you think will happen if you try
#    to find the letter 'a' at starting index 9 and ending index 10? Test it.
# PUT THE ANSWER TO E HERE
# F. Using the variable my_letters and the index method, try to find the letter 'z' which is not
#    in the string. What do you think will happen? Is this different ot find or not? 
# G. Below is declared a list data type. You need this to be one string. Use join on the list
#    to make it a human readable string.
my_list = ["Help!", "I'm", "stuck", "in", "a", "list", "and", "illegible."]
# PUT THE ANSWER TO G HERE
# F. Using my_list and the join method, join my_list using a line feed as a separator.
# PUT THE ANSWER OT F HERE
# H. Imagine that you scraped the following text data declared in web_data below off of a website.
#    The data seems correct to you, but has some strange spacing. Fix it with one function call.
web_data = "         For the low, low price of some cheese, you too can can get in on the nacho party.      "
# PUT THE ANSWER TO H HERE
# I. Take the data in web_data and turn it into a list using the split function.
# PUT THE ANSWER TO I HERE
# J. Imagine you have a sentence which you scraped from a website. This data is represented below by scraped.
#     It seems correct but has strange
#    line feeds. You want to each line feed to be a space. Write code that will do this.
scraped = "When\nwill\nwe\nbe\free\nfrom\nthis\nwretched\ncold."
# PUT THE ANSWER TO J HERE
# K. Imagine that someone else has solved J for you and is asking you to check over their work. What
#    is wrong with the following solution?
#    my_letters.replace("\n", " ")
# PUT THE ANSWER TO K HERE
