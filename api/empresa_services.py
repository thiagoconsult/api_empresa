from api.empresa_model import Empresa
from api.empresa_schema import (
    serialize_empresa,
    serialize_empresa_list,
    EmpresaSchema,
    EmpresaByIdSchema
)
from sqlalchemy.orm import Session
from api.db import engine


#######################################################################
# POST - Serviço de Inclusão de Empresa
#######################################################################


def service_empresa_create(body: EmpresaSchema):
    try:
        nova_empresa = Empresa(
            nome=body.nome,
            cnpj=body.cnpj,
            cep=body.cep,
            cidade=body.cidade,
            bairro=body.bairro,
            rua=body.rua,
            numero=body.numero,
            uf=body.uf
        )

        with Session(engine) as session:
            session.add(nova_empresa)
            session.commit()
            return serialize_empresa(nova_empresa), 201
    except Exception as e:
        return {'err': f'Não foi possível cadastrar a empresa, detalhe do erro: {e.args}'}


#######################################################################
# PUT - Serviço de Alteração de Empresa
#######################################################################


def service_empresa_update(query: EmpresaByIdSchema, body: EmpresaSchema):

    with Session(engine) as session:
        empresa = session.query(Empresa).filter(
            Empresa.id == query.id).first()

        if not empresa:
            return {'err': 'Empresa não encontrada'}, 404

        try:

            empresa.nome = body.nome
            empresa.cnpj = body.cnpj
            empresa.cep = body.cep
            empresa.cidade = body.cidade
            empresa.bairro = body.bairro
            empresa.rua = body.rua
            empresa.numero = body.numero
            empresa.uf = body.uf

            session.commit()

            return serialize_empresa(empresa), 200

        except Exception as e:
            return {'err': f'Não foi possível atualizar a empresa, detalhe do erro: {e.args}'}, 400


#######################################################################
# DELETE - Serviço de Exclusão de Empresa
#######################################################################

def service_empresa_delete(query: EmpresaByIdSchema):
    with Session(engine) as session:
        empresa = session.query(Empresa).filter(Empresa.id == query.id).first()

        if not empresa:
            return {'err': 'Empresa não encontrada'}, 404

        try:
            session.delete(empresa)
            session.commit()
            return {'Empresa excluída com sucesso': serialize_empresa(empresa)}, 200

        except Exception as e:
            return {'err': f'Não foi possível excluir a empresa, detalhe do erro: {e.args}'}, 400


#######################################################################
# GET - Serviço de Consulta Empresa por ID
#######################################################################


def service_empresa_get_by_id(query: EmpresaByIdSchema):
    with Session(engine) as session:
        empresa = session.query(Empresa).filter(
            Empresa.id == query.id).first()

        if not empresa:
            return {'err': 'Empresa não encontrada'}, 404

        return serialize_empresa(empresa)


#######################################################################
# GET - Serviço de Consulta Lista de Empresas
#######################################################################

def service_empresa_get_all():
    with Session(engine) as session:
        empresas = session.query(Empresa).order_by(Empresa.nome.asc()).all()

        if not empresas:
            return {'err': 'Nenhuma empresa encontrada'}, 404

        return serialize_empresa_list(empresas), 200


#######################################################################
# GET - Serviço para Consulta Quantidade de Empresas
#######################################################################


def service_empresa_get_count():
    with Session(engine) as session:
        empresas = session.query(Empresa).all()

        # if not empresas:
        #     return {'err': 'Nenhuma empresa encontrada'}, 404

        quantidade = 0

        for empresa in empresas:
            quantidade += 1
            print(quantidade)

        return {'quantidade': quantidade}