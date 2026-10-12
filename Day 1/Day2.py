'''
Topic: Common Escape Characters: in print() function(in-built)

eg:

print("My name is Yogesh\n I study in CSE branch")

\n      - start a new line
\"      - prints a double quote
\t      - adds a tab indent
\\      - prints a backslash
--> all of these are escape sequence
() --> these are called as parentheses
{} --> these are called as braces

Note: the input() function always returns the value in form of string as default.  During taking data from the console it considers the data in the string format & stores it also in the string format.

Note: Python can only add text to text values & integer to integer values, not text to integer values.
      For that specific operation we have a method to perform the gluing.

Topic: Building Dynamic Messages(Concatenation with plus(+)/Manipulate strings)

* Concatenation: The method of gluing the 2 strings values together with the help of + is called concatenation.

Ex:
first = "Hello"                 #first = variable, "Hello" = string
second = "World"
message = first + second        #+ performs concatenation to 2 string values
print(message)

*Concatenate, format, & calculate: (modern way of concatenation): It's done using f-string(formatted string). It can be used to combine 2 string values or even a string & integer values.

Ex:
name = "Yogesh"
print(f"My name is {name}")

Ex: 
age = 21
print(f"My age is {age + 1}")

Topic: Python String tools/operations: these are called as "Methods" that are built-in which we attach with a dot(.) to perform some operation on data from console prespective.

* .upper        - for all caps

Ex:
name = "yogesh"
name = name.upper()
print(name)

* .lower        - for lowercase

Ex:
name = "Yogesh"
name = name.lower()
print(name)

* .strip        - trims end's spaces(deletes spaces if there exists a space at the end of paragraph or sentence).

Ex:
name = "Yogesh "
name = name.strip()
print(name)

* .replace()    - swaps text

Ex:
name = "Yogesh"
name = name.replace("yogesh", "Yogesh")     #name.replace(old, new) format
print(name)

* len()         - counts characters in specificed location including spaces.

Ex:
name = "Yogesh"
len(name)

--> these all are called as string operations & used to format & manipulate text.
--> They just give a replica of the data in the console & most of them dont affect data when specifically not specified.

Topic: coding exercise done:

print("Hello user! Welcome to the Python tutorial")
name = input("Please enter your name: ")
print("Oh! nice to meet you ", name)
print(f"Oh! nice to meet you {name}")
color = input("Enter your favourite color: ")
print("Nice " + color + " is the most beautiful color")
age = input("What's your age now: ")
print(f"Oh! great you are already {age} tears old now")
print("-" *50)

'''