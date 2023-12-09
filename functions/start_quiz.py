import random
import time


from functions.display_question import display_question
from functions.check_answer import check_answer
from functions.get_user_input import get_user_input

from quizs.quiz_1 import questions

def start_quiz():
    """ Start the quiz game """

    score = 0
    random.shuffle(questions)

    for i, question in enumerate(questions, start=1):
        display_question(question)
        user_response = get_user_input()

        if check_answer(user_response, question['answer']):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['answer']}\n")
        
        # Introduce time between each question
        time.sleep(1)

    return (score/len(questions)) * 100

