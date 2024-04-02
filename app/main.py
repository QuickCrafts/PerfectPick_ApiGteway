import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL
from starlette.middleware.cors import CORSMiddleware
from app.GraphQL.Users.userQueries import GetAllUsers, GetSingleUser,GetSingleUserByEmail ,EmailLogin, GoogleLogin, GetAllCountries,GetSingleCountry, PasswordReset
from app.GraphQL.Users.userMutations import RegisterUser, VerifyAccount, ForgottenPasswordReset, ChangePassword, UpdateUser, CompleteSetup, DeleteUser, CreateCountry, UpdateCountry, DeleteCountry, ImportCountryData
from app.GraphQL.Users.userTypes import User, UserToken, GoogleURL, Other, Country
from app.GraphQL.Ads.adsQueries import GetUserAds, GetCompanyAds, GetCompanies
from app.GraphQL.Ads.adsMutations import CreateAd, UpdateAd, DeleteAd
from app.GraphQL.Ads.adsTypes import Ad, AdMessage, Company
from dotenv import load_dotenv
from app.utils import Authenticate, CheckAdmin

load_dotenv()


@strawberry.type
class Query:
    @strawberry.field
    async def allUsers(self, userToken: str) -> list[User]:
        isTokenValid = await Authenticate(userToken)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        return await GetAllUsers()
    
    @strawberry.field
    async def userByID(self, userID: int, userToken: str) -> User:
        isTokenValid = await Authenticate(userToken)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        potentialData = await GetSingleUser(userID=userID)
        if potentialData is None:
            raise ValueError("User not found")
        else:
            return potentialData
        
    @strawberry.field
    async def userByEmail(self, email: str, userToken: str) -> User:
        isTokenValid = await Authenticate(userToken)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        potentialData = await GetSingleUserByEmail(email=email)
        if potentialData is None:
            raise ValueError("User not found")
        else:
            return potentialData
        
    @strawberry.field
    async def loginWithEmail(self, email: str, password: str) -> UserToken:
        userToken = await EmailLogin(email=email, password=password)
        if userToken is None:
            raise ValueError("User not found")
        else:
            return userToken
        
    @strawberry.field
    async def loginWithGoogle(self) -> GoogleURL:
        userToken = await GoogleLogin()
        if userToken is None:
            raise ValueError("User not found")
        else:
            return userToken
    
    @strawberry.field
    async def countryByID(self, countryID: int) -> Country:
        potentialData = await GetSingleCountry(countryID=countryID)
        return potentialData

    @strawberry.field
    async def allCountries(self) -> list[Country]:
        return await GetAllCountries()

    @strawberry.field
    async def forgotPassword(self, email: str) -> Other:
        await PasswordReset(email=email)
        return Other(message="Email sent to reset password")
    
    @strawberry.field
    async def getUserAds(self, token:str ,id: int) -> list[Ad]:
        isTokenValid = await Authenticate(token)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        ads = await GetUserAds(id=id)
        if ads is None:
            raise ValueError("Ads not found")
        else:
            return ads
        
    @strawberry.field
    async def getCompanyAds(self, token:str,id:int ,com_id: int) -> list[Ad]:
        isTokenValid = await Authenticate(token)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        isAdmin = await CheckAdmin(id=id)
        if isAdmin["isAdmin"] == False:
            raise ValueError("User is not an admin")
        ads = await GetCompanyAds(com_id=com_id)
        if ads is None:
            raise ValueError("Ads not found")
        else:
            return ads
        
    @strawberry.field
    async def getCompanies(self, token:str, id: int) -> list[Company]:
        isTokenValid = await Authenticate(token)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        isAdmin = await CheckAdmin(id=id)
        if isAdmin["isAdmin"] == False:
            raise ValueError("User is not an admin")
        return await GetCompanies()

