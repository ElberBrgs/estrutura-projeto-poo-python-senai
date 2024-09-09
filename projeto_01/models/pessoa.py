from models.enums.sexo import Sexo


class Pessoa:
    def __init__(self,nome:str,idade:int,sexo:Sexo) -> None:
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def __str__(self) -> str:
        return(
            f"\nNome: {self.nome}"
            f"\nIdade: {self.idade}"
            f"\nSexo: {self.sexo.value}"
        )