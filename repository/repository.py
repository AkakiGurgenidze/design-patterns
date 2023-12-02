from dataclasses import dataclass, field
from typing import Protocol
from uuid import UUID


@dataclass
class Apple:
    id: UUID
    name: str
    color: str


class CrudRepository(Protocol):
    def create(self, apple: Apple) -> None:
        pass

    def read(self, apple_id: UUID) -> Apple:
        pass

    def update(self, apple: Apple) -> None:
        pass

    def delete(self, apple_id: UUID) -> None:
        pass


class ExistsError(Exception):
    pass


class DoesNotExistError(Exception):
    pass


@dataclass
class InMemoryRepository:
    apples: dict[UUID, Apple] = field(default_factory=dict)

    def create(self, apple: Apple) -> None:
        if apple.id in self.apples:
            raise ExistsError

        self.apples[apple.id] = apple

    def read(self, apple_id: UUID) -> Apple:
        try:
            return self.apples[apple_id]
        except KeyError:
            raise DoesNotExistError

    def update(self, apple: Apple) -> None:
        if apple.id not in self.apples:
            raise DoesNotExistError

        self.apples[apple.id] = apple

    def delete(self, apple_id: UUID) -> None:
        try:
            del self.apples[apple_id]
        except KeyError:
            raise DoesNotExistError
