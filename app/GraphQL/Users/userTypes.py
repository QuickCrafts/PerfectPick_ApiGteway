import strawberry

@strawberry.type
class User:
    idUser: int
    email: str
    password: str
    firstName: str
    lastName: str
    birthdate: str
    role: bool
    avatarUrl: str
    createdTime: str
    verified: bool
    setup: bool

@strawberry.type
class UserToken:
    token: str