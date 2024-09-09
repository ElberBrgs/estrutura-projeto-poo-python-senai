from os import system

#Importando classes.
from models.pessoa import Pessoa
from models.enums.sexo import Sexo
from models.endereco import Endereco

system("cls || clear")

#Instanciando classe.
pessoa_um = Pessoa("Joaozinho",30,Sexo.MASCULINO,
                   Endereco("Via Rua Alameda","234"))
print(pessoa_um)
