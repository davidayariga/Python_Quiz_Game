# import csv module
import csv

# define Class for common quiz functionalities
class Quiz:
    def __init__(self, question, answers, correct_answer): # Initialize the question, possible answers, and the correct answer
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer

    def ask_question(self): # Method that displays the question and list the possible answers
        print(self.question)
        for i, answer in enumerate(self.answers, 1):
            print(f"{i}. {answer}")

    def check_answer(self, user_input):  # Method that check if the user's input matches the correct answer
        return user_input == self.correct_answer

# Define inheritance class for individual quiz questions which inherits from Quiz
class QuizQuestion(Quiz):
    def __init__(self, question, answers, correct_answer):
        # Initialize the base Quiz class
        super().__init__(question, answers, correct_answer)

# Define class for quiz game functionalities
class QuizGame:
    def __init__(self, filename):  # Initialize the filename and load questions from the CSV file
        self.filename = filename
        self.questions = self.load_questions()
        self.score = 0

    def load_questions(self):  # Method for Loading quiz questions from a csv file
        questions = []
        try:
            with open(self.filename, mode='r') as file: # open csv file in read mode
                quiz_data = csv.DictReader(file)
                for row in quiz_data:
                    question = row['Question']
                    answers = [row[f'Answer {i}'] for i in range(1, 5)]
                    correct_answer = row['Correct Answer'].strip()
                    questions.append(QuizQuestion(question, answers, correct_answer))
        except FileNotFoundError: # Raise file error if csv file not found or properly formatted
            print(f"Error: The file '{self.filename}' was not found.")
        except Exception as e:
            print(f"Error: An unexpected error occurred - {e}")
        return questions

    def play(self):  # Main game loop to play the quiz
        self.score = 0
        for question in self.questions:
            question.ask_question()
            user_input = self.get_user_input()
            if question.check_answer(user_input):
                print("Correct!")
                self.score += 1
            else:
                correct_ans = question.answers[int(question.correct_answer) - 1]
                print(f"Wrong! The correct answer is: {correct_ans}")
   
        self.show_score()
        self.ask_play_again()

    def get_user_input(self): # A method to get user input and ensure it's a valid answer (1-4)
        while True:
            try:
                user_input = input("Your answer (1-4): ").strip()
                if user_input not in ['1', '2', '3', '4']:
                    raise ValueError("Invalid input. Please enter a number between 1 and 4.")
                return user_input
            except ValueError as e:
                print(e)

    def show_score(self): # A menthod that displays the user's score as a percentage
        total_questions = len(self.questions)
        score_percent = round((self.score / total_questions) * 100, 2)
        print(f"Your score: {self.score}/{total_questions} ({score_percent}%)")

    def ask_play_again(self): # A method which asks the user if they want to play again and restart the game if they do
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again == 'yes':
            self.play()

# Inheritance class for GameIherit, inherits from QuizGame
class GameInherit(QuizGame):
    def __init__(self, filename):
        # Initialize the base QuizGame class
        super().__init__(filename)

# Main entry point for the script
if __name__ == "__main__":
    # Initialize the game with questions from 'questions.csv' and start the game if questions are loaded
    quiz_game = QuizGame('questions.csv')
    if quiz_game.questions:
        quiz_game.play()

