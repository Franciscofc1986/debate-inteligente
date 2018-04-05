<?php
include 'enum/enum.php';

class Imagem {

    public function salvarImagem($local, $foto){
        $uploadOk = 0;

        if($foto['error'] == 0){
            $tokenFoto = uniqid();
            $imageFileType = strtolower(pathinfo($foto["name"],PATHINFO_EXTENSION));
            $local = $local . $tokenFoto . '.' . $imageFileType;
            

            // Check if file already exists
            if (file_exists($local)) {
                echo "Sorry, file already exists.";
                $uploadOk = Upload::Erro_Upload;
            }
            // Check file size
            if ($foto["size"] > 500000) {
                echo "Sorry, your file is too large.";
                $uploadOk = Upload::Erro_Upload;
            }
            // Allow certain file formats
            if($imageFileType != "jpg" && $imageFileType != "png" && $imageFileType != "jpeg") {
                echo "Sorry, only JPG, JPEG, PNG & GIF files are allowed.";
                $uploadOk = Upload::Erro_Upload;
            }

            if (move_uploaded_file($foto["tmp_name"], $local)) {
                $uploadOk = Upload::Sucesso_Upload;
            } else {
                echo "Sorry, there was an error uploading your file.";
            }
            
        }else{
            $uploadOk = Upload::Sem_Arquivo;
        }

        if($uploadOk > 0){
            return $tokenFoto . '.' . $imageFileType;
        }else{
            return "";
        }
    }
}
?>