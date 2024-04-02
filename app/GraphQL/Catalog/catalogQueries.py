from app.GraphQL.Catalog.catalogTypes import Movie, Book, Song
import httpx
import os

async def GetAllMovies() -> list[Movie]:
    api_url = os.environ.get("CATALOG_URL")
    auth_url = api_url + "/movies/"
    async with httpx.AsyncClient() as client:
        response = await client.get(auth_url)
        data = response.json()
        # Turns every JSON on the list into a Movie object
        return [Movie(**movie_data) for movie_data in data]
    
async def GetAllBooks() -> list[Book]:
    api_url = os.environ.get("CATALOG_URL")
    auth_url = api_url + "/books/"
    async with httpx.AsyncClient() as client:
        response = await client.get(auth_url)
        data = response.json()
        # Turns every JSON on the list into a Book object
        return [Book(**book_data) for book_data in data]

async def GetAllSongs() -> list[Song]:
    api_url = os.environ.get("CATALOG_URL")
    auth_url = api_url + "/songs/"
    async with httpx.AsyncClient() as client:
        response = await client.get(auth_url)
        data = response.json()
        # Turns every JSON on the list into a Song object
        return [Song(**song_data) for song_data in data]

async def GetSingleMovie(movieID: str) -> Movie:
    api_url = os.environ.get("CATALOG_URL")
    auth_url = api_url + "/movies"
    async with httpx.AsyncClient() as client:
        response = await client.get(auth_url, params={"id_movie": movieID})
        if response.status_code == 404:
            return None
        data = response.json()
        # Turns the JSON into a Movie object
        for movie_data in data:
            if movie_data.get('id_movie') == movieID:
                return Movie(**movie_data)

async def GetSingleBook(bookID: str) -> Book:
    api_url = os.environ.get("CATALOG_URL")
    auth_url = api_url + "/books"
    async with httpx.AsyncClient() as client:
        response = await client.get(auth_url, params={"id_book": bookID})
        if response.status_code == 404:
            return None
        data = response.json()
        # Turns the JSON into a Book object
        for book_data in data:
            if book_data.get('id_book') == bookID:
                return Book(**book_data)

async def GetSingleSong(songID: str) -> Song:
    api_url = os.environ.get("CATALOG_URL")
    auth_url = api_url + "/songs"
    async with httpx.AsyncClient() as client:
        response = await client.get(auth_url, params={"id_song": songID})
        if response.status_code == 404:
            return None
        data = response.json()
        # Turns the JSON into a Song object
        for song_data in data:
            if song_data.get('id_song') == songID:
                return Song(**song_data)