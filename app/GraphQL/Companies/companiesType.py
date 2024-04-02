import strawberry

@strawberry.type
class Company:
  id_company: int
  name_company : str
  email_company : str

@strawberry.type
class CompanyId:
  id: int