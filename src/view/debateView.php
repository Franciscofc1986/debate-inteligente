<?php
    class DebateView
    {
        public function exibir()
        {
            include_once 'comum/topo.php';
            
            echo '<div class="fixed-action-btn toolbar">
    <a class="btn-floating btn-large grey darken-3">
      <i class="large material-icons">mode_edit</i>
    </a>
    <ul>
      <li class=""></li>
      <li class="">
        <input type="text" placeholder="Comentário" id="autocomplete-input" class="autocomplete white-text" >
      </li>
      <li class=""><a href="#!"><i class="material-icons">send</i></a></li>
      <li class=""></li>
    </ul>
  </div>
  
      <div class="row container">

        <div class="col s12 m8 offset-m2 l6 offset-l3">
        <div class="card-panel grey lighten-5 z-depth-1">
          <div class="row valign-wrapper">
                <div class="card">
                <div class="card-image">
                <img src="img/terra-plana.jpg"> 
                </div>
            <div class="card-content">
            <span class="card-title">Debate sobre a terra plana</span>
              <p>A terra é realmente plana? Caso contrário, porque o 
              homem não voltou a pisar na lua?</p>
            </div>
          </div>
        </div></div></div>
    </div>
    
        <div class="row container">
      <section class="col s12">
        <h5 class="light">Comentários</h5>

        <article class="col s12">
            <div class="card">
             <div class="col s12 l6">
                <div class="card">
                    <div class="card-content texto_vetado red-text">
                        <p>Claro que a terra é plana. Se não fosse isso como não vemos a curvatura da terra?</p>
                    </div>
                </div>
            </div>

            <div class="col s12 l6">
                <div class="card">
                    <div class="card-content">
                        <span class="card-title">Argumentos</span>
                        <ul class="collapsible" data-collapsible="accordion">
                            <li>
                            <div class="progress red lighten-5" style=" margin-left: 2%; width: 95%;">
                                <div class="determinate red" style="width: 70%"></div>
                            </div>
                                <div class="collapsible-header ">
                                
                                    <i class="material-icons red-text">check_circle</i>
                                    <p class="texto_vetado red-text">Olhando para o horizonte vejo uma reta ao contrário de um arco.
                                    Olhando para o horizonte vejo uma reta ao contrário de um arco.
                                    Olhando para o horizonte vejo uma reta ao contrário de um arco.</p>
                                    
                                </div>
                                <div class="collapsible-body"><p>Ao olhar para o horizonte eu vejo uma 
                                    reta ao inves de um circuloAo olhar para o horizonte eu vejo uma 
                                    reta ao inves de um circuloAo olhar para o horizonte eu vejo uma 
                                    reta ao inves de um circuloAo olhar para o horizonte eu vejo uma 
                                    reta ao inves de um circuloAo olhar para o horizonte eu vejo uma 
                                    reta ao inves de um circulo</p>
                                     <p>
                                    <div class="right">
                                        <a class="btn-floating red lighten-3">
                                        <i class="material-icons">announcement</i></a>
                                    </div>
                                    </p>  
                                </div>
                                
                            </li>
                            <li>
                                <div class="collapsible-header texto_vetado red-text">
                                    <i class="material-icons">check_circle</i>
                                    As fotos da Nasa mostram a terra plana
                                </div>
                                <div class="collapsible-body"><p>Nas missões apolo 11 e 12, as fotos 
                                    divulgadas pela Nasa mostram o planeta com uma superficie plana.</p>
                                    <p>
                                    <div class="right">
                                        <a class="btn-floating red lighten-3">
                                        <i class="material-icons">announcement</i></a>
                                    </div>
                                    </p> 
                                </div>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
          </div>
        </article>

        <article class="col s12">
            <div class="card">
             <div class="col s12 l6">
                <div class="card">
                    <div class="card-content">
                        <p>Claro que a terra é plana. Se não fosse isso como não vemos a curvatura da terra?</p>
                    </div>
                </div>
            </div>

            <div class="col s12 l6">
                <div class="card">
                    <div class="card-content">
                        <span class="card-title">Argumentos</span>
                        
                    </div>
                </div>
            </div>
          </div>
        </article>

        <article class="col s12">
            <div class="card">
             <div class="col s12 l6">
                <div class="card">
                    <div class="card-content">
                        <p>Claro que a terra é plana. Se não fosse isso como não vemos a curvatura da terra?</p>
                    </div>
                </div>
            </div>

            <div class="col s12 l6">
                <div class="card">
                    <div class="card-content">
                        <span class="card-title">Argumentos</span>
                        <ul class="collapsible" data-collapsible="accordion">
                            <li>
                                <div class="collapsible-header">
                                    <i class="material-icons">check_circle</i>
                                    <p>Olhando para o horizonte vejo uma reta ao contrário de um arco/p>
                                    <p><span class="new badge red accent-2" data-badge-caption="">2</span></p>
                                    
                                </div>
                                <div class="collapsible-body"><p>Ao olhar para o horizonte eu vejo uma 
                                    reta ao inves de um circuloAo olhar para o horizonte eu vejo uma 
                                    reta ao inves de um circulo</p>
                                     <p>
                                    <div class="right">
                                        <a class="btn-floating red lighten-3">
                                        <i class="material-icons">announcement</i></a>
                                    </div>
                                    </p>  
                                </div>
                                
                            </li>
                            <li>
                                <div class="collapsible-header">
                                <i class="material-icons">check_circle</i>
                                As fotos da Nasa mostram a terra plana
                                </div>
                                <div class="collapsible-body"><p>Nas missões apolo 11 e 12, as fotos 
                                    divulgadas pela Nasa mostram o planeta com uma superficie plana.</p>
                                    <p>
                                    <div class="right">
                                        <a class="btn-floating red lighten-3">
                                        <i class="material-icons">announcement</i></a>
                                    </div>
                                    </p> 
                                </div>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
          </div>
        </article>

      </section>
    </div>';

            include_once 'comum/rodape.php';
        }
    }
?>