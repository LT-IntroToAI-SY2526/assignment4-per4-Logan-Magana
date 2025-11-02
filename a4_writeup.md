# Assignment 4 - Writeup

In assignment 4 we created a basic tic tac toe game so that we could learn object oriented programming. Respond to the following questions.

## Reflection Questions

1. What was the most difficult part to tic-tac-toe? When working on it by myself, the hardest part was to print the board itself.What I was doing print(brd.board) instead of print(brd). This caused the program to only print the attribute instead of the object.

2. Explain how you would add a computer player to the game. When the code switches to the next player ( using the turn variable ), instead of asking again for another input, the code will place their symbol automatically and then return to the player. 

3. If you add a computer player, explain (doesn't have to be super technical) how you might get the computer player to play the best move every time. *Note - I am not grading this for a correct answer, I just want to know your thoughts on how you might accomplish it.
I would probably make it so it would start in the same area because the shape of the game is a square so starting in one corner is the same as the other corner. If the robot goes first I'd probably place it in a corner, to threaten a diagnal and straight. If the robot goes second, id tell it to go to the middle because it can block all the diagnals.Assuming the player is playing perfectly, the robot would have to block whichever line that the player threatens. I'm not sure about the syntax of all of that but that's my thought process.
