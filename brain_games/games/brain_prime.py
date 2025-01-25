from brain_games.games.brain_even import generate_number

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num in [1, 2]:
        return "yes"

    for i in range(2, num):
        if num % i == 0:
            return "no"

    return "yes"


def make_question():
    num = generate_number()
    question = f"Question: {num}"
    answer = is_prime(num)
    return (question, answer)
