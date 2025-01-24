import prompt


def welcome_user():
    name = prompt.string("May I have your name? ")
    message = f"Hello, {name}"
    print(message)
