from typing import Optional
import httpx
import os

async def InitializeMovies() -> str:
    api_url = os.environ.get("CATALOG_URL")
    auth_url = api_url + "/movies/init"
    async with httpx.AsyncClient() as client:
        response = await client.get(auth_url, headers={"Content-Type": "application/json"})
        if response.status_code == 500:
            return None
        return response.text
    
async def InitializeBooks() -> str:
    api_url = os.environ.get("CATALOG_URL")
    auth_url = api_url + "/books/init"
    async with httpx.AsyncClient() as client:
        response = await client.get(auth_url, headers={"Content-Type": "application/json"})
        if response.status_code == 500:
            return None
        return response.text
    
async def InitializeSongs() -> str:
    api_url = os.environ.get("CATALOG_URL")
    auth_url = api_url + "/songs/init"
    async with httpx.AsyncClient() as client:
        response = await client.get(auth_url, headers={"Content-Type": "application/json"})
        if response.status_code == 500:
            return None
        return response.text

async def CreateMovie(id_movie: str, awards: Optional[str], cast: Optional[str], director: Optional[str], duration: Optional[str], episodes: Optional[int], genre: Optional[str], original_title: Optional[str], rating: Optional[float], release_date: Optional[str], seasons: Optional[int], title: Optional[str], writers: Optional[str]) -> str:
    api_url = os.environ.get("CATALOG_URL")
    auth_url = api_url + "/movies"
    async with httpx.AsyncClient() as client:
        response = await client.post(auth_url, headers={"Content-Type": "application/json"}, json={"id_movie": id_movie, "awards": awards, "cast": cast, "director": director, "duration": duration, "episodes": episodes, "genre": genre, "original_title": original_title, "rating": rating, "release_date": release_date, "seasons": seasons, "title": title, "writers": writers})
        if response.status_code == 500:
            return None
        return response.text

async def CreateBook(id_book: str, author: Optional[str], genres: Optional[str], pages: Optional[int], rating: Optional[float], title: Optional[str], year: Optional[int]) -> str:
    api_url = os.environ.get("CATALOG_URL")
    auth_url = api_url + "/books"
    async with httpx.AsyncClient() as client:
        response = await client.post(auth_url, headers={"Content-Type": "application/json"}, json={"id_book": id_book, "author": author, "genres": genres, "pages": pages, "rating": rating, "title": title, "year": year})
        if response.status_code == 500:
            return None
        return response.text

async def CreateSong(id_song: str, album: Optional[str], artist: Optional[str], duration: Optional[int], genres: Optional[str], title: Optional[str], rating: Optional[float], year: Optional[int]) -> str:
    api_url = os.environ.get("CATALOG_URL")
    auth_url = api_url + "/songs"
    async with httpx.AsyncClient() as client:
        response = await client.post(auth_url, headers={"Content-Type": "application/json"}, json={"id_song": id_song, "album": album, "artist": artist, "duration": duration, "genres": genres, "title": title, "rating": rating, "year": year})
        if response.status_code == 500:
            return None
        return response.text
    
async def EditMovie(id_movie: str, awards: Optional[str], cast: Optional[str], director: Optional[str], duration: Optional[str], episodes: Optional[int], genre: Optional[str], original_title: Optional[str], rating: Optional[float], release_date: Optional[str], seasons: Optional[int], title: Optional[str], writers: Optional[str]) -> str:
    api_url = os.environ.get("CATALOG_URL")
    auth_url = f"{api_url}/movies/{id_movie}"
    async with httpx.AsyncClient() as client:
        response = await client.put(auth_url, headers={"Content-Type": "application/json"}, json={"id_movie": id_movie, "awards": awards, "cast": cast, "director": director, "duration": duration, "episodes": episodes, "genre": genre, "original_title": original_title, "rating": rating, "release_date": release_date, "seasons": seasons, "title": title, "writers": writers})
        if response.status_code == 500:
            return None
        return response.text

async def EditBook(id_book: str, author: Optional[str], genres: Optional[str], pages: Optional[int], rating: Optional[float], title: Optional[str], year: Optional[int]) -> str:
    api_url = os.environ.get("CATALOG_URL")
    auth_url = f"{api_url}/books/{id_book}"
    async with httpx.AsyncClient() as client:
        response = await client.put(auth_url, headers={"Content-Type": "application/json"}, json={"id_book": id_book, "author": author, "genres": genres, "pages": pages, "rating": rating, "title": title, "year": year})
        if response.status_code == 500:
            return None
        return response.text

async def EditSong(id_song: str, album: Optional[str], artist: Optional[str], duration: Optional[int], genres: Optional[str], title: Optional[str], rating: Optional[float], year: Optional[int]) -> str:
    api_url = os.environ.get("CATALOG_URL")
    auth_url = f"{api_url}/songs/{id_song}"
    async with httpx.AsyncClient() as client:
        response = await client.put(auth_url, headers={"Content-Type": "application/json"}, json={"id_song": id_song, "album": album, "artist": artist, "duration": duration, "genres": genres, "title": title, "rating": rating, "year": year})
        if response.status_code == 500:
            return None
        return response.text
    
async def DeleteMovie(id_movie: str) -> str:
    api_url = os.environ.get("CATALOG_URL")
    auth_url = f"{api_url}/movies/{id_movie}"
    async with httpx.AsyncClient() as client:
        response = await client.delete(auth_url, headers={"Content-Type": "application/json"})
        if response.status_code == 500:
            return None
        return response.text

async def DeleteBook(id_book: str) -> str:
    api_url = os.environ.get("CATALOG_URL")
    auth_url = f"{api_url}/books/{id_book}"
    async with httpx.AsyncClient() as client:
        response = await client.delete(auth_url, headers={"Content-Type": "application/json"})
        if response.status_code == 500:
            return None
        return response.text
    
async def DeleteSong(id_song: str) -> str:
    api_url = os.environ.get("CATALOG_URL")
    auth_url = f"{api_url}/songs/{id_song}"
    async with httpx.AsyncClient() as client:
        response = await client.delete(auth_url, headers={"Content-Type": "application/json"})
        if response.status_code == 500:
            return None
        return response.text