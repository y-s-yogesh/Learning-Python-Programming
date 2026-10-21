'''
** Decision Making in Python:

* Boolean Values: A boolean "bool" is a data type with exactly 2 values (True/False).
--> They are case-sensitive & should be written exactly as it's defined in python.
    True/False.

* Comparison Operators: Compare two values & returns a boolean result. 
--> (== equals to, != not equals to, > greater than, < lesser than, >= greater than or equal to, <= lesser than or equal to).

* String comparison: To check if two strings are equal or not.
--> we can even compare alphatetically to see which comes first alphabetically.
--> They are case-sensitive by default; so, capital letter F != to small letter f.

product_a = "10 Flowers"
product_b = "1 flowers"

print(product_a == product_b)   #false
print(product_a > product_b)    #true

--> single '=' assigns a value
--> double '==" compares values


* if, else, elif: These are conditional flow statements(conditonal logic)
--> if runs when a condition is true.
--> else runs when a conditon is false.
--> elif runs when some extra conditons are true.

@if first match wins, then others are skipped.
--> Always make sure to order your conditions from most specific to least specific ones. If not then the least specific condition will get true(executed) & most specific condition may get skipped. 


* not, and, or(logical operators):
example: if not office_closed:
         print("Office open")

         if not office_closed and not office_weekend
         print("Office officially open")

--> use parenthesis if you want a specific sequence of running the operators.
--> Python runs the code inside parenthesis first & outside part later.

'''