from classe import *
from views import *

lista_de_cao = []
lista_de_humano = []

def criar_cao():
    nome= input("Nome do cao: ")
    tamanho= input("Tamanho em CM: ")
    raca = input("Raca: ")
    cao = Cachorro(nome,tamanho,raca)
    lista_de_cao.append(cao)
    return cao 

def criar_pessoa():
    nome= input("Nome do humano: ")
    idade= input("idade do humano: ")
    peso= input("Peso: ")
    altura= input(" altura do humano: ")
    pessoa = Humano(nome,idade,peso,altura)
    lista_de_humano.append(pessoa)
    return pessoa

while True:
    print(menu_principal())
    op = int (input("informe uma opção: "))
    if 1 == op:
        criar_cao()
        
    elif 2 == op:
        criar_pessoa()