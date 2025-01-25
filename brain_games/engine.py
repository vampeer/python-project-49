from brain_games.cli import get_user_answer, get_user_name

POINT_TO_WIN = 3


def welcome_user():
    """Get username and print welcome message"""
    name = get_user_name()
    message = f"Hello, {name}!"
    print(message)
    return name


def run(game=None):
    """Run games"""
    print("Welcome to the Brain Games!")
    name = welcome_user()

    if game:
        print(game.RULES)

        return engine(name, game)


def engine(name, game):
    answers = 0
    while answers < POINT_TO_WIN:
        question, correct_answer = game.make_question()
        print(question)
        user_answer = get_user_answer()
        if user_answer == correct_answer:
            answers += 1
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. ",
                f"Correct answer was '{correct_answer}'.!",
            )
            print(f"Let's try again, {name}!")
            break

    if answers == POINT_TO_WIN:
        print(f"Congratulations, {name}!")
