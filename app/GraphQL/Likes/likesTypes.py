import strawberry

@strawberry.type
class Like:
    id_like: int
    id_user: int
    id_ad: int
    created_time: str