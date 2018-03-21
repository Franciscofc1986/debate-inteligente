<?php
    class PrincipalView
    {
        public function exibir()
        {
            include_once 'comum/topo.php';
            
            echo '<div class="row container">
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
                    homem não voltou a pisar na lua? Me diz</p>
                    </div>
                    <div class="card-action">
                        <a href="debate.php" class="btn waves-effect waves-light">Abrir </a>
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

            </div>';

            include_once 'comum/rodape.php';
        }
    }
?>