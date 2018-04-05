<?php
require_once 'view/temLogicaView.php';

class TemLogicaController {

    public function index() {
         $paginaTemLogica = new TemLogicaView();
         $paginaTemLogica->exibir();
    }
}
?>