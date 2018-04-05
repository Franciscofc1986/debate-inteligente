<?php
require_once 'view/filosofiaView.php';

class FilosofiaController {

    public function index() {
         $paginaFilosofia = new FilosofiaView();
         $paginaFilosofia->exibir();
    }
}
?>