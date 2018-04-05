<?php
require_once 'view/criarDebateView.php';
include 'comum/ChromePhp.php';

class CriarDebateController {

    public function index() {
         $paginaCriarDebate = new CriarDebateView();
         $paginaCriarDebate->exibir();
    }

    public function salvarDebate($titulo, $texto, $foto) {
        require_once 'model/debate.php';
        require_once 'model/service/debate.php';
        require_once 'comum/imagens.php';
        require_once 'model/alerta.php';

        $debate = new Debate();
        $debate->setTitulo($titulo);
        $debate->setDescricao($texto);

        $instImagens = new Imagem();
        $nomeArquivo = $instImagens->salvarImagem("img/debate/", $foto);
        $debate->setFoto($nomeArquivo);

        $debateService= new DebateService();
        $result = $debateService->criarDebate($debate);

        $alerta = new Alerta();
        if($result){
            $alerta->enviarAlerta("Debate criado com sucesso", 3000, "green");

            header('location: index.php');
        }else{
            $alerta->enviarAlerta("Falha ao tentar salvar o debate", 5000, "red");

            header('location: criarDebate.php');
        }
        ChromePhp::log($result);
    }
}
?>