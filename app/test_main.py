from app.main import get_coin_combination


def test_coin_combination_with_one_penny_coin():
    cents = 1
    assert get_coin_combination(cents) == [1, 0, 0, 0]


def test_coin_combination_with_one_penny_one_nickel():
    cents = 6
    assert get_coin_combination(cents) == [1, 1, 0, 0]


def test_coin_combination_with_two_penny_one_nickel_one_dime():
    cents = 17
    assert get_coin_combination(cents) == [2, 1, 1, 0]


def test_coin_combination_with_two_quarters():
    cents = 50
    assert get_coin_combination(cents) == [0, 0, 0, 2]
