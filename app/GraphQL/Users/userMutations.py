from app.GraphQL.Users.userTypes import UserToken, Other
import httpx
import os
import strawberry

async def RegisterUser(email: str, password: str, firstName: str, lastName: str, birthdate: str, role: bool) -> UserToken:
    api_url = os.environ.get("USERS_URL")
    auth_url = api_url + "/Users"
    async with httpx.AsyncClient() as client:
        response = await client.post(auth_url, headers={"Content-Type": "application/json"}, json={"email": email, "password": password, "firstName": firstName, "lastName": lastName, "birthdate": birthdate, "role": role})
        if response.status_code == 500:
            return None
        return UserToken(token=response.text)
    
async def VerifyAccount(token:str) -> Other:
    api_url = os.environ.get("USERS_URL")
    auth_url = api_url + "/Users/verify"
    async with httpx.AsyncClient() as client:
        response = await client.post(auth_url, params={"userToken": token})
        if response.status_code == 500:
            return None
        return Other(message=response.text)