<?php
class Debate {
    private $id;
    private $titulo;
    private $descricao;
    private $autor;
    private $data_criacao;
    private $foto;

    public function getId() {
        return $this->id;
    }

    public function setId($x) {
        $this->id = $x;
    }

    public function getTitulo() {
        return $this->titulo;
    }
    
    public function setTitulo($x) {
        $this->titulo = $x;
    }

    public function getDescricao() {
        return $this->descricao;
    }
    
    public function setDescricao($x) {
        $this->descricao = $x;
    }

    public function getAutor() {
        return $this->autor;
    }
    
    public function setAutor($x) {
        $this->autor = $x;
    }

    public function getDataCriacao() {
        return $this->data_criacao;
    }
    
    public function setDataCriacao($x) {
        $this->data_criacao = $x;
    }

    public function getFoto() {
        return $this->foto;
    }
    
    public function setFoto($x) {
        $this->foto = $x;
    }
}

?>