quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "question3": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"               
    },
    "question4": {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },
    "question4": {
        "question": "What is the capital of England?",
        "answer": "London"
    },
    "question5": {
        "question": "What is the capital of Portugal?",
        "answer": "Lisbon"
    },
    "question6": {
        "question": "What is the capital of Switzerland?",
        "answer": "Bern"
    },
    "question7": {
        "question": "What is the capital of Austria?",
        "answer": "Vienna"
    },
}


score = 0
for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")
    
    if answer.lower() == value['answer'].lower():
        print("Correct")
        
        score += 1
        print("Your score is: " + str(score))
        print("")
        print("")
        
    else:
        print("Wrong")
        print("The answer is: " + value['answer'])
        print("Your score : " + str(score))
        total_score = 100 * score / 7
        print("")
        print("")
        
print("Your total score in percentage is " + str(total_score) + "%.")
