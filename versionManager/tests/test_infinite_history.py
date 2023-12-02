import pytest

from versionManager.infinite_history import InfiniteHistory


def test_record_and_recover():
    history = InfiniteHistory()

    history.record("1.1.1")

    assert history.recover() == "1.1.1"


def test_multiple_record_and_recover():
    history = InfiniteHistory()

    history.record("1.1.1")
    history.record("1.2.0")

    assert history.recover() == "1.2.0"
    assert history.recover() == "1.1.1"


def test_recover_on_empty_history():
    history = InfiniteHistory()

    with pytest.raises(IndexError):
        history.recover()
