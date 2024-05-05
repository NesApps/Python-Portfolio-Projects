#  a dictionary that stores question and answers
#  have a variable that tracks the score of the player
#  loop through the dictionary using the key value pair
#  display each question to the user and allow them to answer
#  tell them if they are right or wrong
#  show the final result when quiz is completed

quiz = {
    "question1": {
        "question": "what is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "what is the capital of UK?",
        "answer": "London"
    },
    "question3": {
        "question": "what is the capital of Nigeria?",
        "answer": "Abuja"
    },
    "question4": {
        "question": "what is the capital of Germany?",
        "answer": "Berlin"
    },
    "question5": {
        "question": "what is the capital of Spain?",
        "answer": "Madrid"
    },
    "question6": {
        "question": "what is the capital of Portugal?",
        "answer": "Lisbon"
    },
    "question7": {
        "question": "what is the capital of Switzerland?",
        "answer": "Bern"
    },
    "question8": {
        "question": "what is the capital of Austria?",
        "answer": "Vienna"
    },
    "question9": {
        "question": "what is the capital of Italy?",
        "answer": "Rome"
    }
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print('Correct')
        score = score + 1
        print(f"Your score is: {score}")
        print("")
        print("")

    else:
        print("Wrong")
        print(f"The correct answer is: {value['answer']}")
        print(f"Your score is: {score}")
        print("")
        print("")

print(f"You got {score} out of 8 questions correctly")
print(f"Your percentage is {int(score / 9*100)}%")
