import strawberry

@strawberry.type
class Payment:
    id_payment: int
    id_ad: int
    amount_payment: float
    created_time: str
    status_payment: str

@strawberry.type
class PaymentMessage:
    message: str
