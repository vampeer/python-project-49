from brain_games.scripts.brain_even import is_even


def test_even():
    assert is_even(1) is False
    assert is_even(2) is True
    assert is_even(80) is True
