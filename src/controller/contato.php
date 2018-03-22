<?php
require_once 'view/contatoView.php';

class ContatoController {

    public function index() {
         $paginaContato = new ContatoView();
         $paginaContato->exibir();
    }
}
?>