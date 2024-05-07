import strawberry
from typing import Optional

@strawberry.type
class Movie:
    id_movie: str
    awards: Optional[str]
    cast: Optional[str]
    director: Optional[str]
    duration: Optional[str]
    episodes: Optional[int]
    genre: Optional[str]
    original_title: Optional[str]
    rating: Optional[float]
    release_date: Optional[str]
    seasons: Optional[int]
    title: Optional[str]
    writers: Optional[str]

@strawberry.type
class Book:
    id_book: str
    author: Optional[str]
    genres: Optional[str]
    pages: Optional[int]
    rating: Optional[float]
    title: Optional[str]
    year: Optional[int]

@strawberry.type
class Song:
    id_song: str
    album: Optional[str]
    artist: Optional[str]
    duration: Optional[int]
    genres: Optional[str]
    title: Optional[str]
    rating: Optional[float]
    year: Optional[int]