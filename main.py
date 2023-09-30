from fastapi import FastAPI
import pyjokes
from pydantic import BaseModel


app = FastAPI()
@app.get("/")
def joke():
    return pyjokes.get_joke()

@app.get("/{friend}")
def friend_joke(friend: str):
    return friend + " tells his joke: " + pyjokes.get_joke()

@app.get("/multi/{friend}")
def multy_friends_joke(friend: str, jokes_number: int):
    result = ""
    for i in range(jokes_number):
        result += friend + f" tells his joke #{i + 1}: " + pyjokes.get_joke() + " "
    return result

class Joke(BaseModel):
    friend: str
    joke: str

class JokeInput(BaseModel):
    friend: str

# @app.post("/")
# def create_joke(joke_input: JokeInput):
#     return joke_input.friend + " tells his joke: " + pyjokes.get_joke()

@app.post("/")
def create_joke(joke_input: JokeInput):
    return Joke(friend=joke_input.friend, joke=pyjokes.get_joke())

@app.post("/", response_mofel=Joke)
def create_joke(joke_input: JokeInput):
    """kkkkkk"""
    return Joke(friend=joke_input.friend, joke=pyjokes.get_joke())
