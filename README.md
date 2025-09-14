# 📌 Mural de Recados Full-Stack

![Screenshot do Mural de Recados](./screenshot.png)

## 📝 Descrição

Este é um projeto de **"Hello World"** para um ambiente de desenvolvimento full-stack recém-configurado no **Linux Mint**.  
A aplicação consiste em um mural de recados simples que permite **criar, ler, atualizar e deletar mensagens (CRUD)**, demonstrando a integração entre **frontend, backend e banco de dados relacional**.

O objetivo principal é validar a instalação e a comunicação entre todas as ferramentas essenciais de um desenvolvedor.

---

## 🛠️ Tecnologias Utilizadas

- **Backend**
  - Python 3
  - Flask (API REST)
  - MySQL Connector
  - Python-dotenv (variáveis de ambiente)

- **Frontend**
  - HTML5
  - CSS3
  - JavaScript (Vanilla, com Fetch API)

- **Banco de Dados**
  - MySQL

- **Ambiente**
  - Linux Mint
  - Git & GitHub
  - Visual Studio Code

---

## 📂 Estrutura do Projeto

```
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
```

---

## 🚀 Como Executar o Projeto

### ✅ Pré-requisitos
- Python 3 instalado  
- MySQL Server instalado  
- Git instalado  

### 🔧 Passos

1. **Clone o repositório**
   ```bash
   git clone https://github.com/SEU-USUARIO/mural-de-recados.git
   cd mural-de-recados
   ```
   > Substitua `SEU-USUARIO` pelo seu nome de usuário do GitHub.

2. **Crie e configure o banco de dados**
   ```bash
   mysql -u root -p
   ```
   No terminal do MySQL:
   ```sql
   SOURCE database/schema.sql;
   exit;
   ```

3. **Configure as variáveis de ambiente**
   Crie o arquivo `.env` na raiz do projeto:
   ```
   DB_PASSWORD="SUA_SENHA_DO_MYSQL_AQUI"
   ```

4. **Crie e ative o ambiente virtual**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

5. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

6. **Inicie o servidor backend**
   ```bash
   python3 backend/app.py
   ```

7. **Acesse a aplicação**
   Abra o navegador em:  
   👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 👨‍💻 Autor

**Desenvolvido por Juan Ferreira dos Santos**
