from homework_3_15 import calculator


def test_add():
    assert calculator.add(4.5, 5.5) == 10


def test_minus():
    assert calculator.minus(15.5, 5.5) == 10


def test_multiple():
    assert calculator.multiple(3, 3.5) == 10.5


def test_divide():
    assert calculator.divide(55, 5.5) == 10
