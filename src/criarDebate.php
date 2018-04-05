<?php
    require_once 'controller/criarDebate.php';

    $criarDebateController = new CriarDebateController();

    if( isset($_POST['tipo_funcao']) )
    {
        $funcao = $_POST['tipo_funcao'];
        if($funcao == 'criarDebate'){
            $criarDebateController->salvarDebate($_POST['titulo_debate'], $_POST['texto_debate'], $_FILES['imagem_debate']);
        }
    }else{
        $criarDebateController->index();
    }
?>