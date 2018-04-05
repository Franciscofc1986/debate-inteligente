<?php
require_once 'view/principalView.php';
include 'comum/ChromePhp.php';

class PrincipalController {

    public function index() {
        require_once 'model/service/debate.php';

        $debateService = new DebateService();

        $listaDebates = $debateService->receberTodosDebates();
        ChromePhp::log($listaDebates[2]);
        $paginaPrincipal = new PrincipalView();
        $paginaPrincipal->exibir($listaDebates);
    }
}

?>