from brain_games.scripts.brain_even import is_even, is_correct_answer


def test_even():
    assert is_even(1) is False
    assert is_even(2) is True
    assert is_even(80) is True


def test_correct_answer():
    answer = "yes"
    assert (is_even(2) and (answer == "yes")) == True
    assert True is is_correct_answer(3, "no")
    assert True is is_correct_answer(2, "yes")
    # assert is_even(2) is is_correct_answer(2, "yes")
    assert is_even(8) is is_correct_answer(8, "yes")
