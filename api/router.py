from fastapi import APIRouter, status, HTTPException

from fastapi.responses import JSONResponse
from api.routes import books


api_router = APIRouter()
api_router.include_router(books.router, prefix="/books", tags=["books"])


@api_router.get('/books/{book_id}')
async def book_details(book_id):
    book = books.db.get_book(book_id=(int(book_id)))
    if book:
        return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=book.model_dump()
    )
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Book not found'
        )
