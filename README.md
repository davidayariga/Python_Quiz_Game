# Python_Quiz_Game
This python quiz game comprise 10 general questions relating to geography.

## Rationale for the project

This project was developed to fulfill the requirements of the ReDI School for Digital Integration's Python Intermediate Course.

## Requirements of the quiz game
The goal is to create a script that asks the user general questions and prints the results. The questions are read from a CSV file. Each row in the CSV file contains a question, four possible answers, and the correct answer, formatted as follows: 

Question,Answer 1,Answer 2,Answer 3,Answer 4,Correct Answer

What is the provincial capital of Nova Scotia?,Baddeck,Digby,Lunenburg,Halifax,4

## Specific requirements of the quiz game
1. Read CSV file (line by line)
   
   a. Ask question and present possible answers
   
   b. Read user input
   
   c. Check user input (and update score)
   
   d. Give immediate feedback (print correct answer if user’s answer was  wrong)
   
3. Print score ratio (in percent and rounded to 2 digits)
## Code Explanation
The code consists of three main classes: Quiz, QuizQuestion, and QuizGame.

### Quiz Class
Initialization: Sets up the question, possible answers and the correct answer.
ask_question: Displays the question and possible answers.
check_answer: Compares the user’s input to the correct answer.
### QuizQuestion Class
Inherits from Quiz and initializes using the superclass constructor.
### QuizGame Class
Initialization: Loads questions from a CSV file and sets the initial score.
load_questions: Reads questions from the CSV file and handles file not found or other errors.
play: Main game loop that iterates through each question, asks for user input, checks the answer, provides feedback, and updates the score.
get_user_input: Validates the user’s input to ensure it’s a number between 1 and 4.
show_score: Displays the user's score as a percentage.
ask_play_again: Prompts the user to play again and restarts the game if they choose to.
### GameInherit Class
Inherits from QuizGame and initializes using the superclass constructor.
### Main Script
Initializes the QuizGame with questions from questions.csv and starts the game if questions are loaded.
