import requests
import config

def get_workout_data(goal):
    url = f"https://wger.de/api/v2/exercise/?language=2&category={goal}"
    response = requests.get(url)
    return response.json()

