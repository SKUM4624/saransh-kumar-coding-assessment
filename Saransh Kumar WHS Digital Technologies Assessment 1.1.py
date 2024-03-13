# I will be making a quiz program in Python.
# Will add up to 10 questions.
name = input("What's your name? ")

QUESTIONS = {
    "When was the first known use of the word 'quiz'": [
        "1781", "1771", "1871", "1881"
    ],
    "Which keyword do you use to loop over a given list of elements": [
        "for", "while", "each", "loop"
    ],
    "What's the purpose of the built-in zip() function": [
        "To iterate over two or more sequences at the same time",
        "To combine several strings into one",
        "To compress several files into one archive",
        "To get information from the user",
    ],
    "What's the name of Python's sorting algorithm": [
        "Timsort", "Quicksort", "Merge sort", "Bubble sort"
    ] # These are all the different choices for different questions.  
}

for question, alternatives in QUESTIONS.items():
    correct_answer = alternatives[0]
    sorted_alternatives = sorted(alternatives)
    for label, alternative in enumerate(sorted_alternatives): # enumerate is used to label each of the answers so the player does not have to type out the whole answer. They can just type on of the numbers.
        print(f"  {label}) {alternative}")

    answer_label = int(input(f"{question}? ")) # use of int to convert the options into the number that labels an answer.
    answer = sorted_alternatives[answer_label]
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")