# Python version used 3.8
# Importing the csv module to work with the CSV file
import csv

# Defining the main function for the quiz game
def play_quiz():
    # Opening and reading the CSV file containing the quiz data
    with open('questions.csv', mode='r') as file:
        # Using csv.DictReader to convert the CSV file into a list of dictionaries
        # Each row in the CSV becomes a dictionary with column headers as keys
        quiz_data = list(csv.DictReader(file))

    # Then initialize the scores to keep track of correct answers
    score = 0

    # After that, Loop through each question in the quiz data
    for row in quiz_data:
        # Print the question
        print(row['Question'])
        
        # Print each of the four possible answers
        for i in range(1, 5):
            # This dynamically accesses each answer using its number
            print(f"{i}. {row['Answer ' + str(i)]}")

        # Prompt the user for their answer and store it
        user_input = input("Your answer (1-4): ")
        
        # Validate user input; it must be one of '1', '2', '3', '4'
        while user_input not in ['1', '2', '3', '4']:
            # Inform user of invalid input and prompt again
            print("Invalid input. Please enter a number between 1 and 4.")
            user_input = input("Your answer (1-4): ")

        # Check if the user's answer matches the correct answer
        # .strip() is used to remove any leading/trailing whitespace in the CSV data
        if user_input == row['Correct Answer'].strip():
            print("Correct!")
            # Increment score for a correct answer
            score += 1
        else:
            # Retrieve the correct answer based on the 'Correct Answer' value
            correct_ans = row['Answer ' + row['Correct Answer'].strip()]
            # Inform user of the correct answer if they were wrong
            print(f"Wrong! The correct answer is: {correct_ans}")

    # Calculating the total score
    total_questions = len(quiz_data)
    # Calculating the percentage score and rounding it to 2 decimal places
    score_percent = round((score / total_questions) * 100, 2)
    # Printing the user's score and percentage
    print(f"Your score: {score}/{total_questions} ({score_percent}%)")

    # Asking the user if they want to play the quiz again
    play_again = input("Do you want to play again? (yes/no): ")
    # If the user answers 'yes', the quiz restarts
    if play_again.lower() == 'yes':
        play_quiz()

# Start the quiz by calling the play_quiz function
play_quiz()
