import json
import httpx
import os
from app.GraphQL.Likes.likesTypes import Like

async def GetLikesById(adID: int) -> list[Like]:
    api_url = os.environ.get("LIKES_URL")
    # likes_url = api_url + "likes/user/"
    likes_url = api_url + "likes/user/" + str(adID)
    async with httpx.AsyncClient() as client:
        # response = await client.get(likes_url, params={"id_ad": adID})
        response = await client.get(likes_url)
        data = response.json()
        return [Like(**like_data) for like_data in data]

async def GetLikesByMedia(id:int , media:str , preference: str) -> list[Like]:
    api_url = os.environ.get("LIKES_URL")
    likes_url = api_url + "likes/media/" + str(id)
    async with httpx.AsyncClient() as client:
        response = await client.get(likes_url)
        data = response.json()
        return [Like(**like_data) for like_data in data]
  
async def GetWishlistByUserId(userID: int) -> list[Like]:
    api_url = os.environ.get("LIKES_URL")
    likes_url = api_url + "likes/wishlist/" + str(userID)
    async with httpx.AsyncClient() as client:
        response = await client.get(likes_url)
        data = response.json()
        return [Like(**like_data) for like_data in data]

# async def GetMoviesInfo(idMovie: int) -> list[Movie]:
#     api_url = os.environ.get("CATALOG_URL")
#     likes_url = api_url + "movies/"
#     async with httpx.AsyncClient() as client:
#         response = await client.get(likes_url, params={"id": idMovie})
#         data = response.json()
#         return [Movie(**movie_data) for movie_data in data]
  
# async def GetBooksInfo(idBook: int) -> list[Book]:
#     api_url = os.environ.get("CATALOG_URL")
#     likes_url = api_url + "books/"
#     async with httpx.AsyncClient() as client:
#         response = await client.get(likes_url, params={"id": idBook})
#         data = response.json()
#         return [Book(**like_data) for like_data in data]
    
# async def GetSongsInfo(idSong: int) -> list[Song]:
#   api_url = os.environ.get("CATALOG_URL")
#   likes_url = api_url + "songs/"
#   async with httpx.AsyncClient() as client:
#       response = await client.get(likes_url, params={"id": idSong})
#       data = response.json()
#       return [Song(**like_data) for like_data in data]

async def GetRaitingByMediaId(id: int, media: str) -> float:
    api_url = os.environ.get("LIKES_URL")
    likes_url = api_url + "likes/rate/" + str(id)
    response = httpx.request(method="GET",url=likes_url, headers={"Content-Type": "application/json"},  content=json.dumps({"media_type": media}))
    return response