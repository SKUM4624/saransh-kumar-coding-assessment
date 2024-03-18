# quiz.py

# I will be making a quiz program in Python.
# Will have at least 5 questions.

import string
import random
from string import ascii_lowercase

NUM_QUESTIONS_PER_QUIZ = 10
QUESTIONS = {
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
        "Wanganui", "Whanganui", "Whaganui", "Whanganoi",
    ],
    "What two keyboard shortcuts are used to copy paste": [
        "Ctrl+C and Ctrl+V", "Ctrl+Shift+C and Ctrl+P", "Ctrl+Shift+C and Ctrl+V", "Ctrl+Shift+O and Ctrl+Shift+P",
    ]
}

def run_quiz():
    questions = prepare_questions(
        QUESTIONS, num_questions=NUM_QUESTIONS_PER_QUIZ
    )

    num_correct = 0
    for num, (question, alternatives) in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        num_correct += ask_question(question, alternatives)

    print(f"\nYou got {num_correct} correct out of {num} questions")

def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)

def ask_question(question, alternatives):
    correct_answer = alternatives[0]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answer = get_answer(question, ordered_alternatives)
    if answer == correct_answer:
        print("⭐ Correct! ⭐")
        return 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
        return 0

def get_answer(question, alternatives):
    print(f"{question}?")
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")

    return labeled_alternatives[answer_label]

if __name__ == "__main__":
    run_quiz()