@strawberry.type
class Mutation:
    @strawberry.field
    async def signUpUser(self, email: str, password: str, firstName: str, lastName: str, birthdate: str, role: bool) -> Other:
        userToken = await RegisterUser(email=email, password=password, firstName=firstName, lastName=lastName, birthdate=birthdate, role=role)
        if userToken is None:
            raise ValueError("User not found")
        else:
            return userToken
    
    @strawberry.field
    async def VerifyUser(self, token: str) -> Other:
        message = await VerifyAccount(token=token)
        if message is None:
            raise ValueError("User not found")
        else:
            return message
        
    @strawberry.field
    async def recoverPassword(self, token: str, newPassword: str) -> Other:
        message = await ForgottenPasswordReset(token=token, newPassword=newPassword)
        if message is None:
            raise ValueError("User not found")
        else:
            return message

    @strawberry.field
    async def changePassword(self, token:str, id: int ,email:str  ,oldPassword:str, newPassword:str) -> Other:
        isTokenValid = await Authenticate(token)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        message = await ChangePassword(email=email, oldPassword=oldPassword, newPassword=newPassword)
        return message     

    @strawberry.field
    async def updateUser(self,token:str, id:int ,firstName:str = None, lastName:str = None, birthdate:str = None, avatarUrl:str = None, gender:str = None, countryId:str  = None) -> Other:
        isTokenValid = await Authenticate(token)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        message = await UpdateUser( id=id,firstName=firstName, lastName=lastName, birthdate=birthdate, avatarUrl=avatarUrl, gender=gender, countryId=countryId)
        return message

    @strawberry.field   
    async def completeSetup(self,token:str, id:int) -> Other:
        isTokenValid = await Authenticate(token)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        message = await CompleteSetup(id=id)
        return message

    @strawberry.field
    async def deleteUser(self, token: str, id: int) -> Other:
        isTokenValid = await Authenticate(token)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        message = await DeleteUser(id=id)
        return message
        
    @strawberry.field
    async def createCountry(self,token:str, id: int) -> Other:
        isTokenValid = await Authenticate(token)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        isAdmin = await CheckAdmin(id=id)
        if isAdmin["isAdmin"] == False:
            raise ValueError("User is not an admin")
        message = await CreateCountry()
        return message
    
    @strawberry.field
    async def updateCountry(self,token:str, id: int) -> Other:
        isTokenValid = await Authenticate(token)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        isAdmin = await CheckAdmin(id=id)
        if isAdmin["isAdmin"] == False:
            raise ValueError("User is not an admin")
        message = await UpdateCountry()
        return message
    
    @strawberry.field
    async def deleteCountry(self,token:str, id: int) -> Other:
        isTokenValid = await Authenticate(token)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        isAdmin = await CheckAdmin(id=id)
        if isAdmin["isAdmin"] == False:
            raise ValueError("User is not an admin")
        message = await DeleteCountry()
        return message
    
    @strawberry.field
    async def importCountries(self,token:str, id: int) -> Other:
        isTokenValid = await Authenticate(token)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        isAdmin = await CheckAdmin(id=id)
        if isAdmin["isAdmin"] == False:
            raise ValueError("User is not an admin")
        message = await ImportCountryData()
        return message
    
    @strawberry.field
    async def createAd(self, id_ad:int, name_ad:str, ad_url:str, start_date_ad:str, end_date_ad:str, description_ad:str, id_company:int, published_ad:bool) -> AdMessage:
        message = await CreateAd(id_ad=id_ad, name_ad=name_ad, ad_url=ad_url, start_date_ad=start_date_ad, end_date_ad=end_date_ad, description_ad=description_ad, id_company=id_company, published_ad=published_ad)
        return message
    
    @strawberry.field
    async def updateAd(self, id_ad:int, name_ad:str=None, ad_url:str=None, start_date_ad:str=None, end_date_ad:str=None, description_ad:str=None, id_company:int=None, published_ad:bool=None) -> AdMessage:
        message = await UpdateAd(id_ad=id_ad, name_ad=name_ad, ad_url=ad_url, start_date_ad=start_date_ad, end_date_ad=end_date_ad, description_ad=description_ad, id_company=id_company, published_ad=published_ad)
        return message
    
    @strawberry.field
    async def deleteAd(self, id_ad:int) -> AdMessage:
        message = await DeleteAd(id_ad=id)
        return message
        
        


schema = strawberry.Schema(query=Query, mutation=Mutation)


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



