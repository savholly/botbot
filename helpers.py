#helpers.py
#will contain all helpers for the APIs
import requests
import json
import os
from dotenv import load_dotenv

def get_cat():
    url = "https://api.thecatapi.com/v1/images/search"
    header={'x-api-key' : os.getenv('CAT_API_KEY')}
    response = requests.get(url, header).json()[0]["url"]
    return (response)

def get_dog():
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url).json()["message"]
    return (response)

def get_avery():
    url = "https://api.breakingbadquotes.xyz/v1/quotes"
    response = requests.get(url).json()[0]["quote"]
    return(response)

def get_temp(q):
    url = "https://api.openweathermap.org/data/2.5/weather?"
    key = os.getenv('WEATHER_API_KEY')
    city = q
    url = url + "appid=" + key + "&q=" + city
    response = requests.get(url).json()
    temp_kelvin = response["main"]["temp"]
    temp_celc = temp_kelvin - 273
    temp_far = (1.8 * temp_celc) + 32
    return(round(temp_far))

def get_condition(q):
    url = "https://api.openweathermap.org/data/2.5/weather?"
    key = os.getenv('WEATHER_API_KEY')
    city = q
    url = url + "appid=" + key + "&q=" + city
    response = requests.get(url).json()
    condition = response["weather"][0]["main"]
    return(condition)

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single"
    response = requests.get(url).json()["joke"]
    return(response)

def get_meme():
    url = "https://some-random-api.ml/meme"
    response = requests.get(url).json()["image"]
    return(response)

