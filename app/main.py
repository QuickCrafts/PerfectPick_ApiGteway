import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL
from starlette.middleware.cors import CORSMiddleware
from app.GraphQL.Users.userQueries import GetAllUsers, GetSingleUser
from app.GraphQL.Users.userTypes import User
from dotenv import load_dotenv
from app.utils import Authenticate

load_dotenv()




@strawberry.type
class Other:
    name: str

@strawberry.type
class UserToken:
    isTokenValid: bool
    Code: int


@strawberry.type
class Query:
    @strawberry.field
    async def GetAllUsersGQL(self) -> list[User]:
        return await GetAllUsers()
    
    @strawberry.field
    async def GetSingleUserGQL(self, userID: int) -> User:
        potentialData = await GetSingleUser(userID=userID)
        if potentialData is None:
            raise ValueError("User not found")
        else:
            return potentialData

    @strawberry.field
    async def Authenticate(self, userToken: str) -> UserToken:
        result = await Authenticate(userToken)
        return UserToken(isTokenValid=result["isTokenValid"], Code=result["Code"])


schema = strawberry.Schema(query=Query)


graphql_app = GraphQL(schema)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)

# Syntax for HTTP requests to Microservices
@app.get("/Users")
async def testFetch():
    return await Authenticate("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjZXJ0c2VyaWFsbnVtYmVyIjoiMmo2Mm9PQUNya1BBbWc2SS9WV2Q3QT09IiwibmJmIjoxNzExMzg3MTc4LCJleHAiOjE3MTE0MDE1NzgsImlhdCI6MTcxMTM4NzE3OH0.g-_vB7PcG4_BqU-m1qQGXtUDcSeWfcTZhV6boBRJP9Q")

