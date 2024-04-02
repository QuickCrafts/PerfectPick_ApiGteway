from app.GraphQL.Ads.adsTypes import Ad, Company, AdMessage
import httpx
import os

async def CreateAd(id_ad:int, name_ad:str, ad_url:str, start_date_ad:str, end_date_ad:str, description_ad:str, id_company:int, published_ad:bool) -> AdMessage:
    api_url = os.environ.get("ADS_URL")
    auth_url = api_url + "/ads"
    async with httpx.AsyncClient() as client:
        response = await client.post(auth_url,headers={"Content-Type": "application/json"}, json={"id_ad":id_ad, "name_ad":name_ad, "ad_url":ad_url, "start_date_ad":start_date_ad, "end_date_ad":end_date_ad, "description_ad":description_ad, "id_company":id_company, "published_ad":published_ad})
        data = response.json()
        return AdMessage(message=data["message"])
    
async def UpdateAd(id_ad:int, name_ad:str=None, ad_url:str=None, start_date_ad:str=None, end_date_ad:str=None, description_ad:str=None, id_company:int=None, published_ad:bool=None) -> AdMessage:
    api_url = os.environ.get("ADS_URL")
    auth_url = api_url + "/ads"
    async with httpx.AsyncClient() as client:
        response = await client.put(auth_url,headers={"Content-Type": "application/json"}, json={"id_ad":id_ad, "name_ad":name_ad, "ad_url":ad_url, "start_date_ad":start_date_ad, "end_date_ad":end_date_ad, "description_ad":description_ad, "id_company":id_company, "published_ad":published_ad})
        if response.status_code == 500:
            return AdMessage(message="Ad couldn't be updated")
        if response.status_code == 404:
            return AdMessage(message="Ad not found")
        data = response.json()
        return AdMessage(message=data["message"])
    
async def DeleteAd(id_ad:int) -> AdMessage:
    api_url = os.environ.get("ADS_URL")
    auth_url = api_url + "/ads/" + str(id_ad)
    async with httpx.AsyncClient() as client:
        response = await client.delete(auth_url)
        if response.status_code == 500:
            return AdMessage(message="Ad couldn't be deleted")
        if response.status_code == 404:
            return AdMessage(message="Ad not found")
        data = response.json()
        return AdMessage(message=data["message"])