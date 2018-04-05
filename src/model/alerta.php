<?php
class Alerta {
    private $textoAlerta;
    private $tempoAlerta;
    private $corAlerta;

    public function getTextoAlerta() {
        return $this->textoAlerta;
    }

    public function setTextoAlerta($x) {
        $this->textoAlerta = $x;
    }

    public function getTempoAlerta() {
        return $this->tempoAlerta;
    }

    public function setTempoAlerta($x) {
        $this->tempoAlerta = $x;
    }

    public function getCorAlerta() {
        return $this->corAlerta;
    }

    public function setCorAlerta($x) {
        $this->corAlerta = $x;
    }

    public function verificaSeTemAlerta(){
        
        if(!isset ($_SESSION['textoAlerta']) == true)
        {
            return false;
        }else{
            return true;
        }
    }

    public function receberAlerta(){
        $this->setTextoAlerta($_SESSION['textoAlerta']);
        $this->setTempoAlerta($_SESSION['tempoAlerta']);
        $this->setCorAlerta($_SESSION['corAlerta']);
        unset ($_SESSION['textoAlerta']);
        unset ($_SESSION['tempoAlerta']);
        unset ($_SESSION['corAlerta']);

    }

    public function enviarAlerta($texto, $tempo, $cor){
        $_SESSION['textoAlerta'] = $texto;
        $_SESSION['tempoAlerta'] = $tempo;
        $_SESSION['corAlerta'] = $cor;

    }

}

?>