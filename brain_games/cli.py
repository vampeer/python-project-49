import prompt


def welcome_user():
    name = prompt.string("May I have your name? ")
    message = f"Hello, {name}"
    print(message)


def get_user_name():
    name = prompt.string("May I have your name? ")
    return name


def get_user_answer():
    user_answer = prompt.string("Your answer: ")
    return user_answer
