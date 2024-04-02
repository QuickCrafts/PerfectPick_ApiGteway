import httpx
import os


async def Authenticate(userToken: str):
    api_url = os.environ.get("USERS_URL")
    auth_url = api_url + "/Users/setup"
    async with httpx.AsyncClient() as client:
        response = await client.get(auth_url, params={"token": userToken})
        print(response.text)
        if response.status_code == 200:
            isTokenValid = True
        else:
            isTokenValid = False
        return{
            "isTokenValid": isTokenValid,
            "Code": response.status_code,
            "role": response.text.role,
        }

# async def CheckRole(userToken: str):
#     api_url = os.environ.get("USERS_URL")
#     auth_url = api_url + "/Users/setup"
#     api_url = os.environ.get("USERS_URL")
#     auth_url = api_url + "/Users/role"
#     async with httpx.AsyncClient() as client:
#         response = await client.get(auth_url, params={"idUser": idUser})
#         if response.status_code == 200:
#             role = response.text.role
#         else:
#             role = None
#         return role
