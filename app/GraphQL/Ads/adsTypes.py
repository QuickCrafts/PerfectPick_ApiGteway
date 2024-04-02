import strawberry

@strawberry.type
class Company:
    company_id:int
    name:str
    email:str

@strawberry.type
class Ad:
    ad_id: int
    name: str
    ad_url: str # Bucket url to display ad image
    start_date: str #timestamp of start date to publish ad
    end_date: str # timestamp of end date to publish ad
    create_date: str # timestamp of ad creation
    description: str
    company: int
    published: bool

@strawberry.type
class AdMessage:
    message: str