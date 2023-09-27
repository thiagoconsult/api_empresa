from flask_openapi3 import APIBlueprint, Tag
from flask import redirect
from flask_cors import CORS
from api.empresa_schema import (
    EmpresaSchema,
    EmpresaByIdSchema
)
from api.empresa_services import (
    service_empresa_create,
    service_empresa_update,
    service_empresa_delete,
    service_empresa_get_by_id,
    service_empresa_get_all
)


tag_empresa = Tag(
    name='Empresa', description='Inclusão, Alteração, Consulta e Exclusão de Empresa')

api = APIBlueprint(
    'Empresa',
    __name__,
    abp_tags=[tag_empresa]
)


# CORS(api, allow_headers='*', origins='*')

#######################################################################
# Redirecionamento para a documentação Swagger
#######################################################################


@api.route('/')
def index():
    return redirect('/openapi/swagger')


#######################################################################
# POST - Inclusão de Empresa
#######################################################################


@api.post(
    '/empresa',
    summary='Inclusão de Empresa',
    description='Método para inclusão de empresas pelo front-end'
)
def empresa_create(body: EmpresaSchema):
    return service_empresa_create(body)


#######################################################################
# PUT - Alteração de Empresa
#######################################################################


@api.put(
    '/empresa',
    summary='Alteração de Empresa',
    description='Método para alteração de empresas pelo front-end'
)
def empresa_update(query: EmpresaByIdSchema, body: EmpresaSchema):
    return service_empresa_update(query, body)


#######################################################################
# DELETE - Exclusão de Empresa
#######################################################################


@api.delete(
    '/empresa',
    summary='Exclusão de Empresa',
    description='Método para exclusão de empresas pelo front-end'
)
def empresa_delete(query: EmpresaByIdSchema):
    return service_empresa_delete(query)


#######################################################################
# GET - Consulta Empresa por ID
#######################################################################


@api.get(
    '/empresa/id',
    summary='Consulta Empresa por ID',
    description='Método para consulta de empresa por id pelo front-end'
)
def empresa_get_by_id(query: EmpresaByIdSchema):
    return service_empresa_get_by_id(query)


#######################################################################
# GET - Consulta Lista de Empresas
#######################################################################


@api.get(
    '/empresa/all',
    summary='Consulta Lista de Empresa',
    description='Método para consulta de lista de empresas pelo front-end'
)
def empresa_get_all():
    return service_empresa_get_all()
