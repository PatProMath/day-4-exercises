# day-4-exercises

## Exercise 1: Coin Toss 
A virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

### Instructions

The basic instructions for the program were: https://app.codingrooms.com/w/UTHIdV9PlgBX

#### Observation
It gave more 'Tails' than 'Heads' at one time. This may have something to do with the pseudorandom generator basis of the random module. 
Also, if the code above in lines 9 was not commented out, the output (i.e state) stays the same no matter how many times you try the Coin Toss! It also affects line 10.
Reason: https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences#:~:text=random%20Module%20Methods-,1.%20seed(),-This%20initializes%20a

## Banker Roulette
A roulette-based decision maker that chooses a name from a list of names.

### Instruction
Write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.

The split function splits the string names_string into individual names and puts them inside a __*list*__ called **names**. For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name.

#### Hint
Use the **len()** function.

## Treasure Map
It asks the user to give a position index to put their treasure. The treasure location index is a two-digit number (11, 12, 13, ..., 21, ..., 31, ..., 33). 

The index/position is not like a matrix, but like that of a chessboard. So, when one inputs 23, they mean for the "X" spot to be at the second column (horizontally) and at the third row (vertically).

### Program Output
```
["⬜️","⬜️","⬜️"]
["⬜️","⬜️","⬜️"]
["⬜️️","⬜️️","⬜️️"]
Where do you want to put the treasure? 23
["⬜️","⬜️","⬜️"]
["⬜️","⬜️","⬜️"]
["⬜️️","X","⬜️️"]
```