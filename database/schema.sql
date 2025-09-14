-- Cria o banco de dados se ele não existir
CREATE DATABASE IF NOT EXISTS mural_db;

-- Usa o banco de dados
USE mural_db;

-- Cria a tabela para as mensagens
CREATE TABLE IF NOT EXISTS messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);