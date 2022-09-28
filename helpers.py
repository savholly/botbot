#helpers.py
#will contain all helpers for the APIs
import requests
import json
import os
from dotenv import load_dotenv

def get_cat():
    url = "https://api.thecatapi.com/v1/images/search"
    header={'x-api-key' : os.getenv('CAT_API_KEY')}
    response = requests.get(url, header)
    response = response.json()
    response = response[0]["url"]
    return (response)

def get_dog():
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    response = response.json()
    response = response["message"]
    return (response)

def get_avery():
    url = "https://api.breakingbadquotes.xyz/v1/quotes"
    response = requests.get(url)
    response = response.json()
    response = response[0]["quote"]
    return(response)

