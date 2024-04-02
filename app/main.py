import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL
from starlette.middleware.cors import CORSMiddleware
from app.GraphQL.Companies.companiesMutations import CreateCompany, UpdatedCompany
from app.GraphQL.Companies.companiesType import CompanyId
from app.GraphQL.Release.releaseMutations import PublishAd
from app.GraphQL.Users.userQueries import GetAllUsers, GetSingleUser, EmailLogin, GoogleLogin
from app.GraphQL.Users.userMutations import RegisterUser, VerifyAccount
from app.GraphQL.Users.userTypes import User, UserToken, GoogleURL, Other
from app.GraphQL.Payments.paymentsQueries import GetAllPayments, GetPaymentByAd, GetPaymentByCompany, GetSinglePayment
from app.GraphQL.Payments.paymentsMutations import CreateBill, PayBill, CancelBill
from app.GraphQL.Payments.paymentType import Payment
from app.GraphQL.Users.userQueries import GetAllUsers, GetSingleUser,GetSingleUserByEmail ,EmailLogin, GoogleLogin, GetAllCountries,GetSingleCountry, PasswordReset
from app.GraphQL.Users.userMutations import RegisterUser, VerifyAccount, ForgottenPasswordReset, ChangePassword, UpdateUser, CompleteSetup, DeleteUser, CreateCountry, UpdateCountry, DeleteCountry, ImportCountryData
from app.GraphQL.Users.userTypes import User, UserToken, GoogleURL, Other, Country
from app.GraphQL.Ads.adsQueries import GetUserAds, GetCompanyAds, GetCompanies
from app.GraphQL.Ads.adsMutations import CreateAd, UpdateAd, DeleteAd
from app.GraphQL.Ads.adsTypes import Ad, AdMessage, Company
from dotenv import load_dotenv
from app.utils import Authenticate, CheckAdmin
from app.GraphQL.Recommendations.recommendationQueries import fetch_recommendations
from app.GraphQL.Recommendations.recommendationTypes import MovieRecommendation
from producers.recommendations_producer import send_recommendation
from app.GraphQL.Recommendations.recommendationMutations import CreateRecommendationInput, RecommendationResponse, fetch_likes


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
    async def getRecommendationsForUser(self, user_id: str) -> MovieRecommendation:
        return await fetch_recommendations(user_id)

        
    @strawberry.field
    async def BillsByCompanyId (self,  userToken: str ,companyID: int) -> list[Payment]:
        isTokenValid = await Authenticate(userToken)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        if isTokenValid["role"] != 1:
            raise ValueError("User not authorized")
        potentialData = await GetPaymentByCompany(companyID=companyID)
        if potentialData is None:
            raise ValueError("Bills not found")
        else:
            return potentialData
    
    @strawberry.field
    async def BillsByAdId (self,  userToken: str ,adID: int) -> list[Payment]:
        isTokenValid = await Authenticate(userToken)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        if isTokenValid["role"] != 1:
            raise ValueError("User not authorized")
        potentialData = await GetPaymentByAd(adID=adID)
        if potentialData is None:
            raise ValueError("Bills not found")
        else:
            return potentialData

    @strawberry.field
    async def AllBills (self,  userToken: str) -> list[Payment]:
        isTokenValid = await Authenticate(userToken)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        if isTokenValid["role"] != 1:
            raise ValueError("User not authorized")
        potentialData = await GetAllPayments()
        if potentialData is None:
            raise ValueError("Bills not found")
        else:
            return potentialData
    
    @strawberry.field
    async def BillById (self,  userToken: str, idPayment: int) -> Payment:
        isTokenValid = await Authenticate(userToken)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        if isTokenValid["role"] != 1:
            raise ValueError("User not authorized")
        potentialData = await GetSinglePayment(idPayment=idPayment)
        if potentialData is None:
            raise ValueError("Bill not found")
        else:
            return potentialData
    
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
    async def create_recommendation(input: CreateRecommendationInput) -> RecommendationResponse:
        likes_data = await fetch_likes(input.user_id)
        if likes_data:
            send_recommendation(likes_data)
            return RecommendationResponse(message="Recommendation process started successfully.")
        else:
            return RecommendationResponse(message="Failed to fetch likes data or send to RabbitMQ.")

    @strawberry.field
    async def CreateCompany(self,userToken: str, name: str, email: str) -> CompanyId:
        isTokenValid = await Authenticate(userToken)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        if isTokenValid["role"] != 1:
            raise ValueError("User not authorized")
        company = await CreateCompany(name=name, email=email)
        if company is None:
            raise ValueError("Company not created")
        else:
            return company

    @strawberry.field
    async def UpdateCompany (self, userToken: str, companyId:int, name: str, email: str) -> CompanyId:
        isTokenValid = await Authenticate(userToken)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        if isTokenValid["role"] != 1:
            raise ValueError("User not authorized")
        company = await UpdatedCompany(companyId=companyId, name=name, email=email)
        if company is None:
            raise ValueError("Company not updated")
        else:
            return company
        
    @strawberry.field
    async def PublishAd(self, userToken: str, adID: int) -> Other:
        isTokenValid = await Authenticate(userToken)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        if isTokenValid["role"] != 1:
            raise ValueError("User not authorized")
        publish = await PublishAd(adID=adID)
        
        return publish
    
    @strawberry.field
    async def createAd(self,token:str, id:int, id_ad:int, name_ad:str, ad_url:str, start_date_ad:str, end_date_ad:str, description_ad:str, id_company:int, published_ad:bool) -> AdMessage:
        isTokenValid = await Authenticate(token)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        isAdmin = await CheckAdmin(id=id)
        if isAdmin["isAdmin"] == False:
            raise ValueError("User is not an admin")
        message = await CreateAd(id_ad=id_ad, name_ad=name_ad, ad_url=ad_url, start_date_ad=start_date_ad, end_date_ad=end_date_ad, description_ad=description_ad, id_company=id_company, published_ad=published_ad)
        return message
    
    @strawberry.field
    async def updateAd(self,token:str,id:int ,id_ad:int, name_ad:str=None, ad_url:str=None, start_date_ad:str=None, end_date_ad:str=None, description_ad:str=None, id_company:int=None, published_ad:bool=None) -> AdMessage:
        isTokenValid = await Authenticate(token)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        isAdmin = await CheckAdmin(id=id)
        if isAdmin["isAdmin"] == False:
            raise ValueError("User is not an admin")
        message = await UpdateAd(id_ad=id_ad, name_ad=name_ad, ad_url=ad_url, start_date_ad=start_date_ad, end_date_ad=end_date_ad, description_ad=description_ad, id_company=id_company, published_ad=published_ad)
        return message
    
    @strawberry.field
    async def deleteAd(self,token:str, id:int ,id_ad:int) -> AdMessage:
        isTokenValid = await Authenticate(token)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        isAdmin = await CheckAdmin(id=id)
        if isAdmin["isAdmin"] == False:
            raise ValueError("User is not an admin")
        message = await DeleteAd(id_ad=id_ad)
        return message

    @strawberry.field
    async def createBill(self,token:str ,id_ad:int, amount:float) -> Payment:
        isTokenValid = await Authenticate(token)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")

        payment = await CreateBill(id_ad=id_ad, amount=amount)
        return payment
    
    @strawberry.field
    async def payBill(self,token:str, id_payment:int) -> Payment:
        isTokenValid = await Authenticate(token)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        payment = await PayBill(id_payment=id_payment)
        return payment
    
    @strawberry.field
    async def cancelBill(self,token:str, id_payment:int) -> Payment:
        isTokenValid = await Authenticate(token)
        if isTokenValid["isTokenValid"] == False:
            raise ValueError("Invalid Token, user not authorized")
        payment = await CancelBill(id_payment=id_payment)
        return payment


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



