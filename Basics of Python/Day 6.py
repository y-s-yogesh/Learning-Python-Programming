'''
--> when you need to repeat an action you don't need to write the statement again & again.
--> A loop repreats a block of code automatically, making your program shorter & easier to maintain.
--> They repeat as long as a condition is true. (for, while, break, continue).

#for loop, which repeats a set number of times.
#while loop, which repeats as long as a condition is true.
# control loop behavior with break & continue.

** Loops: loops automate repetative tasks by running the same block of code again. 
--> Python gives you 2 choices a for loop - when you know the repetition & a while loop when repetition depends on condition.


--> How range works(start, stop, step): range can take a start value, stop value & a step.
eg: range(1, 10, 2)
    1-->3-->5-->7-->9-->ends the range

syntax: for i in range(5):  #i = 0,1,2,3,4
            print(i)
        
            
        Output: 0
                1
                2
                3
                4

                
* How while loop works: A while checks the condition before every repetition. If the condition statys trye everytime; python doesn't stop & freezes the program by infinite loop.

eg: count = 0
    while count<5:
        print(count)        #count=0,1,2,3,4
        count +=1

eg: health = 3
    while health > 0:
        print(f" Player is alive with Health: {health})
        health -= 1     #modify the condition so the loop will eventually stop

--> Choosing the right loop

--> Choose a for loop when:

--> You know how many times you want to repeat the action.
--> You want an automatic exit after a certain number of repetitions.
--> You want a counter variable to keep track of how many times the loop has run.

--> Choose a while loop when:

--> The total number of repetitions depends on a variable state.
--> You're waiting for something specific to happen before stopping the loop (e.g., user input).
--> You need control over when the loop stops, rather than a fixed number of repetitions.


* Break Statement: immediately ends a loop.
eg: for count in range(10):
        if count == 5:
            break           #exit loop, skip print
        print(count)
    print("Loop Ended")

#Break exits the loop early(it skips the next code after it's execution & enter's next condition)


* Continue: It skips the remaining code in a current iteration, then starts the next one.
eg: for count in range(6):
    if count == 3:
        continue
    print(count)

#continue bypasses the print statement but loop keeps running
#continue skips one iteration
#use continue when one iteration should be ignored without ending the while loop


* Break in while loop:

while True:
    user_input = input("Type 'exit' to stop the loop:")
    if user_input.lower() == "exit":
        break
    print(f"You entered : {user_input})
print("goodbye")

#break ends a while true loop


# Continue in a while loop needs extra care:

current_slot = 0
while current_slot < 5:
    current_slot += 1   #crucial: increments happen right at the start of the lap


    if current_slot == 3:
        print(f"skipping item slot {current_slot}")
        continue        #aborts the rest of this lap & jumps back to the top
        
    #This processing code is skipped when current_slot is 3
    print(f"Successfylly processed item in slot {current_slot}")
print("Inventory scan complete")

#Update the conditon before continue


* Loops can have else block:

color = "blue"
for i in range(3):
    user_input = input("Guess color")
    if user_input.lower() == color:
        print("You guessed it")
        break       #break reached: skip else
else: 
    print(f"Sorry, the correct answer is {color}")

#else runs only without break
'''