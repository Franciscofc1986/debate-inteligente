<?php
require_once 'view/principalView.php';

class PrincipalController {

    public function index() {
         $paginaPrincipal = new PrincipalView();
         $paginaPrincipal->exibir();
    }
}

?>