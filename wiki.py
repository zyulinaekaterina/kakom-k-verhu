from fastapi import FastAPI
from Class import N, FIO, Fio
add = FastAPI()


@add.get("/summ/{number}")
def summ(number: int):
    return N(num=number)

# path


@add.get("/summa/")
def summa(name: str, surname: str):
    return Fio(F=name, S=surname)

# query


@add.post("/class", response_model=Fio)
def clas(fio: FIO):
    return Fio(F=fio.name, S=fio.surname)
# post










# @add.get("/{search}")
# def src(search : str):
#     return wikipedia.summary(search, sentences=7)
# @add.get("/next/{search}")
# def low_sentence_summary(search:str,number:int):
#     return wikipedia.summary(search, sentences=number)
#
# class wikiinput(BaseModel):
#     sear : str
#     snt : int
#
# @add.post("/class")
# def rep(src: wikiinput):
#     return(wikipedia.search(src.sear, results=src.snt))
