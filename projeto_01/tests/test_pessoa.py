import pytest

from projeto_01.models.endereco import Endereco
from projeto_01.models.enums.sexo import Sexo
from projeto_01.models.pessoa import Pessoa


#Modelo.
@pytest.fixture
def criar_pessoa():
    pessoa_um = Pessoa("Joaozinho",30,Sexo.MASCULINO,
                   Endereco("Via Rua Alameda","234"))
    return pessoa_um

def test_pessoa_atributo_nome(criar_pessoa):
    assert criar_pessoa.nome == "Joaozinho"

def test_pessoa_atributo_idade(criar_pessoa):
    assert criar_pessoa.idade == 30
