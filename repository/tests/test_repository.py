from uuid import uuid4

import pytest

from repository.repository import InMemoryRepository, DoesNotExistError, Apple, ExistsError


def test_should_not_read_unknown() -> None:
    unknown_id = uuid4()
    repository = InMemoryRepository()

    with pytest.raises(DoesNotExistError):
        repository.read(unknown_id)


def test_should_persist() -> None:
    apple = Apple(id=uuid4(), name="Golden", color="Gold")
    repository = InMemoryRepository()

    repository.create(apple)

    assert repository.read(apple.id) == apple


def test_should_not_duplicate() -> None:
    apple = Apple(id=uuid4(), name="Golden", color="Gold")
    repository = InMemoryRepository()
    repository.create(apple)

    with pytest.raises(ExistsError):
        repository.create(apple)


def test_should_not_update_unknown() -> None:
    apple = Apple(id=uuid4(), name="Golden", color="Gold")
    repository = InMemoryRepository()

    with pytest.raises(DoesNotExistError):
        repository.update(apple)


def test_should_persist_update() -> None:
    apple = Apple(id=uuid4(), name="Golden", color="Gold")
    repository = InMemoryRepository()
    repository.create(apple)
    apple.name = "Ambrosia"
    apple.color = "Red"

    repository.update(apple)

    assert repository.read(apple.id) == apple


def test_should_not_delete_unknown() -> None:
    unknown_id = uuid4()
    repository = InMemoryRepository()

    with pytest.raises(DoesNotExistError):
        repository.delete(unknown_id)


def test_should_delete() -> None:
    apple = Apple(id=uuid4(), name="Golden", color="Gold")
    repository = InMemoryRepository()
    repository.create(apple)

    repository.delete(apple.id)

    with pytest.raises(DoesNotExistError):
        repository.read(apple.id)
