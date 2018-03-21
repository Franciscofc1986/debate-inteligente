<?php

include 'ChromePhp.php';
include 'enum.php';
$funcao = $_POST['tipo_funcao'];

if($funcao == 'cadastrarUsuario'){
    function cadastrarUsuario() {
        $nome = $_POST['nome_usuario'];
        $email = $_POST['email_usuario'];
        $senha = $_POST['senha_usuario'];
        $foto = $_FILES['foto_usuario'];
        $uploadOk = 0;
        ChromePhp::log($_POST);
        ChromePhp::log($_FILES);

        if($foto['error'] == 0){
            $target_dir = "img/usuario/";
            $tokenFoto = uniqid();
            $imageFileType = strtolower(pathinfo($_FILES["foto_usuario"]["name"],PATHINFO_EXTENSION));
            $target_file = $target_dir . $tokenFoto . '.' . $imageFileType;
            

            // Check if file already exists
            if (file_exists($target_file)) {
                echo "Sorry, file already exists.";
                $uploadOk = Upload::Erro_Upload;
            }
            // Check file size
            if ($_FILES["foto_usuario"]["size"] > 500000) {
                echo "Sorry, your file is too large.";
                $uploadOk = Upload::Erro_Upload;
            }
            // Allow certain file formats
            if($imageFileType != "jpg" && $imageFileType != "png" && $imageFileType != "jpeg") {
                echo "Sorry, only JPG, JPEG, PNG & GIF files are allowed.";
                $uploadOk = Upload::Erro_Upload;
            }

            if (move_uploaded_file($_FILES["foto_usuario"]["tmp_name"], $target_file)) {
                $uploadOk = Upload::Sucesso_Upload;
            } else {
                echo "Sorry, there was an error uploading your file.";
            }
            
        }else{
            $uploadOk = Upload::Sem_Arquivo;
        }

        if($uploadOk > 0){
            include 'conectarBD.php';
            try {
                $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
                $sql = "INSERT INTO usuario (firstname, lastname, email)
                VALUES ('John', 'Doe', 'john@example.com')";
                // use exec() because no results are returned
                $pdo->exec($sql);
                echo "New record created successfully";
                }
            catch(PDOException $e)
                {
                echo $sql . "<br>" . $e->getMessage();
                }
            $pdo = null;
        }
    }

    cadastrarUsuario();
}

?>