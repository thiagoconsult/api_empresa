# MICROSERVIÇO EMPRESA

Esta API foi desenvolvida para entrega do MVP da Sprint 3 da PUC-RIO. Ela foi desenvolvida em Flask para servir uma aplicação
desenvolvida em React.

### Esta API trás os seguintes métodos:

| Método            | Funcionalidade                         |
| ----------------- | -------------------------------------- |
| empresa_create    | Inclusão de uma nova empresa           |
| empresa_update    | Atualização de uma empresa existente   |
| empresa_delete    | Exclusão de uma empresa existente      |
| empresa_get_by_id | Consulta uma empresa pelo ID           |
| empresa_get_all   | Consulta lista de empresas cadastradas |
| ----------------- | -------------------------------------- |

# Como executar

Você precisa ter todas as libs utilizadas no projeto e que estão listadas no arquivo requirements.txt.

Para executar este projeto você poderá criar um ambiente virtual primeiramente e ativá-lo.

### Para instalar e ativar a virtual env no Linux:

Na raiz do projeto, exexute:

```
python3 -m venv env
```

Para ativar a env, execute:

```
source env/bin/activate
```

### Instalando o projeto:

Quando a virtual env estiver ativa, irá aparecer antes do caminho do projeto no cmd o nome (env). Agora, é necessário instalar as libs:

```
pip install -r requirements.txt
```

### EXECUTANDO

Execute o comando:

```
python3 run.py
```

```
http://127.0.0.1:5001/
```

Esta página permitirá explorar a documentação do Microserviço
