from app.GraphQL.Ads.adsTypes import Ad, Company
import httpx
import os

async def GetUserAds(id:int) -> list[Ad]:
    api_url = os.environ.get("ADS_URL")
    auth_url = api_url + "/ads/active/" + str(id)
    async with httpx.AsyncClient() as client:
        response = await client.get(auth_url)
        if response.status_code == 404:
            return None
        data = response.json()
        print(data)
        ads = []
        for ad in data:
            print(ad)
            ads.append(Ad(ad_id=ad["id_ad"], name=ad["name_ad"], ad_url=ad["ad_url"], start_date=ad["start_date_ad"], end_date=ad["end_date_ad"], create_date=["create_date_ad"] ,description=ad["description_ad"], company=ad["id_company"], published=ad["published_ad"]))
        return ads
    
async def GetCompanyAds(com_id:int) -> list[Ad]:
    api_url = os.environ.get("ADS_URL")
    auth_url = api_url + "/ads"
    async with httpx.AsyncClient() as client:
        response = await client.get(auth_url, params={"company": com_id})
        print(response.text)
        if response.status_code == 404:
            return None
        data = response.json()
        ads = []
        for ad in data:
            ads.append(Ad(ad_id=ad["id_ad"], name=ad["name_ad"], ad_url=ad["ad_url"], start_date=ad["start_date_ad"], end_date=ad["end_date_ad"], create_date=["create_date_ad"], description=ad["description_ad"], company=ad["id_company"], published=ad["published_ad"]))
        return ads

async def GetAds(exact_date:bool, published:bool ,start_date:str=None, end_date:str=None) -> list[Ad]:
    api_url = os.environ.get("ADS_URL")
    auth_url = api_url + "/ads"
    async with httpx.AsyncClient() as client:
        response = await client.get(auth_url)
        if response.status_code == 404:
            return None
        data = response.json()
        ads = []
        return ads
    
async def GetCompanies() -> list[Company]:
    api_url = os.environ.get("ADS_URL")
    auth_url = api_url + "/companies"
    async with httpx.AsyncClient() as client:
        response = await client.get(auth_url)
        if response.status_code == 404:
            return None
        data = response.json()
        companies = []
        for company in data:
            companies.append(Company(company_id=company["id_company"], name=company["name_company"], email=company["email_company"]))
        return companies