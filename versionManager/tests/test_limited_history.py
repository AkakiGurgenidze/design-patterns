import pytest

from versionManager.infinite_history import InfiniteHistory
from versionManager.limited_history import HistoryWithLimit


def test_should_persist_record():
    story = "abc"
    storage = InfiniteHistory()
    history = HistoryWithLimit(storage)

    history.record(story)

    assert storage.recover() == story


def test_should_recover_persisted():
    story = "abc"
    storage = InfiniteHistory()
    storage.record(story)

    history = HistoryWithLimit(storage)

    assert history.recover() == story


def test_should_not_record_more_than_a_limit():
    story = "abc"
    history = HistoryWithLimit(InfiniteHistory(), limit=1)

    history.record(story)
    with pytest.raises(IndexError):
        history.record(story)
