<?php
    require_once 'controller/criarDebate.php';

    $criarDebateController = new CriarDebateController();

    if( isset($_POST['tipo_funcao']) )
    {
        $funcao = $_POST['tipo_funcao'];
        if($funcao == 'criarDebate'){
            $criarDebateController->salvarDebate("oloco  bixo");
        }
    }else{
        $criarDebateController->index();
    }
?>