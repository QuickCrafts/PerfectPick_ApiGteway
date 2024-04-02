import httpx
import os

from app.GraphQL.Users.userTypes import Other

async def LikeMedia(id:int, mediaId:int, type:str) -> Other:
    api_url = os.environ.get("LIKES_URL")
    like_url = api_url + "/likes"
    async with httpx.AsyncClient() as client:
        response = await client.post(like_url, headers={"Content-Type": "application/json"}, json={"id": id, "mediaId": mediaId, "type": type})
        if response.status_code == 500:
            return None
        return Other(message=response.text)

async def DislikeMedia(id:int, mediaId:int, type:str) -> Other:
    api_url = os.environ.get("LIKES_URL")
    like_url = api_url + "/likes"
    async with httpx.AsyncClient() as client:
        response = await client.post(like_url, headers={"Content-Type": "application/json"}, json={"id": id, "mediaId": mediaId, "type": type})
        if response.status_code == 500:
            return None
        return Other(message=response.text)

async def DeletePreference(id:int, mediaId:int, type:str) -> Other:
    api_url = os.environ.get("LIKES_URL")
    like_url = api_url + "/likes"
    async with httpx.AsyncClient() as client:
        response = await client.delete(like_url, headers={"Content-Type": "application/json"}, json={"id": id, "mediaId": mediaId, "type": type})
        if response.status_code == 500:
            return None
        return Other(message=response.text)

async def RatingMedia(id:int, mediaId:int, type:str, rating:int) -> Other:
    api_url = os.environ.get("LIKES_URL")
    like_url = api_url + "/likes/rate" + str(mediaId)
    async with httpx.AsyncClient() as client:
        response = await client.post(like_url, headers={"Content-Type": "application/json"}, json={"id": id, "mediaId": mediaId})
        if response.status_code == 500:
            return None
        return Other(message=response.text)