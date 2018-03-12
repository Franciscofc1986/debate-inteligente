
<?php include_once 'topo.php'; 
?>


      <div class="row container">
        <div class="col s12">
        <h5 class="light">Cadastrar usuario</h5>
            <div class="row">
                <div class="col s12">
                </div>
            </div>
            <form action="usuarioController.php" method="post" enctype="multipart/form-data" id="formCadastrar" name="formCadastrar">
                <input id="tipo_funcao" name="tipo_funcao" type="hidden" value="cadastrarUsuario">
                <div class="row">
                    <div class="input-field col s12">
                        <input placeholder="Nome do usuario" id="nome_usuario" name="nome_usuario" type="text" class="validate" required="" aria-required="true">
                        <label for="nome_usuario">Nome</label>
                    </div>
                </div>
                <div class="row">
                    <div class="input-field col s12">
                        <input id="email_usuario" name="email_usuario" type="email" class="validate" required="" aria-required="true">
                        <label for="email">E-mail</label>
                    </div>
                </div>
                <div class="row">
                    <div class="input-field col s12">
                        <input id="senha_usuario" name="senha_usuario" type="password" class="validate" required="" aria-required="true">
                        <label for="password">Senha</label>
                    </div>
                </div>
                <div class="row">
                    <div class="col s12">
                        <label for="foto_usuario">Foto do usuario</label>
                    </div>
                    <div class="input-field col s12">
                        
                        <div class="file-field">
                            <div class="btn">
                                <span>File</span>
                                <input type="file" id="foto_usuario" name="foto_usuario">     
                            </div>
                            <div class="file-path-wrapper">
                                <input class="file-path validate" type="text">
                                
                            </div>
                            
                        </div>
                    </div>
                </div>
                <div class="row center-align" style="margin-bottom: 10px;">
                    <button class="btn waves-effect waves-teal btn-flat grey darken-2 white-text" type="submit" name="action">Salvar
                        <i class="material-icons right">send</i>
                    </button>
                </div>
            </form>
        </div>
    </div>

    <?php include_once 'rodape.php'; ?>