<!DOCTYPE html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8">
    <title >Tem Lógica</title>
    <!--Import Google Icon Font-->
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <!--Import materialize.css-->
    <link type="text/css" rel="stylesheet" href="css/materialize.min.css"  media="screen,projection"/>
    <link type="text/css" rel="stylesheet" href="css/style.css"/>
    <!--Let browser know website is optimized for mobile-->
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  </head>

  <body>
    <header>
    <?php include_once 'barra_topo.php'; ?>
    </header>

      <div class="row container">
        <div class="col s12">
        <h5 class="light">Tipos de Falácia</h5>
          <ul class="collapsible" data-collapsible="accordion">
              <li>
              <div class="collapsible-header"><i class="material-icons">filter_drama</i>Invenção de fatos</div>
              <div class="collapsible-body"><span>Consiste em mentir, dar falsa resposta ou apresentar informações imprecisas.</span></div>
              </li>
              <li>
              <div class="collapsible-header"><i class="material-icons">place</i>Teoria irrefutável</div>
              <div class="collapsible-body"><span>Informar um argumento com uma hipótese que não pode ser testada.
              <div class="card-panel amber lighten-5">Ex.: Ganhei na loteria porque Deus quis assim.</div>
              Uma proposição que não pode ser testada e refutada não possui valor.(Porém, depende do 
              conceito teológico de Deus, pois dependo deste, podendo ser testada qualquer afirmação 
              relativa de alguma maneira, que não precisa ser necessariamente da maneira científica, 
              principalmente quando essa a proposição não é sobre algo observável ou experimentável).</span></div>
              </li>
              <li>
              <div class="collapsible-header"><i class="material-icons">whatshot</i>Deus das lacunas</div>
              <div class="collapsible-body"><span>Responder a questões sem solução com explicações sobrenaturais 
              e/ou que não podem ser comprovadas.
              <div class="card-panel amber lighten-5">Ex.: Os passageiros do avião sobreviveram porque Deus interveio 
              no acidente.</div>
              Deus supre a falta de explicações, as lacunas. É uma teoria irrefutável.</span></div>
              </li>
          </ul>
        </div>
    </div>

    <?php include_once 'rodape.php'; ?>
    
    <!--Import jQuery before materialize.js-->
    <script type="text/javascript" src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="js/materialize.min.js"></script>
    <script type="text/javascript" src="js/app.js"></script> 
  </body>
</html>