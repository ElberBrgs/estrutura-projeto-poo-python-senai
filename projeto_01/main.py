from os import system

#Importando classe da pasta model.
from models.pessoa import Pessoa

system("cls || clear")

#Instanciando classe.
pessoa_um = Pessoa("Joaozinho",30)
print(pessoa_um)
