import httpx
import os

from app.GraphQL.Users.userTypes import Other

async def PublishAd(adID: int) -> Other:
    api_url = os.environ.get("ADS_URL")
    ads_url = api_url + "ads/publish/" + str(adID)
    async with httpx.AsyncClient() as client:
        response = await client.post(ads_url)
        if response.status_code == 500:
            return None
        data = response.json()
        return Other(message=data.get("message"))