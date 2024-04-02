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
        for like_data in data["movies"]:
            likes.append(Like(user_id=like_data["user_id"], media_id=like_data["media_id"], type=like_data["type"], like_type=like_data["like_type"]))
        for like_data in data["songs"]:
            likes.append(Like(user_id=like_data["user_id"], media_id=like_data["media_id"], type=like_data["type"], like_type=like_data["like_type"]))
        for like_data in data["books"]:
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
        for like_data in data["likes"]:
            likes.append(Like(user_id=like_data["user_id"], media_id=like_data["media_id"], type=like_data["type"], like_type=like_data["like_type"]))

        return likes
  
async def GetWishlistByUserId(userID: int) -> list[Like]:
    api_url = os.environ.get("LIKES_URL")
    likes_url = api_url + "/likes/wishlist/" + str(userID)
    async with httpx.AsyncClient() as client:
        response = await client.get(likes_url)
        data = response.json()
        movies = []
        songs = []
        books = []
        
        for like_data in data["movies"]:
            like = Like(user_id=like_data["user_id"], media_id=like_data["media_id"], type=like_data["type"], like_type=like_data["like_type"])
            media = Media(type=like_data["type"], id=like_data["media_id"], info="") ## @todo
            movies.append(LikeExtended(like=like, media=media))
        for like_data in data["songs"]:
            like = Like(user_id=like_data["user_id"], media_id=like_data["media_id"], type=like_data["type"], like_type=like_data["like_type"])
            media = Media(type=like_data["type"], id=like_data["media_id"], info="") ## @todo
            songs.append(LikeExtended(like=like, media=media))
        for like_data in data["books"]:
            like = Like(user_id=like_data["user_id"], media_id=like_data["media_id"], type=like_data["type"], like_type=like_data["like_type"])
            media = Media(type=like_data["type"], id=like_data["media_id"], info="") ## @todo
            books.append(LikeExtended(like=like, media=media))
        
        return Wishlist(user_id=userID, movies=movies, songs=songs, books=books)

async def GetRatingByMediaId(id: str, media: str) -> float:
    api_url = os.environ.get("LIKES_URL")
    likes_url = api_url + "/likes/rate/" + str(id) + "?media_type=" + media
    async with httpx.AsyncClient() as client:
        response = await client.get(likes_url)
    return response.json()