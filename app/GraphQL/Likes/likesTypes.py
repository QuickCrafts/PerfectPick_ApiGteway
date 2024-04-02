import strawberry

@strawberry.type
class Like:
    id: int
    user_id: int
    type: str
    rating: float
    like_type: str
    wishlist: bool
class Media:
    type: str
    id: int
    info: str
class LikeExtended:
    like: Like
    media: Media
class Wishlist:
    user_id: int
    movies: list[LikeExtended]
    songs: list[LikeExtended]
    books: list[LikeExtended]