<?php
require_once 'view/falaciasView.php';

class FalaciasController {

    public function index() {
         $paginaFalacias = new FalaciasView();
         $paginaFalacias->exibir();
    }
}
?>