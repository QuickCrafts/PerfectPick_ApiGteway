from app.GraphQL.Users.userTypes import User, UserToken, GoogleURL, Country
import httpx
import os


# USER ONLY QUERIES

async def GetAllUsers() -> list[User]:
    api_url = os.environ.get("USERS_URL")
    auth_url = api_url + "/Users"
    async with httpx.AsyncClient() as client:
        response = await client.get(auth_url)
        data = response.json()
        users = []
        for user in data:
            countryID = user["countryId"]
            if countryID != None:
                async with httpx.AsyncClient() as client:
                    country_response = await client.get(api_url + "/Country/" + countryID)
                    country_data = country_response.json()
                    countryName = country_data["name"]
            else:
                countryName = "NaN"
            users.append(User(idUser=user["idUser"], email=user["email"], password=user["password"], firstName=user["firstName"], lastName=user["lastName"], birthdate=user["birthdate"], role=user["role"], avatarUrl=user["avatarUrl"], createdTime=user["createdTime"], verified=user["verified"], setup=user["setup"], country=countryName))
        return users
    

async def GetSingleUser(userID: int) -> User:
    api_url = os.environ.get("USERS_URL")
    auth_url = api_url + "/Users"
    async with httpx.AsyncClient() as client:
        response = await client.get(auth_url, params={"userID": userID})
        if response.status_code == 404:
            return None
        data = response.json()
        
        countryID = data["countryId"]
        if countryID != None:
            async with httpx.AsyncClient() as client:
                country_response = await client.get(api_url + "/Country/" + countryID)
                country_data = country_response.json()
                countryName = country_data["name"]
        else:
            countryName = "NaN"
        return User(idUser=data["idUser"], email=data["email"], password=data["password"], firstName=data["firstName"], lastName=data["lastName"], birthdate=data["birthdate"], role=data["role"], avatarUrl=data["avatarUrl"], createdTime=data["createdTime"], verified=data["verified"], setup=data["setup"], country=countryName)
    
async def GetSingleUserByEmail(email: str) -> User:
    api_url = os.environ.get("USERS_URL")
    auth_url = api_url + "/Users/Email/" + email
    async with httpx.AsyncClient() as client:
        response = await client.get(auth_url)
        print(auth_url)
        print(response.text)
        if response.status_code == 404:
            return None
        data = response.json()
        
        countryID = data["countryId"]
        if countryID != None:
            async with httpx.AsyncClient() as client:
                country_response = await client.get(api_url + "/Country/" + countryID)
                country_data = country_response.json()
                countryName = country_data["name"]
        else:
            countryName = "NaN"
        return User(idUser=data["idUser"], email=data["email"], password=data["password"], firstName=data["firstName"], lastName=data["lastName"], birthdate=data["birthdate"], role=data["role"], avatarUrl=data["avatarUrl"], createdTime=data["createdTime"], verified=data["verified"], setup=data["setup"], country=countryName)
    

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
    
# COUNTRY QUERIES
    
async def GetAllCountries() -> list[Country]:
    api_url = os.environ.get("USERS_URL")
    auth_url = api_url + "/Country"
    async with httpx.AsyncClient() as client:
        response = await client.get(auth_url)
        data = response.json()
        return [Country(**country_data) for country_data in data]
    
async def GetSingleCountry(countryID: int) -> Country:
    api_url = os.environ.get("USERS_URL")
    auth_url = api_url + "/Country/" + str(countryID)
    async with httpx.AsyncClient() as client:
        response = await client.get(auth_url)
        if response.status_code == 404:
            raise ValueError("Country not found")
        elif response.status_code == 500:
            raise ValueError("Internal Server Error")
        data = response.json()
        return Country(**data)

async def PasswordReset(email: str) -> str:
    api_url = os.environ.get("USERS_URL")
    auth_url = api_url + "/Users/auth/forgot/" + email
    async with httpx.AsyncClient() as client:
        response = await client.post(auth_url)
        if response.status_code == 500:
            return None
        return response.text
    
async def SendContactEmail(email: str, name: str, message: str) -> str:
    api_url = os.environ.get("USERS_URL")
    auth_url = api_url + "/Users/contact"
    async with httpx.AsyncClient() as client:
        response = await client.post(auth_url, headers={"Content-Type": "application/json"}, json={"email": email, "name": name, "message": message})
        if response.status_code == 500:
            return None
        return response.text
    
async def VerifyGetId(token: str) -> int:
    api_url = os.environ.get("USERS_URL")
    auth_url = api_url + "/Users/verify/" + token
    async with httpx.AsyncClient() as client:
        response = await client.get(auth_url)
        if response.status_code == 500 or response.status_code == 404 or response.status_code == 401: 
            return None
        elif response.status_code == 200:
            data = response.json()
            return int(data["id"])
        