import logging
from dataclasses import dataclass

from versionManager.infinite_history import InfiniteHistory
from versionManager.version_manager import History


@dataclass
class HistoryDecorator:
    inner: History

    def record(self, story: str) -> None:
        self.inner.record(story)

    def recover(self) -> str:
        return self.inner.recover()


@dataclass
class HistoryWithLimit(HistoryDecorator):
    limit: int = 10
    _n_records: int = 0

    def record(self, story: str) -> None:
        if self.limit == self._n_records:
            raise IndexError

        self._n_records += 1
        super().record(story)

    def recover(self) -> str:
        self._n_records -= 1

        return super().recover()


class HistoryWithLogging(HistoryDecorator):
    def record(self, story: str) -> None:
        logging.info("abracadabra")
        super().record(story)


# Option 1 of initializing history using multiple decorations
HistoryWithLogging(HistoryWithLimit(InfiniteHistory()))
