"""
main.py
-------
Ponto de entrada da API.

O que é uma API? É um programa que fica "escutando" pedidos pela rede
(requisições HTTP) e devolve respostas, normalmente em JSON. Quem faz os
pedidos pode ser um site, um app de celular ou outro sistema.

Nesta Etapa 1 a API só tem uma rota, que serve para saber se ela está no ar.
Nas próximas etapas vamos adicionar cadastro, login e rotas protegidas.

Para rodar (na pasta do projeto, com o ambiente virtual ativado):
    uvicorn app.main:app --reload
Depois abra no navegador:
    http://127.0.0.1:8000        -> resposta da rota "/"
    http://127.0.0.1:8000/docs   -> documentação automática (Swagger)
"""

from fastapi import FastAPI

# Cria a aplicação. O título e a descrição aparecem na página /docs.
app = FastAPI(
    title="API de Login Segura",
    description="API de cadastro e login com boas práticas de segurança.",
    version="0.1.0",
)


# @app.get("/") diz ao FastAPI: quando chegar uma requisição GET no
# caminho "/", execute esta função e devolva o que ela retornar.
# O dicionário Python é convertido automaticamente para JSON.
@app.get("/")
def status():
    """Verifica se a API está funcionando."""
    return {"status": "online", "versao": app.version}
