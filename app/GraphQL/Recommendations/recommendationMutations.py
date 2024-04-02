import strawberry
import httpx
import pika
import json
from strawberry.types import Info
from app.GraphQL.Recommendations.recommendationTypes import MovieRecommendation
from app.GraphQL.Recommendations.recommendationTypes import RecommendationResponse,CreateRecommendationInput,RecommendationResponse


async def fetch_likes(user_id: int) -> dict:
    likes_service_url = f"http://PerfectPick_Likes_ms:3000/likes/user/{user_id}"
    async with httpx.AsyncClient() as client:
        response = await client.get(likes_service_url)
        if response.status_code == 200:
            data = response.json()
            # Extract media_ids for movies
            movie_ids = [movie['media_id'] for movie in data['movies']] if data['movies'] else []
            # Assuming similar structure for songs and books, repeat the process
            # For songs and books, if they're supposed to be lists and not null when empty
            song_ids = [song['media_id'] for song in data['songs']] if data['songs'] else []
            book_ids = [book['media_id'] for book in data['books']] if data['books'] else []
            
            # Construct the new response
            transformed_response = {
                "id_user": user_id,
                "movies": movie_ids,
                "songs": song_ids,
                "books": book_ids
            }
            return transformed_response
        else:
            return {}


'''
async def fetch_likes(user_id: int) -> dict:
    recommendation_data = {
        "id_user": user_id,
        "movies": ["tt0106941", "tt0118694"],
        "books": ["AYhxAQHUdCYC", "fyPsAAAAMAAJ"],
        "songs": ["3qhlB30KknSejmIvZZLjOD"]
    }
    
    return recommendation_data
'''