-- DATABASE: temlogica_db
SET @tamanhoTitulo = 100;
SET @tamanhoDescricao = 4000;

CREATE TABLE usuario(
    usuario_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nome_usuario VARCHAR(100),
    senha_usuario VARCHAR(100),
    email_usuario VARCHAR(100),
    tipo_usuario TINYINT UNSIGNED,
    foto_usuario VARCHAR(50),
    data_cadastro_usuario TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao_usuario TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE debate(
    debate_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    titulo_debate VARCHAR(@tamanhoTitulo),
    descricao_debate VARCHAR(@tamanhoDescricao),
    autor_id_debate INT UNSIGNED,
    data_cadastro_debate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE usuario_debate(
    usuario_debate_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT UNSIGNED,
    debate_id INT UNSIGNED,
    data_cadastro_usuario_debate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuario(usuario_id) ON DELETE CASCADE,
    FOREIGN KEY (debate_id) REFERENCES debate(debate_id) ON DELETE CASCADE
);

CREATE TABLE debate_debate(
    debate_id_primeiro INT UNSIGNED,
    debate_id_segundo INT UNSIGNED,
    FOREIGN KEY (debate_id_primeiro) REFERENCES debate(debate_id) ON DELETE CASCADE,
    FOREIGN KEY (debate_id_segundo) REFERENCES debate(debate_id) ON DELETE CASCADE
);

CREATE TABLE resposta(
    resposta_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    texto_resposta VARCHAR(@tamanhoDescricao),
    ordem_resposta SMALLINT UNSIGNED,
    autor_id_resposta INT UNSIGNED,
    debate_id_resposta INT UNSIGNED,
    data_cadastro_resposta TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    cor_resposta TINYINT UNSIGNED,
    status_resposta TINYINT(1) DEFAULT 1,
    FOREIGN KEY (debate_id_resposta) REFERENCES debate(debate_id) ON DELETE CASCADE
);

CREATE TABLE argumento(
    argumento_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    titulo_argumento VARCHAR(@tamanhoTitulo),
    descricao_argumento VARCHAR(@tamanhoDescricao),
    status_argumento TINYINT(1) DEFAULT 1,
    data_cadastro_argumento TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    resposta_id_argumento INT UNSIGNED,
    cor_argumento TINYINT UNSIGNED,
    FOREIGN KEY (resposta_id_argumento) REFERENCES resposta(resposta_id) ON DELETE CASCADE
);

CREATE TABLE premissa(
    premissa_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    titulo_premissa VARCHAR(@tamanhoTitulo),
    descricao_premissa VARCHAR(@tamanhoDescricao),
    status_premissa TINYINT(1) DEFAULT 1,
    data_cadastro_premissa TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    argumento_id_premissa INT UNSIGNED,
    cor_premissa TINYINT UNSIGNED,
    FOREIGN KEY (argumento_id_premissa) REFERENCES argumento(argumento_id) ON DELETE CASCADE
);

CREATE TABLE tipo_erro(
    tipo_erro_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    texto_tipo_erro VARCHAR(100),
    cor_tipo_erro TINYINT UNSIGNED
);

CREATE TABLE erro(
    erro_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    titulo_erro VARCHAR(@tamanhoTitulo),
    descricao_erro VARCHAR(@tamanhoDescricao),
    nome_original VARCHAR(@tamanhoTitulo),
    tipo_erro_id INT UNSIGNED,
    fonte_erro VARCHAR(@tamanhoTitulo),
);

CREATE TABLE exemplo_erro(
    exemplo_erro_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    descricao_exemplo_erro VARCHAR(1000),
    erro_id INT UNSIGNED,
    FOREIGN KEY (erro_id) REFERENCES erro(erro_id) ON DELETE CASCADE
);

CREATE TABLE resposta_erro(
    resposta_erro_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    resposta_id INT UNSIGNED,
    erro_id INT UNSIGNED,
    cont_avaliacoes_erro_reposta TINYINT UNSIGNED,
    FOREIGN KEY (resposta_id) REFERENCES resposta(resposta_id) ON DELETE CASCADE,
    FOREIGN KEY (erro_id) REFERENCES erro(erro_id) ON DELETE CASCADE
);

CREATE TABLE argumento_erro(
    argumento_erro_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    argumento_id INT UNSIGNED,
    erro_id INT UNSIGNED,
    cont_avaliacoes_erro_argumento TINYINT UNSIGNED,
    FOREIGN KEY (argumento_id) REFERENCES argumento(argumento_id) ON DELETE CASCADE,
    FOREIGN KEY (erro_id) REFERENCES erro(erro_id) ON DELETE CASCADE
);

CREATE TABLE premissa_erro(
    premissa_erro_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    premissa_id INT UNSIGNED,
    erro_id INT UNSIGNED,
    cont_avaliacoes_erro_premissa TINYINT UNSIGNED,
    FOREIGN KEY (premissa_id) REFERENCES premissa(premissa_id) ON DELETE CASCADE,
    FOREIGN KEY (erro_id) REFERENCES erro(erro_id) ON DELETE CASCADE
);

CREATE TABLE usuario_resposta_erro(
    usuario_resposta_erro_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    resposta_erro_id INT UNSIGNED,
    usuario_sinalizador_id INT UNSIGNED,
    comentario_sinalizador VARCHAR(@tamanhoDescricao),
    ordem_comentario SMALLINT UNSIGNED,
    data_cadastro_resposta_sinalizador TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (resposta_erro_id) REFERENCES resposta_erro(resposta_erro_id) ON DELETE CASCADE
);

CREATE TABLE usuario_argumento_erro(
    usuario_argumento_erro_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    argumento_erro_id INT UNSIGNED,
    usuario_sinalizador_id INT UNSIGNED,
    comentario_sinalizador VARCHAR(@tamanhoDescricao),
    ordem_comentario SMALLINT UNSIGNED,
    data_cadastro_argumento_sinalizador TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (argumento_erro_id) REFERENCES argumento_erro(argumento_erro_id) ON DELETE CASCADE
);

CREATE TABLE usuario_premissa_erro(
    usuario_premissa_erro_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    premissa_erro_id INT UNSIGNED,
    usuario_sinalizador_id INT UNSIGNED,
    comentario_sinalizador VARCHAR(@tamanhoDescricao),
    ordem_comentario SMALLINT UNSIGNED,
    data_cadastro_premissa_sinalizador TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (premissa_erro_id) REFERENCES premissa_erro(premissa_erro_id) ON DELETE CASCADE
);
