import strawberry

@strawberry.type
class MovieRecommendation:
    id: strawberry.ID
    id_user: str
    movies: list[str]
    books: list[str]
    songs: list[str]

@strawberry.type
class RecommendationResponse:
    message: str

@strawberry.input
class CreateRecommendationInput:
    user_id: int

@strawberry.type
class RecommendationResponse:
    message: str