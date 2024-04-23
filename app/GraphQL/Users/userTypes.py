import strawberry
from typing import Optional

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
    country: str

@strawberry.type
class UserToken:
    token: str

@strawberry.type
class GoogleURL:
    url: str

@strawberry.type
class Other:
    message: str

@strawberry.type
class Country:
    id_country: int
    name: str
    code_2: str
    code_3: str

@strawberry.type
class UpdateUser:
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    birthdate: Optional[str] = None
    avatarUrl: Optional[str] = None
    gender: Optional[str] = None
    country: Optional[str] = None

@strawberry.type
class UserInfo:
    id:int

@strawberry.type
class OtherInt:
    id: int
