import strawberry

@strawberry.type
class Like:
    media_id: str
    user_id: int
    type: str
    like_type: str
class Media:
    type: str
    id: str
    info: str
class LikeExtended:
    like: Like
    media: Media
class Wishlist:
    user_id: int
    movies: list[LikeExtended]
    songs: list[LikeExtended]
    books: list[LikeExtended]