from cards import Card


def test_less_than():
    c1 = Card('a task')
    c2 = Card('b task')
    assert c1 < c2


def test_quality():
    c1 = Card('a task')
    c2 = Card('b task')