import os
import base64
import requests
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
TOKEN_URL = os.getenv("TOKEN_URL")
SEARCH_URL = os.getenv("SEARCH_URL")

# Func to get OAuth2 token
def get_access_token():
    credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()

    payload = {"grant_type": "client_credentials", "scope": "basic"}
    headers = {
        "Authorization": f"Basic {encoded_credentials}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(TOKEN_URL, data=payload, headers=headers)

    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        print("Error Response:", response.json()) 
        raise Exception("Failed to get access token")

# API endpoint to search for food
@app.get("/search_food/")
def search_food(query: str):
    try:
        access_token = get_access_token()
    except Exception as e:
        return {"error": str(e)}

    params = {"method": "foods.search", "format": "json", "search_expression": query}
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(SEARCH_URL, params=params, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data", "details": response.text}
