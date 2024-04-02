import httpx
from app.GraphQL.Recommendations.recommendationTypes import MovieRecommendation

async def fetch_recommendations(user_id: str) -> MovieRecommendation:
    api_url = f"http://recommendationms:8000/recommendation/{user_id}"
    async with httpx.AsyncClient() as client:
        response = await client.get(api_url)
        if response.status_code != 200:
            raise ValueError("Failed to fetch recommendations")
        data = response.json()
        recommendation = data[0] if data else None
        return MovieRecommendation(**recommendation) if recommendation else None

