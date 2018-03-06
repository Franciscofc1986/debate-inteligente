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
      <section class="col s12 m6 l9">
        <h5 class="light">Meus debates</h5>

        <article class="col s12 l6">
        <div class="card">
            <div class="card-image">
              <img src="img/terra-plana.jpg"> 
            </div>
            <div class="card-content">
            <span class="card-title">Debate sobre a terra plana</span>
              <p>A terra é realmente plana? Caso contrário, porque o 
              homem não voltou a pisar na lua?</p>
            </div>
            <div class="card-action">
               <button class="btn waves-effect waves-light" type="submit" name="action">Abrir</button>
            </div>
          </div>
        </article>

        <article class="col s12 l6">
        <div class="card">
            <div class="card-image">
              <img src="img/Deus-existe.jpg"> 
            </div>
            <div class="card-content">
            <span class="card-title">Debate sobre a existência de Deus</span>
              <p>Se Deus existe, porque o mundo esta como esta ?</p>
            </div>
            <div class="card-action">
              <button class="btn waves-effect waves-light" type="submit" name="action">Abrir</button>
            </div>
          </div>
        </article>

        <article class="col s12 l6">
        <div class="card">
            <div class="card-image">
              <img src="img/terra-plana.jpg"> 
            </div>
            <div class="card-content">
            <span class="card-title">Debate sobre a terra plana</span>
              <p>A terra é realmente plana? Caso contrário, porque o 
              homem não voltou a pisar na lua?</p>
            </div>
            <div class="card-action">
               <button class="btn waves-effect waves-light" type="submit" name="action">Abrir</button>
            </div>
          </div>
        </article>

        <article class="col s12 l6">
        <div class="card">
            <div class="card-image">
              <img src="img/Deus-existe.jpg"> 
            </div>
            <div class="card-content">
            <span class="card-title">Debate sobre a existência de Deus</span>
              <p>Se Deus existe, porque o mundo esta como esta ?</p>
            </div>
            <div class="card-action">
              <button class="btn waves-effect waves-light" type="submit" name="action">Abrir</button>
            </div>
          </div>
        </article>

        <article class="col s12 l6">
        <div class="card">
            <div class="card-image">
              <img src="img/terra-plana.jpg"> 
            </div>
            <div class="card-content">
            <span class="card-title">Debate sobre a terra plana</span>
              <p>A terra é realmente plana? Caso contrário, porque o 
              homem não voltou a pisar na lua?</p>
            </div>
            <div class="card-action">
               <button class="btn waves-effect waves-light" type="submit" name="action">Abrir</button>
            </div>
          </div>
        </article>

        <article class="col s12 l6">
        <div class="card">
            <div class="card-image">
              <img src="img/Deus-existe.jpg"> 
            </div>
            <div class="card-content">
            <span class="card-title">Debate sobre a existência de Deus</span>
              <p>Se Deus existe, porque o mundo esta como esta ?</p>
            </div>
            <div class="card-action">
              <button class="btn waves-effect waves-light" type="submit" name="action">Abrir</button>
            </div>
          </div>
        </article>

      </section>

      <aside class="col s12 m6 l3">
      <h5 class="light">Ultimos debates</h5>
        <ul class="collection">
          <li class="collection-item avatar">
            <img src="img/terra-plana.jpg" alt="" class="circle">
            <span class="title">Debate sobre a terra plana</span>
            <p>A terra é realmente plana? Caso contrário, porque o homem não voltou a pisar na lua?
            </p>
               <button class="btn waves-effect waves-light" type="submit" name="action">Abrir</button>

          </li>
          <li class="collection-item avatar">
            <img src="img/Deus-existe.jpg" alt="" class="circle">
            <span class="title">Debate sobre a existência de Deus</span>
            <p>Se Deus existe, porque o mundo esta como esta ?
            </p>
            <button class="btn waves-effect waves-light" type="submit" name="action">Abrir</button>
          </li>
        </ul>
      </aside>

    </div>

    <?php include_once 'rodape.php'; ?>
    
    <!--Import jQuery before materialize.js-->
    <script type="text/javascript" src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="js/materialize.min.js"></script>
    <script type="text/javascript" src="js/app.js"></script> 
  </body>
</html>