import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL
from starlette.middleware.cors import CORSMiddleware
from app.GraphQL.Users.userQueries import GetAllUsers, GetSingleUser, EmailLogin, GoogleLogin
from app.GraphQL.Users.userMutations import RegisterUser, VerifyAccount
from app.GraphQL.Users.userTypes import User, UserToken, GoogleURL, Other
from dotenv import load_dotenv
from app.utils import Authenticate

from typing import Optional
from app.GraphQL.Catalog.catalogQueries import GetAllMovies, GetAllBooks, GetAllSongs, GetSingleMovie, GetSingleBook, GetSingleSong
from app.GraphQL.Catalog.catalogMutations import InitializeMovies, InitializeBooks, InitializeSongs, CreateMovie, CreateBook, CreateSong, EditMovie, EditBook, EditSong, DeleteMovie, DeleteBook, DeleteSong
from app.GraphQL.Catalog.catalogTypes import Movie, Book, Song

load_dotenv()


@strawberry.type
class Query:
    @strawberry.field
    async def GetMovies(self) -> list[Movie]:
        return await GetAllMovies()
    
    @strawberry.field
    async def GetBooks(self) -> list[Book]:
        return await GetAllBooks()
    
    @strawberry.field
    async def GetSongs(self) -> list[Song]:
        return await GetAllSongs()
    
    @strawberry.field
    async def GetSingleMovie(self, movieID: str) -> Movie:
        potentialData = await GetSingleMovie(movieID=movieID)
        if potentialData is None:
            raise ValueError("Movie not found")
        else:
            return potentialData
    
    @strawberry.field
    async def GetSingleBook(self, bookID: str) -> Book:
        potentialData = await GetSingleBook(bookID=bookID)
        if potentialData is None:
            raise ValueError("Book not found")
        else:
            return potentialData

    @strawberry.field
    async def GetSingleSong(self, songID: str) -> Song:
        potentialData = await GetSingleSong(songID=songID)
        if potentialData is None:
            raise ValueError("Song not found")
        else:
            return potentialData

    @strawberry.field
    async def GetUsers(self, userToken: str) -> list[User]:
        isTokenValid = await Authenticate(userToken)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        return await GetAllUsers()
    
    @strawberry.field
    async def GetUserByUserID(self, userID: int, userToken: str) -> User:
        isTokenValid = await Authenticate(userToken)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        potentialData = await GetSingleUser(userID=userID)
        if potentialData is None:
            raise ValueError("User not found")
        else:
            return potentialData
        
    @strawberry.field
    async def LoginWithEmail(self, email: str, password: str) -> UserToken:
        userToken = await EmailLogin(email=email, password=password)
        if userToken is None:
            raise ValueError("User not found")
        else:
            return userToken
        
    @strawberry.field
    async def LoginWithGoogle(self) -> GoogleURL:
        userToken = await GoogleLogin()
        if userToken is None:
            raise ValueError("User not found")
        else:
            return userToken
        
