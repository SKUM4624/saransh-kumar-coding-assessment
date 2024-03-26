# quiz.py
# Code to be used for assessment.
# I will be making a quiz program in Python.
# Will have at least 5 questions.

from collections import UserString
import string
import random
from string import ascii_lowercase

NUM_QUESTIONS_PER_QUIZ = 10 # constant for the number of questions
QUESTIONS = { # constant variable
    "Who is the principal": [
        "Mr Mcallen", "Mrs DeSchmidt", "Mr Dunn", "Mrs Spooner",
    ],
    "How many credits do you need to pass NCEA Level 1": [
        "60", "80", "100", "40",
    ],
    "Which keyword do you use to loop over a given list of elements": [
        "for", "while", "each", "loop",
    ],
    "What subject is mandatory to Year 11's": [
        "English", "Math", "Science", "Chinese",
    ],
    "What code editor is free on Windows and is most commonly used": [
        "Visual Studio Code", "JetBrains", "Notepad++", "PowerShell",
    ],
    "What is the most common brand of phone": [
        "Iphone", "Samsung", "Google Pixel", "Huawei",
    ],
    "Who declared war on Ukraine": [
        "Russia", "Poland", "India", "Saudi Arabia",
    ],
    "What's symbol increases a variables value by 1": [
        "++", "=+", "+=", "==",
    ],
    "What is the proper spelling of this town": [
        "Whanganui", "Wanganui", "Whaganui", "Whanganoi",
    ],
    "What two keyboard shortcuts are used to copy paste": [
        "Ctrl+C and Ctrl+V", "Ctrl+Shift+C and Ctrl+P", "Ctrl+Shift+C and Ctrl+V", "Ctrl+Shift+O and Ctrl+Shift+P",
    ]
}

def run_quiz():
    questions = prepare_questions( # defines a variable named questions that combines the questions and number of questions
        QUESTIONS, num_questions=NUM_QUESTIONS_PER_QUIZ
    )

    user = input("What's your name? ")
    print(f"Ok {user}, there are {NUM_QUESTIONS_PER_QUIZ} questions about random general topics. Good luck!")
    num_correct = 0
    for num, (question, alternatives) in enumerate(questions, start=1): # starts the index with '1' instead of '0', and numbers the questions accordingly.
        print(f"\nQuestion {num}:") 
        num_correct += ask_question(question, alternatives)

    print(f"\nYou got {num_correct} correct out of {num} questions {user}!") # declares score when quiz is finished.

def prepare_questions(questions, num_questions): 
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions) # properly shuffles the questions for every quiz session

def ask_question(question, alternatives):
    correct_answer = alternatives[0]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives)) # randomizes the choices for each question every session

    answer = get_answer(question, ordered_alternatives)
    if answer == correct_answer:
        print(f"⭐ Good job! You got it correct! ⭐")
        return 1
    else:
        print(f"Sorry, you got it wrong! The answer is {correct_answer!r}, not {answer!r}!")
        return 0

def get_answer(question, alternatives):
    print(f"{question}?")
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives)) # labels all of the multiple choice from A to D
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}") # prints the question then the alternatives underneath it

    while (answer_label := input("\nChoice? ")) not in labeled_alternatives: # asks user to choose a choice
        print(f"Please answer one of {', '.join(labeled_alternatives)}") # forces the user to choose between the choices if the have typed something else

    return labeled_alternatives[answer_label]

if __name__ == "__main__":
    run_quiz()