<?php

require_once 'model/dao/debate.php';

class DebateService {

    public function criarDebate($debate) {
         $debateDAO = new DebateDAO();
         return $debateDAO->salvarDebate($debate);
    }

    public function receberTodosDebates($usuarioId = NULL){
        $debateDAO = new DebateDAO();
        if (isset($usuarioId)) {
            return $debateDAO->receberDebatesDoUsuario($usuarioId);
        }else{
            return $debateDAO->receberTodosDebates();   
        }
    }
}

?>