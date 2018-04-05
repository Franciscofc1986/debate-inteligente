<?php
require_once 'view/criarDebateView.php';

class CriarDebateController {

    public function index() {
         $paginaCriarDebate = new CriarDebateView();
         $paginaCriarDebate->exibir();
    }

    public function salvarDebate($teste) {
         echo $teste;
    }
}
?>