''' Types of Data:
1. Int          #whole numbers
2. Float        #decimal numbers
3. Complex      #real and imaginary numbers as examples 2+3j, 4-5j, -4, -4.25, 4X, 4X+3Y
4. String       #a sequence of characters quoted in single ''or double quotes""
5. Boolean      #True or False
6. List         #ordered and changeable collection
7. Tuple        #ordered and unchangeable collection
8. Dictionary   #unordered, changeable and indexed collection
9. Set          #unordered collection of unique items'''

'''Numeric Data Types:
* Int - Integer
* Float - Decimal Number
* Complex - Real and Imaginary Number'''

'''Text Data Types:
* String - A sequence of characters'''

'''Sequence Data Types:
* List - A collection of items which is ordered and changeable. Allows duplicate members.
* Tuple - A collection of items which is ordered and unchangeable. Allows duplicate members.
* Dictionary - A collection of items which is unordered, changeable and indexed. No duplicate members.
* Set - A collection of unique items which is unordered. No duplicate members.'''

'''Variables:
* Variables are containers for storing data values of any type. In Python, you do not need to declare the type of variable, it is inferred from the value assigned to it. It's like a college bag used to store different types of subject books(any subject book can be stored in the bag).
* Variable names can contain letters, numbers, and underscores, but cannot start with a number. They are case-sensitive.
* Using variables we can store, access, & modify the data values at any time.
* example: a = 10, b = 20, c = a + b, print(c) also Name = "Yogesh", Age = 20, print(Name, Age) are also examples of variables.'''

'''Comments:
* Comments are used to explain code and make it more readable. In Python, comments start with the # symbol. 
* Multi-line comments can be created using triple quotes ('''''' or """)'''

''' To take Input from user:
* The input() function is used to take input from the user. It always returns the input as a string.
* To convert the input to a specific data type, we can use type conversion functions like int(), float(), etc. For example, Age = int(input("Enter your age: ")) will take input from the user and convert it to an integer.
example: Name = input("Enter your name: ") will take input from the user and store it as a string in the variable Name.'''

'''To print output to the console:
* The print() function is used to display output to the console. It can take multiple arguments and will print them separated by spaces. For example, print("Hello", Name, "you are", Age, "years old.") will print the values of the variables Name and Age along with the text.
example: print("Hello", Name, "you are", Age, "years old.") will print the values of the variables Name and Age along with the text.
Name = input("Enter your name: ")     #Taking input from user
Age = int(input("Enter your age: "))   #Taking input from user and converting it to integer
print("Hello", Name, "you are", Age, "years old.")  #Printing the values of variables'''

'''Operators: an operator is a symbol that tells/helps the interpreter to perform specific mathematical, relational or logical operations/manipulations. Python divides the operators in the following groups:
* Arithmetic Operators - Used to perform mathematical operations like addition (+), subtraction (-), multiplication (*), division (/), integer division (//), modulus/modulo (%), and exponentiation (**).
* Assignment Operators - Used to assign values to variables (e.g., =, +=, -=, *=, /=, //=, %=, **=).
* Comparison/Relational Operators - Used to compare two values and return a boolean result (True or False). (e.g., equals to (==), not equals to (!=), greater than (>), less than (<), greater than or equal to (>=), less than or equal to (<=)).
* Logical Operators - Used to combine conditional statements (and, or, not).'''

'''selection control structures/statements: (Programming Constructs or Decision Making Statements or Control Flow Statements):-
* Control flow statements are used to control the flow of execution of the program based on certain conditions. The main control flow statements in Python are:
* if statement - Used to execute a block of code if a specified condition is true.
example:
a = 30
b = 20
if(a>b): print("a is larger value", a, b)

* if-else statement - Used to execute one block of code if a specified condition is true, and another block of code if the condition is false.
example:
a = 30
b = 20
if(a>b):
    print("a is larger value", a, b)
else:
    print("b is larger value", a, b)

* if-elif-else statement(multiple if's) - Used to execute one block of code among multiple conditions.
example:
a = 30
b = 20
c = 10
if(a>b and a>c):
    print("a is the largest value", a, b, c)
elif(b>c):
    print("b is the largest value", a, b, c)
else:
    print("c is the largest value", a, b, c)'''

'''Iteration control structures/statements: (Looping Statements or Repetition Control Statements or Iterative Control Statements):-Control flow statements are used to execute a block of code repeatedly based on certain conditions. The main control flow statements in Python are:
* for loop - Used to iterate over a sequence (like a list, tuple, dictionary, set, or string) and execute a block of code for each item in the sequence.
example:
a=[1,2,3,4,5,6,7,8,9,10]
for number in a:
    print(number)

example 2:
for number in 1,2,3,4,5,6,7,8,9,10:
    print(number)

*while loop - Used to execute a block of code repeatedly as long as a specified condition is true.
example:
while(a<=10):
    print(a)'''

'''Loop Control Statements: (Break, Continue, Pass)
* break statement - Used to exit the loop prematurely when a certain condition is met.
* continue statement - Used to skip the current iteration of the loop and move to the next iteration.
* pass statement - Used as a placeholder for future code. It does nothing when executed.'''

