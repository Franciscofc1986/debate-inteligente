<?php
require_once 'view/loginView.php';

class LoginController {

    public function index() {
         $paginaLogin = new LoginView();
         $paginaLogin->exibir();
    }
}
?>