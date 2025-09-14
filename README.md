# Mural de Recados Full-Stack

![Screenshot do Mural de Recados](./screenshot.png)

## 📝 Descrição

Este é um projeto de "Hello World" para um ambiente de desenvolvimento full-stack recém-configurado no Linux Mint. A aplicação consiste em um mural de recados simples que permite criar, ler, atualizar e deletar mensagens (CRUD), demonstrando a integração completa entre frontend, backend e um banco de dados relacional.

O objetivo principal é validar a instalação e a comunicação entre todas as ferramentas essenciais de um desenvolvedor.

---

## 🛠️ Tecnologias Utilizadas

-   **Backend:**
    -   Python 3
    -   Flask (para a API REST)
    -   MySQL Connector
    -   Python-dotenv (para gerenciar variáveis de ambiente)
-   **Frontend:**
    -   HTML5
    -   CSS3
    -   JavaScript (Vanilla, com Fetch API)
-   **Banco de Dados:**
    -   MySQL
-   **Ambiente:**
    -   Linux Mint
    -   Git & GitHub
    -   Visual Studio Code

---

## 📂 Estrutura do Projeto

mural-de-recados/
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── screenshot.png
├── backend/
│   └── app.py
├── database/
│   └── schema.sql
└── frontend/
├── css/
│   └── style.css
├── js/
│   └── script.js
└── index.html

---

## 🚀 Como Executar o Projeto

Siga os passos abaixo para rodar a aplicação localmente.

### Pré-requisitos
- Python 3 instalado
- MySQL Server instalado
- Git instalado

### Passos

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU-USUARIO/mural-de-recados.git](https://github.com/SEU-USUARIO/mural-de-recados.git)
    cd mural-de-recados
    ```
    *Não se esqueça de substituir `SEU-USUARIO` pelo seu nome de usuário do GitHub.*

2.  **Crie e configure o banco de dados:**
    - Acesse o MySQL com seu usuário root:
      ```bash
      mysql -u root -p
      ```
    - Execute o script `schema.sql` para criar o banco de dados e a tabela:
      ```sql
      SOURCE database/schema.sql;
      exit;
      ```

3.  **Configure as variáveis de ambiente:**
    - Crie um arquivo chamado `.env` na raiz do projeto.
    - Adicione sua senha do MySQL ao arquivo:
      ```
      DB_PASSWORD="SUA_SENHA_DO_MYSQL_AQUI"
      ```

4.  **Crie e ative o ambiente virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

5.  **Instale as dependências do Python:**
    ```bash
    pip install -r requirements.txt
    ```

6.  **Inicie o servidor backend:**
    ```bash
    python3 backend/app.py
    ```

7.  **Acesse a aplicação:**
    - Abra seu navegador e acesse [http://127.0.0.1:5000](http://127.0.0.1:5000).

---
**Desenvolvido por Juan Ferreira dos Santos.**
