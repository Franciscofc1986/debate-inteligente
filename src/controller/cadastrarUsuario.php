<?php
require_once 'view/cadastrarUsuarioView.php';

class CadastrarUsuarioController {

    public function index() {
         $paginaCadastrarUsuario = new CadastrarUsuarioView();
         $paginaCadastrarUsuario->exibir();
    }
}

?>