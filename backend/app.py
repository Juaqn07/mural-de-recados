# Importação das bibliotecas necessárias
from flask import Flask, request, jsonify, render_template
import mysql.connector
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Inicialização do Flask
# Aponta para a pasta 'frontend' para encontrar os templates (HTML) e arquivos estáticos (CSS, JS)
app = Flask(__name__, template_folder='../frontend', static_folder='../frontend')

# Dicionário com as configurações de conexão ao banco de dados
# A senha é carregada de forma segura a partir das variáveis de ambiente
db_config = {
    'user': 'root',
    'password': os.getenv('DB_PASSWORD'),
    'host': '127.0.0.1',
    'database': 'mural_db'
}

# Função auxiliar para obter uma conexão com o o banco de dados
def get_db_connection():
    """Cria e retorna uma nova conexão com o banco de dados MySQL."""
    conn = mysql.connector.connect(**db_config)
    return conn

# --- DEFINIÇÃO DAS ROTAS DA API ---

# Rota para buscar todas as mensagens (Endpoint GET)
@app.route('/api/messages', methods=['GET'])
def get_messages():
    """Busca todas as mensagens no banco de dados e as retorna em formato JSON."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT id, content, created_at FROM messages ORDER BY created_at DESC"
    cursor.execute(query)
    messages = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(messages)

# Rota para adicionar uma nova mensagem (Endpoint POST)
@app.route('/api/messages', methods=['POST'])
def add_message():
    """Recebe o conteúdo de uma nova mensagem via JSON e a insere no banco de dados."""
    data = request.get_json()
    new_message_content = data['content']
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO messages (content) VALUES (%s)"
    cursor.execute(query, (new_message_content,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'status': 'success', 'message': 'Mensagem adicionada!'}), 201

# Rota para ATUALIZAR uma mensagem existente (Endpoint PUT)
@app.route('/api/messages/<int:message_id>', methods=['PUT'])
def update_message(message_id):
    """Atualiza o conteúdo de uma mensagem específica."""
    data = request.get_json()
    updated_content = data['content']
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "UPDATE messages SET content = %s WHERE id = %s"
    cursor.execute(query, (updated_content, message_id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'status': 'success', 'message': 'Mensagem atualizada!'})

# Rota para EXCLUIR uma mensagem (Endpoint DELETE)
@app.route('/api/messages/<int:message_id>', methods=['DELETE'])
def delete_message(message_id):
    """Exclui uma mensagem específica do banco de dados."""
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "DELETE FROM messages WHERE id = %s"
    cursor.execute(query, (message_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'status': 'success', 'message': 'Mensagem excluída!'})


# Rota principal para servir a página inicial (o frontend)
@app.route('/')
def serve_index():
    """Renderiza e serve o arquivo principal index.html."""
    return render_template('index.html')

# Bloco de execução principal
if __name__ == '__main__':
    app.run(debug=True)
    