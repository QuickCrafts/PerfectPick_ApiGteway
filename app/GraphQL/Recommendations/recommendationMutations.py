import strawberry
import httpx
import pika
import json
from strawberry.types import Info
from app.GraphQL.Recommendations.recommendationTypes import MovieRecommendation
from app.GraphQL.Recommendations.recommendationTypes import RecommendationResponse,CreateRecommendationInput,RecommendationResponse



'''
async def fetch_likes(user_id: int) -> dict:
    likes_service_url = f"http://likes-service:8001/likes/{user_id}"
    async with httpx.AsyncClient() as client:
        response = await client.get(likes_service_url)
        if response.status_code == 200:
            return response.json()
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