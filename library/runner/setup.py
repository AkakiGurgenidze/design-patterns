import os

from fastapi import FastAPI

from library.infra.fastapi import book_api
from library.infra.in_memory import BookInMemory


def init_app():
    app = FastAPI()
    app.include_router(book_api)

    if os.getenv("BOOK_REPOSITORY_KIND", "memory") == "sqlite":
        app.state.books = ...
    else:
        app.state.books = BookInMemory()

    return app
