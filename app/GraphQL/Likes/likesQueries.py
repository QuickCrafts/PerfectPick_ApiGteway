import json
import httpx
import os
from app.GraphQL.Likes.likesTypes import Like, LikeExtended, Media, Wishlist

async def GetLikesById(id: int, media:str = None, preference: str = None) -> list[Like]:
    api_url = os.environ.get("LIKES_URL")
    likes_url = api_url + "/likes/user/" + str(id)

    if media != None and preference == None:
        likes_url = likes_url + "?media_type=" + media
    elif preference != None and media == None:
        likes_url = likes_url + "?preference=" + preference
    elif preference != None and media != None:
        likes_url = likes_url + "?preference=" + preference + "&media_type=" + media

    async with httpx.AsyncClient() as client:
        response = await client.get(likes_url)
        data = response.json()
        likes = []
        movies = []
        songs = []
        books = []

        if isinstance(data["movies"], list):
            movies = data["movies"]
        if isinstance(data["songs"], list):
            songs = data["songs"]
        if isinstance(data["books"], list):
            books = data["books"]
        
        for like_data in movies:
            likes.append(Like(user_id=like_data["user_id"], media_id=like_data["media_id"], type=like_data["type"], like_type=like_data["like_type"]))
        for like_data in songs:
            likes.append(Like(user_id=like_data["user_id"], media_id=like_data["media_id"], type=like_data["type"], like_type=like_data["like_type"]))
        for like_data in books:
            likes.append(Like(user_id=like_data["user_id"], media_id=like_data["media_id"], type=like_data["type"], like_type=like_data["like_type"]))

        return likes

async def GetLikesByMedia(id:str , media:str, preference: str = None) -> list[Like]:
    api_url = os.environ.get("LIKES_URL")
    likes_url = api_url + "/likes/media/" + id + "?media_type=" + media

    if preference != None and media == None:
        likes_url = likes_url + "&preference=" + preference
    
    async with httpx.AsyncClient() as client:
        response = await client.get(likes_url)
        data = response.json()
        likes = []
        likes_response = []

        if isinstance(data["likes"], list):
            likes_response = data["likes"]

        for like_data in likes_response:
            likes.append(Like(user_id=like_data["user_id"], media_id=like_data["media_id"], type=like_data["type"], like_type=like_data["like_type"]))

        return likes
    
async def GetSpecificLike(id:int , mediaID:str, mediaType: str) -> Like:
    api_url = os.environ.get("LIKES_URL")
    likes_url = api_url + "/likes?user_id=" + str(id) + "&media_type=" + mediaType + "&media_id=" + mediaID
    
    async with httpx.AsyncClient() as client:
        response = await client.get(likes_url)
        data = response.json()

        if response.status_code == 200:
            return Like(user_id=data["user_id"], media_id=data["media_id"], type=data["type"], like_type=data["like_type"])

        return None
  
async def GetWishlistByUserId(userID: int) -> list[Like]:
    api_url = os.environ.get("LIKES_URL")
    likes_url = api_url + "/likes/wishlist/" + str(userID)
    async with httpx.AsyncClient() as client:
        response = await client.get(likes_url)
        data = response.json()
        movies = []
        songs = []
        books = []
        movies_response = []
        songs_response = []
        books_response = []

        if isinstance(data["movies"], list):
            movies_response = data["movies"]
        if isinstance(data["songs"], list):
            songs_response = data["songs"]
        if isinstance(data["books"], list):
            books_response = data["books"]
        
        for like_data in movies_response:
            like = Like(user_id=like_data["user_id"], media_id=like_data["media_id"], type=like_data["type"], like_type=like_data["like_type"])
            media = Media(type=like_data["type"], id=like_data["media_id"], info="") ## @todo
            movies.append(LikeExtended(like=like, media=media))
        for like_data in songs_response:
            like = Like(user_id=like_data["user_id"], media_id=like_data["media_id"], type=like_data["type"], like_type=like_data["like_type"])
            media = Media(type=like_data["type"], id=like_data["media_id"], info="") ## @todo
            songs.append(LikeExtended(like=like, media=media))
        for like_data in books_response:
            like = Like(user_id=like_data["user_id"], media_id=like_data["media_id"], type=like_data["type"], like_type=like_data["like_type"])
            media = Media(type=like_data["type"], id=like_data["media_id"], info="") ## @todo
            books.append(LikeExtended(like=like, media=media))
        
        return Wishlist(user_id=userID, movies=movies, songs=songs, books=books)

async def GetRatingByMediaId(id: str, media: str, userID: str = None) -> float:
    api_url = os.environ.get("LIKES_URL")
    likes_url = api_url + "/likes/rate/" + str(id) + "?media_type=" + media

    if userID != None:
        likes_url = likes_url + "&user_id=" + userID

    async with httpx.AsyncClient() as client:
        response = await client.get(likes_url)
    return response.json()