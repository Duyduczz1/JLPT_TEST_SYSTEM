import random


def pick_questions(questions, amount):
    if len(questions) <= amount:
        return questions
    return random.sample(questions, amount)
