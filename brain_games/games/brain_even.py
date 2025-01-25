import random

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_number(x=1, y=100):
    """Generate random number"""
    return random.randint(x, y)


def make_question():
    number = generate_number()
    question = f"Question: {number}"
    answer = correct_answer(number)
    return (question, answer)


def correct_answer(number):
    return "yes" if number % 2 == 0 else "no"
