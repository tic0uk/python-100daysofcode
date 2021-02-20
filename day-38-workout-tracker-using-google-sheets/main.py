import requests
import datetime as dt
import os

# Exercise Tracking with Python and Google Sheets

NUTRITIONIX_APP_ID = os.environ.get("NT_APP_ID")
NUTRITIONIX_API_KEY = os.environ.get("NT_API_KEY")
GENDER = "male"
WEIGHT_KG = "100"
HEIGHT_CM = "168"
AGE = 38

NUTRITIONIX_Endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

enter_exercise = input("Tell me what exercises you did: ")

exercise_parameters = {
    "query": enter_exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(NUTRITIONIX_Endpoint, json=exercise_parameters, headers=headers)

data = response.json()["exercises"]
SHEETY_Endpoint = "https://api.sheety.co/625d2f429ba4ee7746c809f8b47b4ea4/myWorkouts/workouts"

today_date = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%X")

sheety_headers = {
    "Authorization": os.environ.get("SHEETY_BEARER"),
}
for item in data:
    sheety_data = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": item["name"].title(),
            "duration": item["duration_min"],
            "calories": item["nf_calories"],
        }
    }
    response_sheet = requests.post(SHEETY_Endpoint, json=sheety_data, headers=sheety_headers)
    print(response_sheet.text)
