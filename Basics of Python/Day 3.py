'''
--> In Python we store information in variables. A viariable is just a "labelled contrainer" that holds a value in memory & that you get to choose the label.
--> you could put a number in it, A piece of text, a decimal, or something else entirely. And whenever you need that value later; you just call it by the name.
--> In some languages you need to initially declare what type of data is that variable holding but, in python it figures it out automatically & use it at any time.


* Dynamic Typing:

Dynamic Typing means that you don't have to tell python on what type of variable is getting stored in it. Python figures it out automatically & re-assigns it a new value later & python quietly adjusts it's data type for you if necessary.

--> Python always looks at the value at the right side first & then puts it into a container on the left. (I assume that this is for in the time of assigning the values & not during running any loops or iteration statements).

------> "Right to Left rule": Container <------------- Interprets the data type <------------- looks at the values


--> At any point of time if we want to see what kind of type the varialbe is holding, we can type the below syntax to know the data type of the variable:

Syntax: type(variable)              # type() is a built in function in Python used to retrieve the data type.

print(type(variable))
<class 'str'>               #Output

# Modulo Operator(an arithmetic operator): is mainly used to check whether the number if olld or even as it returns remainder value or leftover value.

# Exponent operator(**): we use two stars (**) for power operations.
Example: a = 2**3       # output = 8 (as 2*2*2 = 8)


* Python Follows "PEMDAS" rule: 
Example: 

result1 = 2+3*4         # output = 14 (as it followed PEMDAS rule)
result2 = (2+3)*4       # output = 20 (as we wrapped it with parentheses & made own sequence to execute)

--> () With parentheses we can control the execution sequence.
--> without parentheses we can't control the execution as it follows PEMDAS rules for Mathemetical operation.
--> Use parentheses if you actually want to run something in a sequence & especially while arithmetic operations.



* Mixing integers & float: Int + float = float (as python doesn't want to loose the decimal precision & hence float dominates while adding it with a integer values).

Example:

result1 = 5+2
result2 = 5+2.5
print(result1, result2)
print(type(result1), type(result2)) 

#Output: 
7
7.5
<class 'int'>
<class 'float'>             # it automatically converted the output to float data type but, later it can be trimmed.

------------> Preserves decimal precision ------------> Automatic Convertion


* Don't divide by zero: 

Dividing numbers by zero will cause your program to crash. As Python doesn't allow it. If you try then Python returns "Zero division error message".


* Type Casting: 

As a default feature, Python always set's the data type to text when a value is assigned by user from console & in order to change it's type during assigning a value the concept of "Type casting" comes into frame, where we override the default option of the data type from string - int/float/comples.

* Casting = converting from one type to another.

---> Three main built-in converters:-

1. int() for whole numbers. eg: age = int(input("What's your age"))
2. float() for decimal numbers. eg: cgpa = float(input("What's your cgpa"))
3. str() for text data. eg: name = str(input("What's your name"))

* Wrap or nest:

1. wrap = two steps; 
eg: raw = input("age")
    age = int(raw)

2. nest = one line;
eg: age = int(input("Age?))

Input runs--------------> int wraps --------------> age is stored ----------- (left to right rule)

* Limits of convertion:

--> Non numeric text can't be parsed; eg: name = int(input(""))
--> Python won't drop the decimal for you; eg: gpa = int(input(#may be 9.5))

* Rule of Thumb:

--> If a decimal is possible, use float()
--> float() can be converted into int() later.
--> Python rounds down; chops the decimal - when decimal is converted into int.
--> eg: int(3.6) # equals to 3 when converted.

'''