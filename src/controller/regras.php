<?php
require_once 'view/regrasView.php';

class RegrasController {

    public function index() {
         $paginaRegras = new RegrasView();
         $paginaRegras->exibir();
    }
}
?>