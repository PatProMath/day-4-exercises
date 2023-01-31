import random

random_integer =  random.randint(1,20)
print(random_integer)

random_float =  random.random()
print(random_float)

# seed = random.seed(40)
print(random.randint(1, 50))

""" Coin Toss """
# In the code above in lines 9 was not commented out, the output (i.e state) stays the same no matter how many times, you try the Coin Toss! It also affects line 10.
toss = random.randint(0,1)

if toss == 1:
    print("Heads")
else:
    print("Tails")

"""Banker Roulette"""
names_string = input("Give me everybody's names, separated by a comma. \n")

names_list = names_string.split(", ")

num_of_names = len(names_list)

random_choice = random.randint(0, num_of_names - 1)

person_to_pay = names_list[random_choice]

# person_to_pay = random.choice(names_list) 
# The choice function reduces 4 lines of  code to just 1.
print(person_to_pay + " is going to pay for everyone's meal!")

"""Nested Lists"""
dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

print(len(dirty_dozen))

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

second_dirty_dozen = [fruits, vegetables] # Nested List
print(f"The second_dirty_dozen is: {second_dirty_dozen}")
# print("The second_dirty_dozen is: " + second_dirty_dozen) throws TypeError. You cannot concatenate 

print(len(second_dirty_dozen))
print(f"The second element of the second_dirty_dozen is the list vegetables, {second_dirty_dozen[1]}\n")

element1 = second_dirty_dozen[0][0] # Get the element by using the index twice almost like with matrix indices. 
print(element1) # Prints the first element of the first nested list: Strawberries

element2 = second_dirty_dozen[1][0] 
# Index 1: Second element of names is vegetables, a nested list.
# Index O: First element of the nested list vegetables is Spinach 
print(element2) # Prints the first element of the second nested list: Spinach

element3 = second_dirty_dozen[1][2]
print(element3) # Prints the third element of the second nested list: Tomatoes
element3 = "Birds" #  This will not change the list second_dirty_dozen. We have only reassigned another value to the variable element3, not to the nested list entry.
print(element3)
print(f"second_dirty_dozen after only changing 'element3' variable: {second_dirty_dozen}\n")

second_dirty_dozen[1][2] = "Birds" 
#  will change the list second_dirty_dozen
print(f"second_dirty_dozen after only changing the entry directly: {second_dirty_dozen}\n")

"""Treasure Map"""
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

column = int(position[0]) - 1
row =  int(position[1]) - 1

map[row][column] = "X"

print(f"{row1}\n{row2}\n{row3}")