from brain_games.games.brain_even import generate_number

RULES = "What number is missing in the progression?"


def generate_progression(length):
    difference = generate_number(1, 15)
    start = generate_number(1, 9)
    progression = []
    progression.append(start)
    while len(progression) < length:
        progression.append(difference + progression[len(progression) - 1])

    hidden_index = generate_number(0, length - 1)
    answer = str(progression[hidden_index])
    progression[hidden_index] = ".."
    progression = map(str, progression)
    progression = " ".join(progression)
    return (progression, answer)


def make_question():
    progression, correct_answer = generate_progression(10)
    question = f"Question: {''.join(progression)}"
    answer = correct_answer
    return (question, answer)
