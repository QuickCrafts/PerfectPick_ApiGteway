import httpx
import os

from app.GraphQL.Users.userTypes import Other

async def LikeMedia(id:int, mediaId:str, type:str) -> Other:
    api_url = os.environ.get("LIKES_URL")
    like_url = api_url + "/likes"
    async with httpx.AsyncClient() as client:
        response = await client.post(
            like_url, 
            headers={"Content-Type": "application/json"}, 
            json={
                "user_id": id, 
                "media_id": mediaId,
                "media_type": type,
                "like_type": "LK"})
        if response.status_code == 201:
            return Other(message=response.text)
        else:
            return None

async def DislikeMedia(id:int, mediaId:str, type:str) -> Other:
    api_url = os.environ.get("LIKES_URL")
    like_url = api_url + "/likes"
    async with httpx.AsyncClient() as client:
        response = await client.post(
            like_url, 
            headers={"Content-Type": "application/json"}, 
            json={
                "user_id": id, 
                "media_id": mediaId,
                "media_type": type,
                "like_type": "DLK"})
        if response.status_code == 201:
            return Other(message=response.text)
        else:
            return None
        
async def DeletePreference(id:int, mediaId:str, type:str) -> Other:
    api_url = os.environ.get("LIKES_URL")
    like_url = api_url + "/likes?user_id=" + str(id) + "&media_id=" + mediaId + "&media_type=" + type
    async with httpx.AsyncClient() as client:
        response = await client.delete(like_url)
        if response.status_code == 204:
            return Other(message='Deleted')
        else:
            return None

async def AddToWishlist(id:int, mediaId:str, type:str) -> Other:
    api_url = os.environ.get("LIKES_URL")
    like_url = api_url + "/likes/wishlist/" + str(id)
    async with httpx.AsyncClient() as client:
        response = await client.post(
            like_url, 
            headers={"Content-Type": "application/json"}, 
            json={
                "media_id": mediaId, 
                "media_type": type, 
                "type": "ADD"})
        if response.status_code == 201:
            return Other(message=response.text)
        else:
            return None
        
async def RemoveFromWishlist(id:int, mediaId:str, type:str) -> Other:
    api_url = os.environ.get("LIKES_URL")
    like_url = api_url + "/likes/wishlist/" + str(id)
    async with httpx.AsyncClient() as client:
        response = await client.post(
            like_url, 
            headers={"Content-Type": "application/json"}, 
            json={
                "media_id": mediaId, 
                "media_type": type, 
                "type": "RMV"})
        if response.status_code == 201:
            return Other(message=response.text)
        else:
            return None

async def RatingMedia(id:int, mediaId:str, type:str, rating:int) -> Other:
    api_url = os.environ.get("LIKES_URL")
    like_url = api_url + "/likes/rate" + str(mediaId)
    async with httpx.AsyncClient() as client:
        response = await client.post(like_url, headers={"Content-Type": "application/json"}, json={"id": id, "mediaId": mediaId})
        if response.status_code == 500:
            return None
        return Other(message=response.text)