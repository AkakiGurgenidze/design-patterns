from dataclasses import dataclass, field
from uuid import UUID

from library.core.books import Book
from library.core.errors import DoesNotExistError


@dataclass
class BookInMemory:
    books: dict[UUID, Book] = field(default_factory=dict)

    def create(self, book: Book) -> None:
        self.books[book.id] = book

    def read(self, book_id: UUID) -> Book:
        try:
            return self.books[book_id]
        except KeyError:
            raise DoesNotExistError(book_id)

    def read_all(self) -> list[Book]:
        return list(self.books.values())
