from __future__ import annotations
from dataclasses import dataclass, field

from typing import Protocol
from uuid import UUID, uuid4


@dataclass
class BookService:
    books: BookRepository

    def filter_author(self, starts_with: str) -> list[Book]:
        all_books = self.books.read_all()

        return [book for book in all_books if book.author.startswith(starts_with)]


class BookRepository(Protocol):
    def create(self, book: Book) -> None:
        pass

    def read(self, book_id: UUID) -> Book:
        pass

    def read_all(self) -> list[Book]:
        pass


@dataclass
class Book:
    name: str
    isbn: str
    author: str

    id: UUID = field(default_factory=uuid4)
