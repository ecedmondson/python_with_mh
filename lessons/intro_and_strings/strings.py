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
print("Will this line print?")
# And it will not run unless you remove the '#'
# Exercise:
# A. Try to run this file and see if the code in line
#    13 will print. 
# B. Try removing the '#' before line 13 and running
#    this file again.
# C. Look up how to comment in another programming language.
#    For example, try C++. How does the comment syntax differ?

# MH:
#     in C++ comments are set apart by /* */ sandwiching the text.
#     CSS uses the same /* */.
#     in HTML, <!-- --> sandwich the text.

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

# MH:
#     ha! you hadn't actually defined "my_num", but "my_int" (line #35)

my_num = my_int

my_num + 5 > 12 # (because my_num is set to 7)
print(my_num) # > 7

# Be sure to distinguish the '=' assignment operator from the
# '==' comparison operator. '=' allows you to assign data to
# variable names, like in the examples above. '==' allows you
# to compare data, and will results in True or False.
# So, for example:
print(5 == 5) # > True
print(3 == 5) # > False

# There are rules for variable names in Python. Because they are instinctual for me
# I am including a link here for you to read about the rules:
# https://www.w3schools.com/python/gloss_python_variable_names.asp

# Exercise:
# A. An example above uses code that looks like print(5 == 5). What do you think will happen
#    if you changed to a single equal sign operator? Test out your prediction by running the
#    following line of code:
# print(5 = 5)
# MH:
#     i predict it will > 5
#     i was wrong. you cannot assign a variable inside a print?

# B. Define a variable called "num" Set it equal to any number value. Perform any mathematical
# operation on your variable. Leave that code in this file.
num = 3
print(num)
num = num * 2
print(num)

# C. Define a variable called "my_var". Set it eequal to any valid Python data type. Print the
#    variable. After the print, reassign the same variable name to any different valid Python data type.
#    What do you think will happen if you re-print the variable? Test your theory. 
# MH:
#     i accidentally sort of did this for 2.B, but i predict it will print whatever it was last defined as?
my_var = "dobby"
print(my_var)
my_var = 100.5
print(my_var)

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
my_char = "A"
# has a data type that is a string.
print(type(my_char)) # > str

# MH:
#     is it valid/common to put a comment at the end of a line (as in 109 above?)
#     i feel like no

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
my_letters_a = my_letters.find("a")
print("in", my_letters, ", a first appears at index", my_letters_a)

# B. Using the variable my_letters again and the find method again, find the first instance
#    of the letter 'a' from index 2 onward.
# PUT THE ANSWER TO B HERE
my_letters_a_2 = my_letters.find("a", 2)
print("after index 2, a first appears at index", my_letters_a_2)

# C. Using the variable my_letters again and the find method again, find the first instance
#   of the letter 'a' from index 11 through index 16. 
# PUT THE ANSWER TO C HERE
my_letters_a_11_16 = my_letters.find("a", 11, 16)
print("inclusively (i think, WRONGLY IT TURNS OUT) between indexes 11 and 16, a first appears at index", my_letters_a_11_16)


# D. Using the variable my_letters and the find method, try to find the letter 'z' which is not
#    in the string. What do you think will happen?
# PUT THE ANSWER TO D HERE
# MH:
#     the docs.python link tells me it will return "-1" if sub is not found
my_letters_z = my_letters.find("z")
print(my_letters_z)
# MH:
#     seems like it would be nicer to use an if?
#     and set it if the find returns an interger<0
#     then it prints "that letter is not found".

# E. There is a letter 'a' at index 10 in my_letters. What do you think will happen if you try
#    to find the letter 'a' at starting index 9 and ending index 10? Test it.
# PUT THE ANSWER TO E HERE
# MH:
#     i think the search is inclusive (see 3.C), so i think it will find a at 10...
my_letters_a_9_10 = my_letters.find("a", 9, 10)
print(my_letters_a_9_10)
# MH:
#     i was wrong. it returned -1. i guess it is not inclusive.
#     i'm also thinking i should have just used one variable, e.g. find, for A-E.

# F. Using the variable my_letters and the index method, try to find the letter 'z' which is not
#    in the string. What do you think will happen? Is this different ot find or not? 
# MH:
#     it will be different than find.
#     when the sub is not found, it "raises ValueError" instead of returning -1.
#     according to the docs.python link.

# index = my_letters.index("z")
# print(index)

# MH:
#     so....
#     find is useful when you want the code to tell you where and whether the sub is found.
#     index is useful if you need the code to stop if the sub isn't present.
#     i'm going to set lines 179&180, my answer to F, as comments
#     so it doesn't disrupt my running the code for the following answers.

# G. Below is declared a list data type. You need this to be one string. Use join on the list
#    to make it a human readable string.
my_list = ["Help!", "I'm", "stuck", "in", "a", "list", "and", "illegible."]
# PUT THE ANSWER TO G HERE
# MH:
#     i will be honest, i had to look at W3 for help with this.
#     my first tactic was my_list.join and then i got confused
separator = " "
join = separator.join(my_list)
print(join)

# F. Using my_list and the join method, join my_list using a line feed as a separator.
# PUT THE ANSWER OT F HERE
# MH:
#     i had to google line feed
separator = "\r\n"
join = separator.join(my_list)
print(join)

# H. Imagine that you scraped the following text data declared in web_data below off of a website.
#    The data seems correct to you, but has some strange spacing. Fix it with one function call.
web_data = "         For the low, low price of some cheese, you too can can get in on the nacho party.      "
# PUT THE ANSWER TO H HERE
strip = web_data.strip()
print(strip)

# I. Take the data in web_data and turn it into a list using the split function.
# PUT THE ANSWER TO I HERE
split = web_data.split()
print(split)

# J. Imagine you have a sentence which you scraped from a website. This data is represented below by scraped.
#     It seems correct but has strange
#    line feeds. You want to each line feed to be a space. Write code that will do this.
scraped = "When\nwill\nwe\nbe\free\nfrom\nthis\nwretched\ncold."
# PUT THE ANSWER TO J HERE
replace = scraped.replace("\n", " ")
print(replace)
replace = replace.replace("\f", " f")
print(replace)

# K. Imagine that someone else has solved J for you and is asking you to check over their work. This
#    person wants to print the updated my_letters to their screen to see the new changes. What
#    is wrong with the following solution?
#    my_letters.replace("\n", " ")
#    print(my_letters)
# PUT THE ANSWER TO K HERE
# MH:
#     two things are wrong,
#     first, they're performing the replace operation on the wrong variable, my_letters, not scraped
#     second, they've failed to correct the \f thingie?

# Remember that there was a little blurb about strings behaving like lists/arrays/sequences.
# The next exercise set will be about these properties.