'''Collections: are used to store multiple items in a single variable or used to group the data/information & store them together.
*Different types of collections in python are: 
1. List
2. String
3. Set
4. Dictionary
5. Tuple

* List - A collection of items/elements which is ordered and changeable. Allows duplicate members. Lists are defined using square brackets [] & Separated by commas. Here each item in the list is called an element. Lists can contain elements of different data types like integers, strings, floats, etc. Lists are mutable, meaning we can change their content without changing their identity.
* Indexing in lists starts from 0 for the first element, 1 for the second element, and so on. Negative indexing is also allowed, where -1 refers to the last element, -2 to the second last element, and so on.
example: 
Attendancelist = [1, 2, 3, 4, 5]

len(Attendancelist) #will return the number of elements in the list, which is 5.
Attendancelist[0] #will return the first element of the list, which is 1 with index 0.
Attendancelist[-1] #will return the last element of the list, which is 5 with index -1.
Attendancelist[4] #will return the fifth element of the list, which is 5 with index 4.
Attendancelist.append(6) #will add the element 6 to the end of the list.

#Adding 2 lists together using the + operator will concatenate them, creating a new list that contains all the elements from both lists.
example:
Attendancelist1 = [1, 2, 3]
Attendancelist2 = [4, 5, 6]
Attendancelist3 = Attendancelist1 + Attendancelist2 #will create a new list Attendancelist3 which contains [1, 2, 3, 4, 5, 6].

#List slicing is a technique used to extract a portion of a list by specifying a range of indices. The syntax for slicing is list[start:end], where start is the index of the first element to include, and end is the index of the first element to exclude. If start is omitted, it defaults to 0, and if end is omitted, it defaults to the length of the list.
example:
Attendancelist = [1, 2, 3, 4, 5]
Attendancelist[1:3] #will return a new list containing elements at indices 1 and 2, which is [2, 3].
Attendacelist[:3] #will return a new list containing elements from the beginning up to index 2, which is [1, 2, 3].
Attendacelist[2:] #will return a new list containing elements from index 2 to the end, which is [3, 4, 5].

* String - A collection of characters which is ordered and unchangeable. Strings are defined using single or double quotes.
example:
Name = "Yogesh"
Name[4] #will return the character at index 4, which is 's' or accessing the 4th alphabet in the name ''Yogesh''.
Name.upper() #will return the string in uppercase, which is 'YOGESH'.
Name.lower() #will return the string in lowercase, which is 'yogesh'.

* Set - A collection of unique items which is unordered. Sets are defined using curly braces {} or the set() function. Sets do not allow duplicate members and are mutable, meaning we can add or remove elements from a set.

set representation: Rollno = {1, 2, 3, 4, 5}
music = {1,2,3}
yoga = {3,4,5}

union of 2 sets:

Rollno.union(music | yoga) #will return a new set containing all unique elements from both sets, which is {1, 2, 3, 4, 5}.
Rollno.intersection(music & yoga) #will return a new set containing only the elements that are present in both sets, which is {3}.
Rollno.difference(music - yoga) #will return a new set containing the elements that are present in Rollno but not in music, which is {4, 5}.

To add an element to a set, we can use the add() method. 
For example, 
Rollno.add(6) will add the element 6 to the Rollno set. #output will be {1, 2, 3, 4, 5, 6}.
To remove an element from a set, we can use the remove() method.
For example,
Rollno.remove(5) will remove the element 5 from the Rollno set. #output will be {1, 2, 3, 4}.

Rollno.union(music) #will return a new set containing all unique elements from both sets, which is {1, 2, 3, 4, 5}.
intersection of 2 sets: Rollno.intersection(music) #will return a new set containing only the elements that are present in both sets, which is {1, 2, 3}.
'''

'''
*Tuple - A collection of items which is ordered and unchangeable. Tuples are defined using parentheses () and separated by commas. Tuples can contain elements of different data types like integers, strings, floats, etc. Tuples are immutable, meaning we cannot change their content after creation.
example:
vegetables = ("carrot", "potato", "onion")

Accessing elements in a tuple is similar to lists, using indexing and slicing. Indexing starts from 0 for the first element, 1 for the second element, and so on. Negative indexing is also allowed, where -1 refers to the last element, -2 to the second last element, and so on.
example:
vegetables[2] #will return the third element of the tuple, which is 'onion'.

To add or combine a tuple:
combo = vegetables + vegetables #output will be ('carrot', 'potato', 'onion', 'carrot', 'potato', 'onion').
'''

'''Dictionary - A collection of items which is unordered, changeable and indexed. Dictionaries are defined using curly braces {} and consist of key-value pairs. Each key is unique and is used to access its corresponding value. Dictionaries are mutable, meaning we can change their content by adding, modifying, or removing key-value pairs.
example:
Student_marks = {"Yogesh": 90, "Ramesh": 85, "Suresh": 95}
print(Student_marks) #will output the entire dictionary: {'Yogesh': 90, 'Ramesh': 85, 'Suresh': 95}.

#The name of the student is the key & marks is the value.

Accessing values in a dictionary is done using the keys. We can use square brackets [] or the get() method to access the value associated with a specific key.
print(Student_marks["Yogesh"]) #will output the value associated with the key 'Yogesh', which is 90.

Adding or modifying key-value pairs in a dictionary is done by assigning a value to a key. If the key already exists, its value will be updated; if the key does not exist, a new key-value pair will be added.
Student_marks["Ramesh"] = 88 #will update the value associated with the key 'Ramesh' to 88.
Student_marks.update({'Yogesh':100}) #the output will be {'Yogesh': 100, 'Ramesh': 88, 'Suresh': 95}.'''