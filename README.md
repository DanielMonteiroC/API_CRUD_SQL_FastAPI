# FastAPI React CRUD

Este projeto é uma aplicação full stack que utiliza **FastAPI** no backend com banco de dados **MySQL** e **React** no frontend. O sistema realiza operações de CRUD (Create, Read, Update, Delete) de forma integrada.

---

## 📁 Estrutura do Projeto
```
fastapi_react_crud/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── crud.py
│   │   ├── database.py
│   │   └── routes.py
│   └── requirements.txt
└── frontend/
    ├── src/
    │   ├── components/
    │   │   ├── ItemForm.js
    │   │   └── ItemList.js
    │   ├── App.js
    │   └── api.js
    └── package.json
```

---

## 🚀 Como executar o projeto

### Backend (FastAPI + MySQL)

#### Pré-requisitos:
- Python 3.10+
- MySQL Server
- Virtualenv (opcional, mas recomendado)

#### Passos:
```bash
# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Configure a string de conexão no arquivo `database.py`
# Exemplo:
# DATABASE_URL = "mysql+pymysql://usuario:senha@localhost/sistema"

# Rode o servidor FastAPI
uvicorn app.main:app --reload
```

Acesse a documentação da API em: [http://localhost:8000/docs](http://localhost:8000/docs)

### Frontend (React)

#### Pré-requisitos:
- Node.js + npm ou yarn

#### Passos:
```bash
# Instale as dependências
npm install

# Inicie o servidor React
npm start
```

O frontend estará disponível em: [http://localhost:3000](http://localhost:3000)

---

## 🔧 Funcionalidades
- Criar item
- Listar todos os itens
- Obter item por ID
- Atualizar item
- Deletar item

---

## 🌐 CORS
O backend já vem configurado com suporte a CORS permitindo qualquer origem:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 🧑‍💻 Tecnologias utilizadas
- **FastAPI**
- **SQLAlchemy**
- **MySQL**
- **React**
- **Axios**
- **Uvicorn**

---

## 📦 Requisitos do Projeto

### Backend:
Ver `backend/requirements.txt`

### Frontend:
Ver `frontend/package.json`

---

## 📄 Licença
Este projeto está sob a licença MIT.
