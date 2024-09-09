class Endereco:
    def __init__(self,logradouro:str,numero:str) -> None:
        self.logradouro = logradouro
        self.numero = numero

    def __str__(self) -> str:
        return (
            f"\nLogradouro: {self.logradouro}"
            f"\nNúmero: {self.numero}"
            )