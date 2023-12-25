from uuid import UUID

from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import JSONResponse

from library.core.books import BookService, Book
from library.core.errors import DoesNotExistError
from library.infra.fastapi.dependables import BookRepositoryDependable

book_api = APIRouter(tags=["Books"])


class CreateBookRequest(BaseModel):
    name: str
    isbn: str
    author: str


class BookItem(BaseModel):
    id: UUID
    name: str
    isbn: str
    author: str


class BookItemEnvelope(BaseModel):
    book: BookItem


class BookListEnvelope(BaseModel):
    books: list[BookItem]


@book_api.post(
    "/books",
    status_code=201,
    response_model=BookItemEnvelope,
)
def create_book(request: CreateBookRequest, books: BookRepositoryDependable):
    book = Book(**request.model_dump())
    books.create(book)

    return {"book": book}


@book_api.get(
    "/books/{book_id}",
    status_code=200,
    response_model=BookItem,
)
def read_book(book_id: UUID, books: BookRepositoryDependable) -> Book | JSONResponse:
    try:
        return books.read(book_id)
    except DoesNotExistError:
        return JSONResponse(
            status_code=404,
            content={"message": f"Book with id<{book_id}> does not exist."},
        )


@book_api.get("/books", response_model=BookListEnvelope)
def read_all(books: BookRepositoryDependable, author_starts_with: str = ""):
    return {"books": BookService(books).filter_author(author_starts_with)}