@strawberry.type
class Mutation:
    @strawberry.field
    async def RegisterWithEmail(self, email: str, password: str, firstName: str, lastName: str, birthdate: str, role: bool) -> UserToken:
        userToken = await RegisterUser(email=email, password=password, firstName=firstName, lastName=lastName, birthdate=birthdate, role=role)
        if userToken is None:
            raise ValueError("User not found")
        else:
            return userToken
    
    @strawberry.field
    async def VerifyUserAccount(self, token: str) -> Other:
        message = await VerifyAccount(token=token)
        if message is None:
            raise ValueError("User not found")
        else:
            return message
        
    @strawberry.mutation
    async def InitializeAllMovies(self) -> str:
        movie = await InitializeMovies()
        if movie is None:
            raise ValueError("Error trying to initialize the movies")
        else:
            return movie
        
    @strawberry.mutation
    async def InitializeAllBooks(self) -> str:
        movie = await InitializeBooks()
        if movie is None:
            raise ValueError("Error trying to initialize the books")
        else:
            return movie
        
    @strawberry.mutation
    async def InitializeAllSongs(self) -> str:
        movie = await InitializeSongs()
        if movie is None:
            raise ValueError("Error trying to initialize the songs")
        else:
            return movie
    
    @strawberry.mutation
    async def CreateNewMovie(self, idMovie: str, awards: Optional[str], cast: Optional[str], director: Optional[str], duration: Optional[str], episodes: Optional[int], genre: Optional[str], original_title: Optional[str], rating: Optional[float], release_date: Optional[str], seasons: Optional[int], title: Optional[str], writers: Optional[str]) -> str:
        movie = await CreateMovie(id_movie=idMovie, awards=awards, cast=cast, director=director, duration=duration, episodes=episodes, genre=genre, original_title=original_title, rating=rating, release_date=release_date, seasons=seasons, title=title, writers=writers)
        if movie is None:
            raise ValueError("Error trying to create the movie")
        else:
            return movie
        
    @strawberry.mutation
    async def CreateNewBook(self, id_book: str, author: Optional[str], genres: Optional[str], pages: Optional[int], rating: Optional[float], title: Optional[str], year: Optional[int]) -> str:
        book = await CreateBook(id_book=id_book, author=author, genres=genres, pages=pages, rating=rating, title=title, year=year)
        if book is None:
            raise ValueError("Error trying to create the book")
        else:
            return book
        
    @strawberry.mutation
    async def CreateNewSong(self, id_song: str, album: Optional[str], artist: Optional[str], duration: Optional[int], genres: Optional[str], title: Optional[str], year: Optional[int]) -> str:
        song = await CreateSong(id_song=id_song, album=album, artist=artist, duration=duration, genres=genres, title=title, year=year)
        if song is None:
            raise ValueError("Error trying to create the book")
        else:
            return song
    
    @strawberry.mutation
    async def EditExistingMovie(self, idMovie: str, awards: Optional[str], cast: Optional[str], director: Optional[str], duration: Optional[str], episodes: Optional[int], genre: Optional[str], original_title: Optional[str], rating: Optional[float], release_date: Optional[str], seasons: Optional[int], title: Optional[str], writers: Optional[str]) -> str:
        movie = await EditMovie(id_movie=idMovie, awards=awards, cast=cast, director=director, duration=duration, episodes=episodes, genre=genre, original_title=original_title, rating=rating, release_date=release_date, seasons=seasons, title=title, writers=writers)
        if movie is None:
            raise ValueError("Error trying to edit the movie")
        else:
            return movie

    @strawberry.mutation
    async def EditExistingBook(self, id_book: str, author: Optional[str], genres: Optional[str], pages: Optional[int], rating: Optional[float], title: Optional[str], year: Optional[int]) -> str:
        book = await EditBook(id_book=id_book, author=author, genres=genres, pages=pages, rating=rating, title=title, year=year)
        if book is None:
            raise ValueError("Error trying to edit the book")
        else:
            return book
        
    @strawberry.mutation
    async def EditExistingSong(self, id_song: str, album: Optional[str], artist: Optional[str], duration: Optional[int], genres: Optional[str], title: Optional[str], year: Optional[int]) -> str:
        song = await EditSong(id_song=id_song, album=album, artist=artist, duration=duration, genres=genres, title=title, year=year)
        if song is None:
            raise ValueError("Error trying to edit the song")
        else:
            return song
    
    @strawberry.mutation
    async def DeleteExistingMovie(self, idMovie: str) -> str:
        movie = await DeleteMovie(id_movie=idMovie)
        if movie is None:
            raise ValueError("Error trying to delete the movie")
        else:
            return movie
    
    @strawberry.mutation
    async def DeleteExistingBook(self, id_book: str) -> str:
        book = await DeleteBook(id_book=id_book)
        if book is None:
            raise ValueError("Error trying to delete the book")
        else:
            return book
    
    @strawberry.mutation
    async def DeleteExistingSong(self, id_song: str) -> str:
        song = await DeleteSong(id_song=id_song)
        if song is None:
            raise ValueError("Error trying to delete the song")
        else:
            return song
        


        


schema = strawberry.Schema(query=Query, mutation=Mutation)


graphql_app = GraphQL(schema)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)

# Syntax for HTTP requests to Microservices
@app.get("/Users")
async def testFetch():
    return await Authenticate("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjZXJ0c2VyaWFsbnVtYmVyIjoiMmo2Mm9PQUNya1BBbWc2SS9WV2Q3QT09IiwibmJmIjoxNzExMzg3MTc4LCJleHAiOjE3MTE0MDE1NzgsImlhdCI6MTcxMTM4NzE3OH0.g-_vB7PcG4_BqU-m1qQGXtUDcSeWfcTZhV6boBRJP9Q")

