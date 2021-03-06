<?php
echo '<nav class="z-depth-5">
        <a href="#" data-activates="slide-out" class="button-collapse menu-1 show-on-large"><i class="material-icons">menu</i></a>
        <a href="#" data-activates="slide-out-2" class="right button-collapse menu-2 show-on-large"><i class="material-icons">apps</i></a>
        <div class="nav-wrapper grey darken-3">
            <div class="container">
                <a href="#" class="brand-logo title-1">Tem lógica</a>
            </div> 
            <ul class="hide-on-med-and-down right">               
                <li>    
                   <div class="center row">
                      <div class="col s12 " >
                        <div class="row" id="topbarsearch">
                          <div class="input-field col s6 s12 grey-text">
                            <i class="grey-text material-icons prefix">search</i>
                            <input type="text" placeholder="buscar" id="autocomplete-input" class="autocomplete grey-text" >
                            </div>
                          </div>
                        </div>
                      </div>          
                  </li>                     
                <li>Bem vindo Francisco !</li>
            </ul>
        </div>
    </nav>
    
    <ul id="slide-out" class="side-nav">
      <li><div class="user-view">
        <div class="background">
          <img src="img/background.png">
        </div>
        <a href="#!user"><img class="circle" src="img/default.jpg"></a>
        <a href="#!name"><span class="bold black-text name">Francisco de Faria Cardoso</span></a>
        <a href="#!email"><span class="black-text email">francisco_faria@inatel.br</span></a>
      </div></li>
      <li><div class="divider"></div></li>
      <li><a class="subheader">Acesso rápido</a></li>
      <li><a href="#!"><i class="material-icons">home</i>Minha pagina inicial</a></li>
      <li><a href="#!"><i class="material-icons">playlist_add</i>Criar um debate</a></li>
      <li><a href="#!"><i class="material-icons">notifications</i>Notificações</a></li>
      <li><a href="#!"><i class="material-icons">person_add</i>Convidar amigo</a></li>
      <li><div class="divider"></div></li>
      <li><a class="subheader">Sair</a></li>
      <li><a class="waves-effect" href="#!"><i class="material-icons">exit_to_app</i>Deslogar</a></li>
    </ul>

    <ul id="slide-out-2" class="side-nav">
      <li><a href="login.html"><i class="material-icons">account_box</i>Logar</a></li>
      <li><a href="#!"><i class="material-icons">dvr</i>Regras</a></li>
      <li><a href="falacias.php"><i class="material-icons">speaker_notes_off</i>Falácias</a></li>
      <li><a href="#!"><i class="material-icons">contact_mail</i>Contato</a></li>
      <li><a href="#!"><i class="material-icons">info</i>Sobre o Site</a></li>
    </ul>';
?>