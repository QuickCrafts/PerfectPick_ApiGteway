from app.GraphQL.Users.userTypes import User, UserToken, GoogleURL
import httpx
import os



async def GetAllUsers() -> list[User]:
    api_url = os.environ.get("USERS_URL")
    auth_url = api_url + "/Users"
    async with httpx.AsyncClient() as client:
        response = await client.get(auth_url)
        data = response.json()
        # Turns every JSON on the list into a User object
        return [User(**user_data) for user_data in data]
    

async def GetSingleUser(userID: int) -> User:
    api_url = os.environ.get("USERS_URL")
    auth_url = api_url + "/Users"
    async with httpx.AsyncClient() as client:
        response = await client.get(auth_url, params={"userID": userID})
        if response.status_code == 404:
            return None
        data = response.json()
        # Turns the JSON into a User object
        return User(**data)
    
async def EmailLogin(email: str, password: str) -> UserToken:
    api_url = os.environ.get("USERS_URL")
    auth_url = api_url + "/Users/Login"
    async with httpx.AsyncClient() as client:
        response = await client.post(auth_url, headers={"Content-Type": "application/json"}, json={"email": email, "password": password})
        if response.status_code == 500:
            return None
        return UserToken(token=response.text)
    
async def GoogleLogin() -> UserToken:
    api_url = os.environ.get("USERS_URL")
    auth_url = api_url + "/Users/GoogleLogin"
    async with httpx.AsyncClient() as client:
        response = await client.get(auth_url)
        if response.status_code == 500:
            return None
        return GoogleURL(url=response.url)
