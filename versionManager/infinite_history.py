from dataclasses import dataclass, field


@dataclass
class InfiniteHistory:
    _stories: list[str] = field(default_factory=list)

    def record(self, story: str) -> None:
        self._stories.append(story)

    def recover(self) -> str:
        return self._stories.pop()
