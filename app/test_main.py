from app.main import get_coin_combination


def test_coin_combination_with_one_penny_coin():
    cents = 1
    assert get_coin_combination(cents) == [1, 0, 0, 0]


def test_coin_combination_with_one_penny_one_nickel():
    cents = 5
    assert get_coin_combination(cents) == [0, 1, 0, 0]


def test_coin_combination_with_one_dime():
    cents = 10
    assert get_coin_combination(cents) == [0, 0, 1, 0]


def test_coin_combination_with_one_quarters():
    cents = 25
    assert get_coin_combination(cents) == [0, 0, 0, 1]


def test_coin_combination_with_two_quarters():
    cents = 50
    assert get_coin_combination(cents) == [0, 0, 0, 2]


def test_coin_combination_with_all_coin():
    cents = 116
    assert get_coin_combination(cents) == [1, 1, 1, 4]


def test_coin_combination_with_zero_cents():
    cents = 0
    assert get_coin_combination(cents) == [0, 0, 0, 0]


def test_coin_combination_with_negative_cents():
    cents = -10
    assert get_coin_combination(cents) == "Invalid cents"