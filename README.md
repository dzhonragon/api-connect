# API Connect - Gerenciamento de Usuários

API REST desenvolvida em Python com Flask como parte da Experiência Prática II da disciplina de Desenvolvimento Back-end. O projeto implementa operações CRUD para o gerenciamento de usuários e utiliza comunicação HTTP com dados no formato JSON.

## Objetivo

A API permite cadastrar, listar, buscar, atualizar e remover usuários. O projeto foi desenvolvido seguindo conceitos de arquitetura REST, utilizando métodos HTTP adequados, códigos de status e respostas padronizadas em JSON.

## Tecnologias utilizadas

* Python 3
* Flask
* Git
* GitHub

## Estrutura do projeto

```text
desenvolvimentobackend/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── controllers/
│   ├── __init__.py
│   └── users_controller.py
│
├── routes/
│   ├── __init__.py
│   └── users.py
│
├── data/
│   ├── __init__.py
│   └── users.py
│
└── venv/
```

## Instalação

Clone o repositório:

```bash
git clone git@github.com:dzhonragon/api-connect.git
```

Acesse a pasta do projeto:

```bash
cd api-connect
```

Crie um ambiente virtual:

```bash
python -m venv venv
```

No Windows, ative o ambiente virtual:

```bash
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Execução

Para iniciar o servidor:

```bash
python app.py
```

A API será executada localmente em:

```text
http://127.0.0.1:5000
```

## Endpoints

| Método | Endpoint         | Descrição                     | Status esperado                          |
| ------ | ---------------- | ----------------------------- | ---------------------------------------- |
| GET    | `/usuarios`      | Lista todos os usuários       | 200 OK                                   |
| GET    | `/usuarios/<id>` | Busca um usuário pelo ID      | 200 OK ou 404 Not Found                  |
| POST   | `/usuarios`      | Cadastra um novo usuário      | 201 Created ou 400 Bad Request           |
| PUT    | `/usuarios/<id>` | Atualiza um usuário existente | 200 OK, 400 Bad Request ou 404 Not Found |
| DELETE | `/usuarios/<id>` | Remove um usuário             | 204 No Content ou 404 Not Found          |

## Exemplo de cadastro

Requisição:

```http
POST /usuarios
Content-Type: application/json
```

Corpo JSON:

```json
{
    "nome": "João Silva",
    "email": "joao@email.com"
}
```

Exemplo de resposta:

```json
{
    "data": {
        "id": 1,
        "nome": "João Silva",
        "email": "joao@email.com"
    }
}
```

Status HTTP:

```text
201 Created
```

## Exemplo de erro de validação

Caso o campo `nome` ou `email` não seja informado corretamente, a API retorna:

```json
{
    "error": "Os campos nome e email são obrigatórios."
}
```

Status HTTP:

```text
400 Bad Request
```

## Exemplo de usuário não encontrado

Ao buscar, atualizar ou remover um ID inexistente, a API retorna uma resposta de erro em JSON:

```json
{
    "error": "Usuário não encontrado."
}
```

Status HTTP:

```text
404 Not Found
```

## Conceitos aplicados

O projeto utiliza os princípios básicos de uma API REST, separando as responsabilidades entre rotas, controladores e dados. As requisições são recebidas pelo servidor Flask, encaminhadas para a lógica correspondente e respondidas em formato JSON.

As operações CRUD implementadas representam Create, Read, Update e Delete. Para isso, foram utilizados os métodos HTTP POST, GET, PUT e DELETE, juntamente com códigos de status adequados para indicar o resultado de cada operação.

Os dados são armazenados temporariamente em memória, permitindo a simulação de persistência durante a execução do servidor. As informações são perdidas quando a aplicação é encerrada e reiniciada.
