from flask import Flask, request, jsonify
from services.ai_service import generate_plan
from services.nutrition_api import get_nutrition_data
from services.workout_api import get_workout_data

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the AI Workout & Nutrition Planner!"


@app.route('/generate-plan', methods=['POST'])
def generate():
    data = request.json
    goal = data.get('goal')
    dietary_preference = data.get('diet')

    # AI-generated plan
    ai_response = generate_plan(goal, dietary_preference)

    # Fetch nutrition and workout data
    nutrition_data = get_nutrition_data(dietary_preference)
    workout_data = get_workout_data(goal)

    return jsonify({
        "ai_plan": ai_response,
        "nutrition_data": nutrition_data,
        "workout_data": workout_data
    })


if __name__ == '__main__':
    app.run(debug=True)
