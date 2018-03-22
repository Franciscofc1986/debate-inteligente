<?php
require_once 'view/sobreView.php';

class SobreController {

    public function index() {
         $paginaSobre = new SobreView();
         $paginaSobre->exibir();
    }
}
?>