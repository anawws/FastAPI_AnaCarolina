from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
def index():
   return { "data" : "Bem vindo!!!" }


#Parte 1 - Quadrados


@app.get("/quadrados")
def listaQuadrados(max : Optional[int] = 10):
   quadrados = []
   for i in range(1, max+1):
       quadrados.append(i**2)
  
   return {
       "max" : max,
       "quadrados" : quadrados
   }


#Tabuada


@app.get("/tabuada/{numero}")
def listaTabuada(numero : int, start : Optional[int] = 1 , end : Optional[int] = 10):
   tabuada = []
   for i in range(start, end+1):
       tabuada.append(numero*i)
  
   return {
       "número" : numero,
       "tabuada" : tabuada
    }


#Bhaskara


class num(BaseModel):
   a : float
   b : float
   c : float

@app.post("/bhaskara")
def Bhaskara(c : num):
    d = c.b**2 -4*c.a*c.c
    x1 = ((-c.b) + d ** 0.5) / (2*c.a)
    x2 = ((-c.b) - d ** 0.5) / (2*c.a)
    return {
       "eq" : str(c.a) + "x²" + str(c.b) + "x" + str(c.c),
       "x1" : x1,
       "x2" : x2
    }


#Conta

class letra(BaseModel):
   frase : str

@app.post("/conta")
def ContaLetra(conta : letra):
    v = 0
    c = 0
    o = 0
    for i in range(0, len(conta.frase)):
        caractere = conta.frase[i]
        if caractere.lower() in 'aeiou':
            v = v+1
        elif caractere.lower() in ' ':
            c = c+1
        else:
            o = o+1
            
    return {
        "frase" : conta.frase,
        "vogais": v,
        "espacos": c,
        "outros": o
    }