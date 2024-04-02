# from app.GraphQL.Users.userTypes import User, UserToken, GoogleURL
import json
from app.GraphQL.Payments.paymentType import Payment
import httpx
import os

async def GetAllPayments() -> list[Payment]:
    api_url = os.environ.get("ADS_URL")
    payment_url = api_url + "payments/"
    async with httpx.AsyncClient() as payment_client:
        response = await payment_client.get(payment_url)
        data = response.json()
        # Turns every JSON on the list into a Payment object
        return [Payment(**payment_data) for payment_data in data]

async def GetSinglePayment(idPayment: int) -> Payment:
    api_url = os.environ.get("ADS_URL")
    print(api_url)
    payment_url = api_url + "payments/" + str(idPayment)
    async with httpx.AsyncClient() as payment_client:
        response = await payment_client.get(payment_url)
        print(response.text)
        data = response.json()
        # Turns the JSON into a Payment object
        return Payment(**data)

async def GetPaymentByCompany(companyID: int) -> list[Payment]:
    api_url = os.environ.get("ADS_URL")
    payment_url = api_url + "payments/"
    response = httpx.request(method="GET",url=payment_url, headers={"Content-Type": "application/json"},  content=json.dumps({"id_company" : companyID}))
    data = response.json()
    # Turns every JSON on the list into a Payment object
    return [Payment(**payment_data) for payment_data in data]


async def GetPaymentByAd(adID: int) -> list[Payment]:
    api_url = os.environ.get("ADS_URL")
    payment_url = api_url + "payments/"
    response = httpx.request(method="GET",url=payment_url, headers={"Content-Type": "application/json"},  content=json.dumps({"id_ad" : adID}))
    data = response.json()
    # Turns every JSON on the list into a Payment object
    return [Payment(**payment_data) for payment_data in data]