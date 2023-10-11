from pydantic import BaseModel


class N(BaseModel):
    num: int


class FIO(BaseModel):
    name: str
    surname: str


class Fio(BaseModel):
    F: str
    S: str
