import requests
import datetime as dt
import os
today = dt.datetime.now()

#Nutri api connection and authentication
nutritionI = os.environ['nutritionID']
nutriAp = os.environ['nutriApi']
nutri_endpoint = os.environ['nutri_endpoint']

headers = \
    {
        "x-app-id": nutritionI,
        "x-app-key": nutriAp
    }

nutri_Para = \
    {
        "query": input("What exercises did you do today? ")
    }

response = requests.post(url=nutri_endpoint, json=nutri_Para, headers=headers).json()
result = response["exercises"]

#Adding a row in google sheet

sheetyApi = os.environ["sheetyApi"]
sheet_Auth =os.environ["sheet_Auth"]
dayW= today.strftime('%d/%m/%Y')
time = today.strftime('%X')


for exercise in result:
    sheety_Para =\
        {
            "workout":
                {
                    "date": dayW,
                    "time": time,
                    "exercise": exercise["name"].title(),
                    "duration": exercise['duration_min'],
                    "calories": exercise["nf_calories"]


                }

        }

Auth_Header =\
    {
        "Authorization": sheet_Auth ,

    }

sheetResponse = requests.post(url=sheetyApi, json=sheety_Para, headers=Auth_Header)

print("Workout information successfully added to the spreadsheet")


