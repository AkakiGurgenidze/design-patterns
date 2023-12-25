from typing import Annotated

from fastapi import Depends
from fastapi.requests import Request

from library.core.books import BookRepository


def get_book_repository(request: Request) -> BookRepository:
    return request.app.state.books  # type: ignore


BookRepositoryDependable = Annotated[BookRepository, Depends(get_book_repository)]
