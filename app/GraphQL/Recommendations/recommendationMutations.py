import strawberry
import httpx
import pika
import json
from strawberry.types import Info
from app.GraphQL.Recommendations.recommendationTypes import MovieRecommendation
from app.GraphQL.Recommendations.recommendationTypes import RecommendationResponse,CreateRecommendationInput,RecommendationResponse
from app.GraphQL.Recommendations.recommendationTypes import UpdateRecommendationInput

async def fetch_likes(user_id: int) -> dict:
    likes_service_url = f"http://PerfectPick_Likes_ms:3000/likes/user/{user_id}"
    async with httpx.AsyncClient() as client:
        response = await client.get(likes_service_url)
        if response.status_code == 200:
            data = response.json()
            movie_ids = [movie['media_id'] for movie in data['movies']] if data['movies'] else []
            song_ids = [song['media_id'] for song in data['songs']] if data['songs'] else []
            book_ids = [book['media_id'] for book in data['books']] if data['books'] else []
            
            transformed_response = {
                "id_user": user_id,
                "movies": movie_ids,
                "songs": song_ids,
                "books": book_ids
            }
            return transformed_response
        else:
            return {}



async def update_recommendation(self, user_id: str, input: UpdateRecommendationInput) -> str:
        # Implement the logic to call the REST API to update the recommendation here.
        ...
        return "Recommendation updated successfully"


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