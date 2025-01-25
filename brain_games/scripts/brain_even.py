import prompt
import random


count_correct_answers = 0
point = 1
points_for_win = 3


def welcome_user():
    global name
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    message = f"Hello, {name}!"
    print(message)


def is_win():
    if count_correct_answers >= points_for_win:
        return True
    return False


def is_even(num):
    if num % 2 == 0:
        return "yes"
    return "no"


def is_valid(answer):
    if answer in ["yes", "no"]:
        return True
    return False


def attempt_answer():
    global count_correct_answers
    number = random.randint(1, 99)
    question = f"Question: {number}"

    print(question)
    user_answer = prompt.string("Your answer:")
    user_answer = user_answer.strip().lower()

    if is_valid(user_answer):
        if user_answer == is_even(number):
            print("Correct!")
            count_correct_answers = count_correct_answers + point
            if is_win():
                print(f"Congratulations, {name}!")
                exit()
            attempt_answer()

    print(
        f"'{user_answer}' is wrong answer ;(. Correct answer was '{is_even(number)}'."
    )
    print(f"Let's try again, {name}!")
    exit()


def main():
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    attempt_answer()


if __name__ == "__main__":
    main()
