from os import system

#Importando classes.
from models.pessoa import Pessoa
from models.enums.sexo import Sexo

system("cls || clear")

#Instanciando classe.
pessoa_um = Pessoa("Joaozinho",30,Sexo.MASCULINO)
print(pessoa_um)
