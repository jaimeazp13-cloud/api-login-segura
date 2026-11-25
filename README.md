# 🔑 API de Login Segura

API em Python (FastAPI) de cadastro e login de usuários, construída aos poucos aplicando boas práticas de **segurança da informação**.

> 🚧 Projeto em desenvolvimento — construído em etapas.

## Etapas

- [x] **1. Estrutura inicial** e rota de status (`GET /`)
- [ ] **2. Cadastro** de usuários com senha protegida por hash (bcrypt) e banco SQLite
- [ ] **3. Login** com token JWT
- [ ] **4. Rotas protegidas** e limite de tentativas de login (contra força bruta)
- [ ] **5. Testes automatizados** e documentação final

## Como rodar

Precisa do [Python 3.12+](https://www.python.org/downloads/).

```bash
git clone https://github.com/jaimeazp13-cloud/api-login-segura.git
cd api-login-segura
python -m venv .venv
.venv\Scripts\activate        # Windows (no Linux/Mac: source .venv/bin/activate)
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Depois abra:
- http://127.0.0.1:8000 — status da API
- http://127.0.0.1:8000/docs — documentação interativa gerada automaticamente

## Tecnologias

Python · FastAPI · Uvicorn

## Autor

Feito por **Jaime Augusto Perez**, estudante de Sistemas de Informação.
[LinkedIn](https://www.linkedin.com/in/jaime-augusto-perez)
