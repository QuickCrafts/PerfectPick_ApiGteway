from app.GraphQL.Companies.companiesType import Company, CompanyId
import httpx
import os


async def CreateCompany(name: str, email: str) -> CompanyId:
    api_url = os.environ.get("ADS_URL")
    companies_url = api_url + "companies/"
    async with httpx.AsyncClient() as client:
        response = await client.post(companies_url, headers={"Content-Type": "application/json"}, json={"name": name, "email": email})
        if response.status_code == 500:
            return None
        data = response.json()
        return CompanyId(id=data.get("id"))
    
async def UpdatedCompany(companyId:int, name: str, email: str) -> CompanyId:
    api_url = os.environ.get("ADS_URL")
    companies_url = api_url + "companies/" + str(companyId)
    async with httpx.AsyncClient() as client:
        response = await client.put(companies_url, headers={"Content-Type": "application/json"}, json={"name": name, "email": email})
        if response.status_code == 500:
            return None
        data = response.json()
        return CompanyId(id=data.get("id"))