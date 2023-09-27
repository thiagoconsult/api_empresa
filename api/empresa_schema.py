from pydantic import BaseModel
from typing import List, Optional
from api.empresa_model import Empresa


class EmpresaSchema(BaseModel):
    nome: str = 'Google'
    cnpj: str = '89415819000123'
    cep: str = '01001000'
    cidade: str = 'São Paulo'
    bairro: str = 'Sé'
    rua: str = 'Praça da Sé'
    numero: int = 1
    uf: str = 'SP'


class EmpresaByIdSchema(BaseModel):
    id: int


def serialize_empresa(empresa: Empresa):

    return {
        'id': empresa.id,
        'nome': empresa.nome,
        'cnpj': empresa.cnpj,
        'cep': empresa.cep,
        'cidade': empresa.cidade,
        'bairro': empresa.bairro,
        'rua': empresa.rua,
        'numero': empresa.numero,
        'uf': empresa.uf
    }


def serialize_empresa_list(empresas: List[Empresa]):

    lista = []

    for empresa in empresas:
        lista.append(serialize_empresa(empresa))

    # return {'Empresas': lista}
    return lista
