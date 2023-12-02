from dataclasses import dataclass

from limited_history import HistoryWithLogging, HistoryWithLimit


class AwesomeHistory:
    def save(self, story: str) -> None:
        pass

    def load(self) -> str:
        pass


@dataclass
class AwesomeHistoryAdapter:
    inner: AwesomeHistory

    def record(self, story: str) -> None:
        self.inner.save(story)

    def recover(self) -> str:
        return self.inner.load()


# Option 2 of initializing history using awesome history instead of infinite history
HistoryWithLogging(HistoryWithLimit(AwesomeHistoryAdapter(AwesomeHistory())))
