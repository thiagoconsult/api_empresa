from typing import Any
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from api.db import engine


class Base(DeclarativeBase):
    pass


class Empresa(Base):
    __tablename__ = 'empresa'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(50))
    cnpj: Mapped[str] = mapped_column(String(14), unique=True)
    cep: Mapped[str] = mapped_column(String(8))
    cidade: Mapped[str] = mapped_column(String(50))
    bairro: Mapped[str] = mapped_column(String(50))
    rua: Mapped[str] = mapped_column(String(50))
    numero: Mapped[int] = mapped_column(Integer)
    uf: Mapped[str] = mapped_column(String(2))

    def __init__(self, nome: str, cnpj: str, cep: str, cidade: str, bairro: str, rua: str, numero: int, uf: str):
        self.nome = nome
        self.cnpj = cnpj
        self.cep = cep
        self.cidade = cidade
        self.bairro = bairro
        self.rua = rua
        self.numero = numero
        self.uf = uf


Base.metadata.create_all(engine)
