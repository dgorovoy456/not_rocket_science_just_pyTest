import pytest
import cards
from packaging.version import parse


@pytest.mark.skipif(
    parse(cards.__version__).major < 2,
    reason="Card < comparison not supported in 1.x",
)
def test_less_than():
    c1 = cards.Card('a task')
    c2 = cards.Card('b task')
    assert c1 < c2


def test_quality():
    c1 = cards.Card('a task')
    c2 = cards.Card('b task')