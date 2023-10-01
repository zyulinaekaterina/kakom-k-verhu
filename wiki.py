from fastapi import FastAPI
import wikipedia


# print(wikipedia.summary("Bill Gates", sentences=2))
# print(wikipedia.suggest("Bill cliton"))
# print(wikipedia.summary("Ubuntu"))
# print(wikipedia.summary("Key (cryptography)"))
# print(wikipedia.page("Python (programming language)").content)

add = FastAPI()
@add.get("/cont")
def cont(inf: str):
    return wikipedia.page(inf).content

@add.get("/summ/{number}")
def summ(summary: str, number_of_sentences: int):
    return wikipedia.summary(summary, sentences=number_of_sentences)