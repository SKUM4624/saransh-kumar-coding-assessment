# quiz.py

# I will be making a quiz program in Python.
# Will add up to 10 questions.

from string import ascii_lowercase
import string
import random

name = input("What's your name? ")
NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS = {
    "When was the first known use of the word 'quiz'": [
        "1781", "1771", "1871", "1881"
    ],
     "What's the purpose of the built-in zip() function": [
        "To iterate over two or more sequences at the same time",
        "To combine several strings into one",
        "To compress several files into one archive",
        "To get information from the user",
    ],
    "What's the name of Python's sorting algorithm": [
        "Timsort", "Quicksort", "Merge sort", "Bubble sort"
    ],
    "What does dict.get(key) return if key isn't found in dict": [
        "None", "key", "True", "False",
    ]
}

num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(QUESTIONS))
questions = random.sample(list(QUESTIONS.items()), k=num_questions)

num_correct = 0 # score 
for num, (question, alternatives) in enumerate(questions, start=1): # starts the index with '1' instead of '0', and numbers the questions accordingly.
    print(f"\nQuestion {num}:") 
    print(f"{question}?")
    correct_answer = alternatives[0]
    labeled_alternatives = dict(
        zip(ascii_lowercase, random.sample(alternatives, k=len(alternatives)))
    ) # labels the alternatives in an alphabetically sorted choice list.
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}") # forces the user to choose between the choices if the have typed something else.

    answer = labeled_alternatives[answer_label]
    if answer == correct_answer:
        print("⭐ Correct! ⭐") # Adds a bit of flair.
        num_correct += 1 # adds a point if correct.
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")

print(f"\nYou got {num_correct} correct out of {num} questions") # declares score when quiz is finished.