# Gerenciador de Transações Financeiras com Flask

Este é um projeto simples de API Flask para gerenciar transações financeiras. A API permite criar, listar, editar, excluir e detalhar transações.

## Requisitos

Certifique-se de ter Python e Flask instalados em seu ambiente de desenvolvimento.

## Instalação

1. Clone o repositório para o seu ambiente local:

    ```bash
    git clone https://github.com/seu_usuario/nome_do_repositorio.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd nome_do_repositorio
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

Execute o arquivo `app.py` para iniciar o servidor Flask:

```bash
python app.py

Isso iniciará a API na porta padrão 5000 e estará disponível em http://localhost:5000/.

Rotas
GET /transacao: Lista todas as transações.
POST /transacao: Cria uma nova transação. O corpo da requisição deve ser um JSON contendo os campos descricao, valor, data e tipo_da_transacao.
PUT /transacao/int:id: Edita uma transação existente com o ID fornecido. O corpo da requisição deve ser um JSON contendo os campos a serem atualizados.
DELETE /transacao/int:id: Exclui a transação com o ID fornecido.
GET /transacao/int:id: Detalha uma transação específica com o ID fornecido.
Validação de Dados
Os seguintes critérios de validação são aplicados aos campos das transações:

O campo "valor" é obrigatório e deve ser um número.
O campo "descricao" é obrigatório e deve ser uma string.
O campo "tipo_da_transacao" é obrigatório e deve ser exatamente "entrada" ou "saida".

Exemplo de Transação
{
    "id": 1,
    "descricao": "conta de mercado",
    "valor": 60000,
    "data": "2024-02-29",
    "tipo_da_transacao": "saida"
}
