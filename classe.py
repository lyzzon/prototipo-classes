


class Animal:
    nome:str
    coracao:bool
    racional:bool
    def __init__(self,nome,coracao):
        self.nome=nome     
        self.coracao=coracao

class Humano(Animal):
    cor=str
    racional=True
    cultura=True
    
    def __init__(self,racionalidade,nome,cultura,cor):
        super().__init__(nome,True,True)
        self.racionalidade = racionalidade
        self.nome = nome 
        self.cultura = cultura
        self.cor = cor
        
class Cachorro(Animal):
    tamanho=0
    raca=''
    
    def __init__(self,tamanho,raca,nome):
        super().__init__(nome,True,True)
        self.tamanho = tamanho
        self.raca = raca
        self.nome = nome
        self.coracao=True
        self.racional=False
        
        
    def latir(self):
        print('au-au')
                