import math
import random

from brain_games.games.brain_even import generate_number

RULES = "Find the greatest common divisor of given numbers."


def make_question():
    first_num = generate_number()
    second_num = generate_number()
    question = f"Question: {first_num} and {second_num}"
    answer = correct_answer(first_num, second_num)
    return (question, answer)


def correct_answer(first, second):
    return str(math.gcd(first, second))
