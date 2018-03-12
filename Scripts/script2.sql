INSERT INTO `temlogica_db`.`usuario` (`usuario_id`, `nome_usuario`, `senha_usuario`, 
`email_usuario`, `tipo_usuario`, `foto_usuario`, `data_cadastro_usuario`, 
`data_atualizacao_usuario`) 
VALUES (NULL, 'Francisco de Faria Cardoso', '123456', 'francisco_fc@yahoo.com.br', 
'2', '1.jpg', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

CREATE USER 'francisco'@'localhost' IDENTIFIED BY '***';
GRANT ALL PRIVILEGES ON *.* 
TO 'francisco'@'localhost' IDENTIFIED BY '***' WITH 
GRANT OPTION MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;
GRANT ALL PRIVILEGES ON `temlogica_db`.* TO 'francisco'@'localhost';