<?php
class Usuario {
    private $id;
    private $nome;
    private $senha;
    private $email;
    private $tipo;
    private $foto;

    public function getId() {
        return $this->id;
    }

    public function setId($x) {
        $this->id = $x;
    }

    public function getNome() {
        return $this->nome;
    }
    
    public function setNome($x) {
        $this->nome = $x;
    }

    public function getSenha() {
        return $this->senha;
    }
    
    public function setSenha($x) {
        $this->senha = $x;
    }

    public function getEmail() {
        return $this->email;
    }
    
    public function setEmail($x) {
        $this->email = $x;
    }

    public function getTipo() {
        return $this->tipo;
    }
    
    public function setTipo($x) {
        $this->tipo = $x;
    }

    public function getFoto() {
        return $this->foto;
    }
    
    public function setFoto($x) {
        $this->foto = $x;
    }

    public function verificarSessao(){
        session_start();
        if(!isset ($_SESSION['usuario']) == true)
        {
            return false;
        } 
        else{
            return true;
        }
    }
}

?>