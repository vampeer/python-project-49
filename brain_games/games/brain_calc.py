import operator
import random
from brain_games.games.brain_even import generate_number

RULES = "What is the result of the expression?"


operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
}


def generate_operation():
    return random.choice(list(operations.keys()))


def make_question():
    first_num = generate_number()
    second_num = generate_number()
    operator = generate_operation()
    question = f"Question: {first_num}{operator}{second_num}"
    answer = correct_answer(first_num, second_num, operator)
    return (question, answer)


def correct_answer(first, second, operation):
    return str(operations[operation](first, second))
