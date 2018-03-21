<?php
    class LoginView
    {
        public function exibir()
        {
            include_once 'comum/topo.php';
            
            echo '<div class="container container-login">
                <div class="row">
                    <div class="col s0 m3 l4 ">
                    </div>
                    <form method="post" action="comum/logar.php" id="formlogin" name="formlogin" >
                        <div class="col s12 m6 l4 ">
                            <div class="card white">
                                <div class="card-content grey-text">
                                    <span class="card-title ">Logar</span>
                                    <div class="row">
                                        <div class="input-field col s12">
                                            <input id="email" type="email" name="email" class="validate">
                                            <label for="email">Email</label>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="input-field col s12">
                                            <input id="senha" type="password" name="senha" class="validate">
                                            <label for="senha">Password</label>
                                        </div>
                                    </div>
                                    <div class="row center-align" style="margin-bottom: 10px;">
                                        <button class="btn waves-effect waves-teal btn-flat grey darken-2 white-text" type="submit" name="action">Logar
                                            <i class="material-icons right">send</i>
                                        </button>
                                    </div>
                                    <div class="row">
                                    </div>
                                    <div class="row center-align" style="margin-bottom: 10px;">
                                        <a href="cadastrarUsuario.php" class="btn waves-effect waves-teal btn-flat grey darken-2 white-text">Cadastrar <i class="material-icons right">person_add</i></a>

                                    </div>
                                    <div class="row">
                                    </div>
                                    <div class="row center-align ">
                                        <div class="card-action">
                                            <a href="#" class="grey-text">Esqueci minha senha</a>
                                        </div>
                                    </div>
                                </div>

                            </div>
                        </div>
                    </form>
                    <div class="col s0 m3 l4 ">
                            </div>
                </div>
            </div>';

            include_once 'comum/rodape.php';
        }
    }
?>