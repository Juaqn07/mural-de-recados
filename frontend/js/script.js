document.addEventListener('DOMContentLoaded', () => {
    // Seleciona os elementos principais da página
    const form = document.getElementById('message-form');
    const input = document.getElementById('message-input');
    const button = form.querySelector('button');
    const container = document.getElementById('messages-container');

    // Função assíncrona para buscar as mensagens da API
    const fetchMessages = async () => {
        const response = await fetch('/api/messages');
        const messages = await response.json();
        
        container.innerHTML = ''; // Limpa o contêiner
        
        // Adiciona cada mensagem ao container, agora com botões de ação
        messages.forEach(msg => {
            const msgDiv = document.createElement('div');
            msgDiv.className = 'message';
            
            const msgContent = document.createElement('span');
            msgContent.textContent = msg.content;
            
            const actionsDiv = document.createElement('div');
            actionsDiv.className = 'actions';

            const editButton = document.createElement('button');
            editButton.className = 'edit-btn';
            editButton.textContent = 'Editar';
            editButton.onclick = () => editMessage(msg.id, msg.content);

            const deleteButton = document.createElement('button');
            deleteButton.className = 'delete-btn';
            deleteButton.textContent = 'Excluir';
            deleteButton.onclick = () => deleteMessage(msg.id);

            actionsDiv.appendChild(editButton);
            actionsDiv.appendChild(deleteButton);

            msgDiv.appendChild(msgContent);
            msgDiv.appendChild(actionsDiv);
            container.appendChild(msgDiv);
        });
    };

    // Função para EDITAR uma mensagem
    const editMessage = async (id, currentContent) => {
        const newContent = prompt('Edite seu recado:', currentContent);
        if (newContent && newContent !== currentContent) {
            await fetch(`/api/messages/${id}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ content: newContent })
            });
            fetchMessages(); // Atualiza a lista
        }
    };

    // Função para EXCLUIR uma mensagem
    const deleteMessage = async (id) => {
        if (confirm('Tem certeza que deseja excluir este recado?')) {
            await fetch(`/api/messages/${id}`, {
                method: 'DELETE'
            });
            fetchMessages(); // Atualiza a lista
        }
    };

    // Adiciona o listener de evento para o envio do formulário
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        button.disabled = true;
        button.textContent = 'Enviando...';
        
        await fetch('/api/messages', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ content: input.value })
        });
        
        input.value = '';
        button.disabled = false;
        button.textContent = 'Enviar';
        fetchMessages();
    });

    fetchMessages(); // Carrega as mensagens iniciais
});