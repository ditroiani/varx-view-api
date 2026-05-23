# VarX View API
## Smart Retail Analytics
 
> API de analise anonima de audiencia para ambientes comerciais.
> Transforma cameras em sensores de inteligencia de publico — sem armazenar imagens.
 
![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.136-green)
 
## Sobre o Projeto
 
O VarX View processa frames de camera localmente, descarta as imagens imediatamente
e persiste apenas metadados anonimizados. Gera KPIs de audiencia para:
 
- Academias, barbearias e varejo em geral
- Plataformas de Digital Signage (DOOH)
- Gestao de Retail Media
 
**100% LGPD-compliant — zero dados pessoais armazenados.**
 
## Stack
 
- **API:** Python 3.13 + FastAPI
- **Banco de dados:** PostgreSQL + SQLAlchemy + Alembic
- **Infraestrutura:** Docker + Docker Compose
 
## Como rodar localmente
```bash
# Clone o repositorio
git clone https://github.com/SEU_USUARIO/varx-view-api.git
cd varx-view-api
 
# Crie e ative o ambiente virtual
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows
 
# Instale as dependencias
pip install -r requirements.txt
 
# Configure as variaveis de ambiente
cp .env.example .env
# Edite o .env com suas configuracoes
 
# Rode a API
uvicorn src.main:app --reload
```
 
Acesse: http://localhost:8000/docs
 
## Endpoints
| Metodo | Endpoint | Descricao |
|--------|----------|-----------|
...
 
## Autor
Diego Troiani
