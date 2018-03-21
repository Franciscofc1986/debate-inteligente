<?php
require_once 'view/debateView.php';

class DebateController {

    public function index() {
         $paginaDebate = new DebateView();
         $paginaDebate->exibir();
    }
}
?>