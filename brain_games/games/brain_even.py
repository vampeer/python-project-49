import random

# from brain_games.cli import generate_number

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_number():
    """Generate random number"""
    return random.randint(1, 100)


def make_question():
    number = generate_number()
    question = f"Question: {number}"
    answer = correct_answer(number)
    return (question, answer)


def correct_answer(number):
    return "yes" if number % 2 == 0 else "no"
