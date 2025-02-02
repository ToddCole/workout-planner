import requests
import config

def get_nutrition_data(diet):
    url = "https://api.nutritionix.com/v1_1/search"
    params = {
        "query": diet,
        "appId": config.NUTRITIONIX_APP_ID,
        "appKey": config.NUTRITIONIX_API_KEY
    }
    response = requests.get(url, params=params)
    return response.json()
