import pytest


@pytest.fixture(name='renamed')
def ultimate_answer_fixture():
    return 42


def test_everything(renamed):
    assert renamed == 42
