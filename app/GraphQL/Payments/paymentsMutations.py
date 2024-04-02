from app.GraphQL.Payments.paymentType import PaymentMessage
import httpx
import os

async def CreateBill(id_ad:int, amount:float) -> PaymentMessage:
    api_url = os.environ.get("PAYMENTS_URL")
    auth_url = api_url + "/payments"
    async with httpx.AsyncClient() as client:
        response = await client.post(auth_url, headers={"Content-Type": "application/json"}, json={"id_ad": id_ad, "amount_payment": amount})
        if response.status_code == 500:
            return None
        return PaymentMessage(message=response.text)
    
async def PayBill(id_payment:int) -> PaymentMessage:
    api_url = os.environ.get("PAYMENTS_URL")
    auth_url = api_url + "/payments/pay" + str(id_payment)
    async with httpx.AsyncClient() as client:
        response = await client.put(auth_url)
        if response.status_code == 500:
            return None
        return PaymentMessage(message=response.text)
    
async def CancelBill(id_payment:int) -> PaymentMessage:
    api_url = os.environ.get("PAYMENTS_URL")
    auth_url = api_url + "/payments/cancel" + str(id_payment)
    async with httpx.AsyncClient() as client:
        response = await client.put(auth_url)
        if response.status_code == 500:
            return None
        return PaymentMessage(message=response.text)