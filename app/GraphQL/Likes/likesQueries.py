import httpx
import os
from app.GraphQL.Likes.likesTypes import Like

async def GetLikesById(adID: int) -> list[Like]:
    api_url = os.environ.get("LIKES_URL")
    ads_url = api_url + "likes/user/"
    # ads_url = api_url + "likes/user/" + str(adID) + "/
    async with httpx.AsyncClient() as client:
        response = await client.get(ads_url, params={"id_ad": adID})
        # response = await client.get(ads_url)
        data = response.json()
        return [Like(**like_data) for like_data in data]

async def GetLikesByMedia(id:int , media:str , preference: str) -> list[Like]:
    api_url = os.environ.get("LIKES_URL")
    ads_url = api_url + "likes/media/"
    async with httpx.AsyncClient() as client:
        response = await client.get(ads_url, params={"id": id})
        data = response.json()
        return [Like(**like_data) for like_data in data]
  
async def GetWishlistByUserId(userID: int) -> list[Like]:
    api_url = os.environ.get("LIKES_URL")
    ads_url = api_url + "likes/wishlist/"
    async with httpx.AsyncClient() as client:
        response = await client.get(ads_url, params={"id_user": userID})
        data = response.json()
        return [Like(**like_data) for like_data in data]

# async def GetMoviesInfo(idMovie: int) -> list[Movie]:
#     api_url = os.environ.get("CATALOG_URL")
#     ads_url = api_url + "movies/"
#     async with httpx.AsyncClient() as client:
#         response = await client.get(ads_url, params={"id": idMovie})
#         data = response.json()
#         return [Movie(**movie_data) for movie_data in data]
  
# async def GetBooksInfo(idBook: int) -> list[Book]:
#     api_url = os.environ.get("CATALOG_URL")
#     ads_url = api_url + "books/"
#     async with httpx.AsyncClient() as client:
#         response = await client.get(ads_url, params={"id": idBook})
#         data = response.json()
#         return [Book(**like_data) for like_data in data]
  # async def GetSongsInfo(idSong: int) -> list[Song]:
  #   api_url = os.environ.get("CATALOG_URL")
  #   ads_url = api_url + "songs/"
  #   async with httpx.AsyncClient() as client:
  #       response = await client.get(ads_url, params={"id": idSong})
  #       data = response.json()
  #       return [Song(**like_data) for like_data in data]