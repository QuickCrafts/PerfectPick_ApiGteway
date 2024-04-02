from app.GraphQL.Users.userTypes import UserToken, Other
import httpx
import os
import strawberry

# USER ONLY MUTATIONS

async def RegisterUser(email: str, password: str, firstName: str, lastName: str, birthdate: str, role: bool) -> UserToken:
    api_url = os.environ.get("USERS_URL")
    auth_url = api_url + "/Users"
    async with httpx.AsyncClient() as client:
        response = await client.post(auth_url, headers={"Content-Type": "application/json"}, json={"email": email, "password": password, "firstName": firstName, "lastName": lastName, "birthdate": birthdate, "role": role})
        if response.status_code == 500:
            return None
        return Other(message=response.text)
    
async def VerifyAccount(token:str) -> Other:
    api_url = os.environ.get("USERS_URL")
    auth_url = api_url + "/Users/verify"
    async with httpx.AsyncClient() as client:
        response = await client.post(auth_url, params={"userToken": token})
        if response.status_code == 500:
            return None
        return Other(message=response.text)
    
async def ForgottenPasswordReset(token:str, newPassword:str) -> Other:
    api_url = os.environ.get("USERS_URL")
    auth_url = api_url + "/Users/auth/recover"
    async with httpx.AsyncClient() as client:
        response = await client.post(auth_url, headers={"Content-Type": "application/json"}, json={"newPassword": newPassword}, params={"verificationToken": token})
        if response.status_code == 500:
            return None
        return Other(message=response.text)
    
async def ChangePassword(email:str  ,oldPassword:str, newPassword:str) -> Other:
    api_url = os.environ.get("USERS_URL")
    auth_url = api_url + "/Users/auth/change"
    async with httpx.AsyncClient() as client:
        response = await client.post(auth_url, headers={"Content-Type": "application/json"}, json={ "email": email,"oldPassword": oldPassword, "newPassword": newPassword})
        if response.status_code == 500:
            return None
        return Other(message=response.text)
    
async def UpdateUser(id:int ,firstName:str = None, lastName:str = None, birthdate:str = None, avatarUrl:str = None, gender:str = None, countryId:str  = None) -> Other:
    api_url = os.environ.get("USERS_URL")
    auth_url = api_url + "/Users/" + str(id)
    async with httpx.AsyncClient() as client:
        response = await client.put(auth_url, headers={"Content-Type": "application/json"}, json={"firstName": firstName, "lastName": lastName, "birthdate": birthdate, "avatarUrl": avatarUrl, "gender":gender, "countryId":countryId})
        if response.status_code == 500:
            return None
        return Other(message=response.text)
    
async def CompleteSetup(id:id) -> Other:
    api_url = os.environ.get("USERS_URL")
    auth_url = api_url + "/Users/setup"
    async with httpx.AsyncClient() as client:
        response = await client.post(auth_url, headers={"Content-Type": "application/json"}, params={"id": id})
        if response.status_code == 500:
            return None
        return Other(message=response.text)
    
async def DeleteUser(id:int) -> Other:
    api_url = os.environ.get("USERS_URL")
    auth_url = api_url + "/Users/" + str(id)
    # DELETE User from Users Database
    async with httpx.AsyncClient() as client:
        response = await client.delete(auth_url)
        if response.status_code == 500:
            raise ValueError("User couldn't be deleted")
    
    # DELETE User likes
    likes_api_url = os.environ.get("LIKES_URL")
    likes_api_url = likes_api_url + "/likes/user/" + str(id)
    async with httpx.AsyncClient() as client:
        response = await client.delete(likes_api_url)
        if response.status_code == 500:
            raise ValueError("User likes couldn't be deleted")
        
    # DELETE User recommendations
    recommends_api_url = os.environ.get("RECOMMS_URL")
    recommends_api_url = recommends_api_url + "/recommendation/" + str(id)
    async with httpx.AsyncClient() as client:
        response = await client.delete(likes_api_url)
        if response.status_code == 500:
            raise ValueError("User recommendations couldn't be deleted")
        
    # DELETE User Ad info
    ads_api_url = os.environ.get("ADS_URL")
    ads_api_url = ads_api_url + "/ads/user/" + str(id)
    async with httpx.AsyncClient() as client:
        response = await client.delete(ads_api_url)
        if response.status_code == 500:
            raise ValueError("User ads couldn't be deleted")
        
    return Other(message="User deleted successfully")

# COUNTRY MUTATIONS

async def CreateCountry(name:str, code_2:str, code_3:str) -> Other:
    api_url = os.environ.get("USERS_URL")
    auth_url = api_url + "/Country"
    async with httpx.AsyncClient() as client:
        response = await client.post(auth_url, headers={"Content-Type": "application/json"}, json={"name": name, "code_2": code_2, "code_3": code_3})
        if response.status_code == 500:
            return None
        return Other(message=response.text)
    
async def UpdateCountry(id:int, name:str = None, code_2:str = None, code_3:str = None) -> Other:
    api_url = os.environ.get("USERS_URL")
    auth_url = api_url + "/Country/" + str(id)
    async with httpx.AsyncClient() as client:
        response = await client.put(auth_url, headers={"Content-Type": "application/json"}, json={"name": name, "code_2": code_2, "code_3": code_3})
        if response.status_code == 500:
            return None
        return Other(message=response.text)
    
async def DeleteCountry(id:int) -> Other:
    api_url = os.environ.get("USERS_URL")
    auth_url = api_url + "/Country/" + str(id)
    async with httpx.AsyncClient() as client:
        response = await client.delete(auth_url)
        if response.status_code == 500:
            return None
        return Other(message=response.text)
    
async def ImportCountryData() -> Other:
    api_url = os.environ.get("USERS_URL")
    auth_url = api_url + "/Country"
    async with httpx.AsyncClient() as client:
        response = await client.put(auth_url)
        if response.status_code == 500:
            return None
        return Other(message=response.text)