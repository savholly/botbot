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

def get_temp(q):
    url = "https://api.openweathermap.org/data/2.5/weather?"
    key = os.getenv('WEATHER_API_KEY')
    city = q
    url = url + "appid=" + key + "&q=" + city
    response = requests.get(url)
    response = response.json()
    temp_kelvin = response["main"]["temp"]
    temp_celc = temp_kelvin - 273
    temp_far = (1.8 * temp_celc) + 32
    return(round(temp_far))

def get_condition(q):
    url = "https://api.openweathermap.org/data/2.5/weather?"
    key = os.getenv('WEATHER_API_KEY')
    city = q
    url = url + "appid=" + key + "&q=" + city
    response = requests.get(url)
    response = response.json()
    condition = response["weather"][0]["main"]
    return(condition)