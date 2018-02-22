-- DATABASE: temlogica_db

CREATE TABLE usuario(
    usuario_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nome_usuario VARCHAR(100),
    senha_usuario VARCHAR(100),
    email_usuario VARCHAR(100),
    tipo_usuario INT UNSIGNED,
    foto_usuario VARCHAR(30),
    data_cadastro_usuario TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao_usuario TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);