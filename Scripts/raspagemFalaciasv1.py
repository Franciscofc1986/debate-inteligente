import json
import sys
import datetime
from urllib.request import urlopen
from lxml import etree
from lxml import html
from io import StringIO
from googletrans import Translator

def rodarScript() :

    
    htmlCode = '''<html> <body>
        <div class="list-group mx-auto" style="max-width:940px;"><div id="pageresults">
        <a href="/logicalfallacies/Accent-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia de sotaque</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando o significado de uma palavra, frase ou ideia inteira é interpretado de forma diferente, mudando onde o acento cai.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">sotaque, falácia da ênfase, falácia do sotaque, falácia da prosódia, sotaque enganoso</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Accident-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia do acidente</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando se tenta aplicar uma regra geral a todas as situações em que claramente há exceções à regra. </font><font style="vertical-align: inherit;">Regras ou leis simplistas raramente levam em consideração exceções legítimas, e ignorar essas exceções é contornar a razão para preservar a ilusão de uma lei perfeita. </font><font style="vertical-align: inherit;">As pessoas gostam de simplicidade e muitas vezes preferem manter a simplicidade em detrimento da racionalidade.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">a dicto simpliciter ad dictum secundum quid, destruindo a exceção, dicto secundum quid ad dictum simpliciter, dicto simpliciter, acidente inverso, acidente reverso, falácia da regra geral, generalização abrangente</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Ad-Fidentia" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Ad Fidentia</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Atacar a autoconfiança da pessoa no lugar do argumento ou da evidência.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">argumentum ad fidentia, contra a autoconfiança</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Ad-Hoc-Rescue" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Resgate ad hoc</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Muitas vezes, queremos desesperadamente estar certos e nos apegar a certas crenças, apesar de qualquer evidência apresentada em contrário. </font><font style="vertical-align: inherit;">Como resultado, começamos a inventar desculpas para explicar por que nossa crença ainda pode ser verdadeira, e ainda é verdadeira, apesar do fato de não termos nenhuma evidência real do que estamos inventando.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">inventando coisas, falácia MSU</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Ad-Hominem-Abusive" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Ad Hominem (Abusivo)</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Atacar a pessoa que está argumentando, em vez do próprio argumento, quando o ataque à pessoa é completamente irrelevante para o argumento que a pessoa está apresentando.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">argumento ad hominem, abuso pessoal, ataques pessoais, falácia abusiva, apelo à pessoa, condenação da fonte, xingamentos, refutação por caricatura, contra a pessoa, contra o homem</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Ad-Hominem-Circumstantial" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Ad hominem (circunstancial)</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Sugerir que a pessoa que está fazendo o argumento é tendenciosa ou predisposta a assumir uma determinada posição e, portanto, o argumento é necessariamente inválido.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Argumentum ad hominem, apelo ao motivo, apelo ao interesse pessoal, argumento a partir de motivos, conflito de interesses, motivos falsos, cinismo ingênuo, motivos questionadores, interesses escusos</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Ad-Hominem-Guilt-by-Association" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Ad Hominem (Culpa por Associação)</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando a fonte é vista negativamente por causa de sua associação com outra pessoa ou grupo que já é visto negativamente.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">argumentum ad hominem, falácia de associação, falácia de má companhia, falácia de empresa que você mantém, falácia de eles não são como nós, falácia de transferência</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Ad-Hominem-Tu-quoque" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Ad Hominem (Tu quoque)</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Reivindicar o argumento é falho ao apontar que aquele que apresenta o argumento não está agindo de forma consistente com as reivindicações do argumento.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">argumentum ad hominem tu quoque, apelo à hipocrisia, você também falácia, hipocrisia, inconsistência pessoal</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Affirmative-Conclusion-from-a-Negative-Premise" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Conclusão afirmativa de uma premissa negativa</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A conclusão de um silogismo categórico de forma padrão é afirmativa, mas pelo menos uma das premissas é negativa. </font><font style="vertical-align: inherit;">Quaisquer formas válidas de silogismos categóricos que afirmam uma premissa negativa devem ter uma conclusão negativa.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">negativa ilícita, tirando uma conclusão negativa de premissas afirmativas, falácia de premissas negativas</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Affirming-a-Disjunct" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Afirmando um Disjunto</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Fazendo a falsa suposição de que, quando apresentado a uma possibilidade ou/ou, se uma das opções for verdadeira, a outra deve ser falsa. </font><font style="vertical-align: inherit;">É quando o “ou” não é especificamente definido como exclusivo.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">a falácia do disjunto alternativo, falso disjuntivo excludente, afirmando um disjunto, a falácia do silogismo alternativo, afirmando uma alternativa, silogismo disjuntivo impróprio, falácia do silogismo disjuntivo</font></font></i></div>
            </div>
        </a>
        <noscript><a href="/qa?seopagecat=&seobatch=10"><button type="button" class="d-inline btn btn-lg btn-primary mt-2 mb-1">Next Page</button></a></noscript>
        <a href="/logicalfallacies/Affirming-the-Consequent" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Afirmando o Conseqüente</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Um erro na lógica formal em que se o consequente é considerado verdadeiro, o antecedente é considerado verdadeiro, como resultado.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">erro inverso, falácia do conseqüente, afirmando o conseqüente, afirmação do conseqüente</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Alleged-Certainty" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Certeza Alegada</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Afirmar uma conclusão sem evidências ou premissas, por meio de uma afirmação que faz com que a conclusão pareça certa quando, na verdade, não é.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">assumindo a conclusão</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Alphabet-Soup" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Sopa de alfabeto</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">O uso deliberado e excessivo de siglas e abreviaturas para parecer mais entendido no assunto ou confundir os outros.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Alternative-Advance" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Avanço Alternativo</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando alguém é apresentado a apenas duas opções, ambas essencialmente iguais, apenas com palavras diferentes. </font><font style="vertical-align: inherit;">Essa técnica é muito usada em vendas. </font><font style="vertical-align: inherit;">O raciocínio falacioso seria cometido pela pessoa que aceita as opções como as únicas opções, o que provavelmente estaria em um nível subconsciente, já que praticamente qualquer pessoa - se pensasse sobre isso - reconheceria a existência de outras opções.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">situação perde-perde</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Amazing-Familiarity" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Familiaridade incrível</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">O argumento contém informações que parecem impossíveis de serem obtidas – como se viessem de um autor onisciente. </font><font style="vertical-align: inherit;">Esse tipo de escrita/contação de histórias é característico da ficção, portanto, quando usado em um argumento, deve lançar dúvidas.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">argumento da onisciência, "como diabos você pode saber disso?"</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Ambiguity-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia de ambiguidade</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando uma frase pouco clara com múltiplas definições é usada dentro do argumento; </font><font style="vertical-align: inherit;">portanto, não suporta a conclusão. </font><font style="vertical-align: inherit;">Alguns dirão que palavras isoladas contam para a falácia da ambigüidade, que na verdade é uma forma específica de falácia conhecida como equívoco.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">afirmação ambígua, anfibolia, anfibologia, ambigüidade semântica, imprecisão</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Anonymous-Authority" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Autoridade anônima</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando uma fonte não especificada é usada como evidência para a alegação. </font><font style="vertical-align: inherit;">Isso é comumente indicado por frases como “Dizem que...”, “Já foi dito...”, “Ouvi dizer que...”, “Estudos mostram...”, ou grupos generalizados como, “os cientistas dizem...”</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">apelo à autoridade anônima</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Anthropomorphism" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Antropomorfismo</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A atribuição de características e propósitos humanos a objetos inanimados, animais, plantas ou outros fenômenos naturais, ou a deuses. </font><font style="vertical-align: inherit;">Isso se torna uma falácia lógica quando usado no contexto de um argumento.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">personificação</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Appeal-to-Accomplishment" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo à Realização</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando o argumento que está sendo feito é protegido de críticas baseadas no nível de realização de quem está argumentando. </font><font style="vertical-align: inherit;">Uma forma dessa falácia também ocorre quando os argumentos são avaliados pelas realizações, ou sucesso, da pessoa que apresenta o argumento, e não pelos méritos do próprio argumento.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">apelo ao sucesso</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Appeal-to-Anger" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo à raiva</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando as emoções de raiva, ódio ou raiva são substituídas por evidências em uma discussão.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">apelo ao ódio, repugnância, apelo à indignação, etc.</font></font></i></div>
            </div>
        </a>
        <noscript><a href="/qa?seopagecat=&seobatch=20"><button type="button" class="d-inline btn btn-lg btn-primary mt-2 mb-1">Next Page</button></a></noscript>
        <a href="/logicalfallacies/Appeal-to-Authority" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo à autoridade</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Insistir que uma alegação é verdadeira simplesmente porque uma autoridade válida ou especialista no assunto disse que era verdadeira, sem qualquer outra evidência de suporte oferecida. </font><font style="vertical-align: inherit;">Veja também o apelo à falsa autoridade.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">argumento de autoridade, ipse dixit, argumentum ad verecundiam</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Appeal-to-Celebrity" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo à celebridade</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Aceitar a reivindicação de uma celebridade com base em seu status de celebridade, não na força do argumento.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Appeal-to-Closure" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo ao Encerramento</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Aceitar evidências com base no desejo de encerramento - ou acabar com o problema. </font><font style="vertical-align: inherit;">Embora o desejo de fechamento seja um fenômeno psicológico real que afeta o bem-estar dos indivíduos, usar o "fechamento" como uma razão para aceitar evidências que de outra forma não seriam aceitas é falacioso.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">apelo à justiça</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Appeal-to-Coincidence" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo à Coincidência</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Concluir que um resultado é devido ao acaso quando as evidências sugerem fortemente o contrário. </font><font style="vertical-align: inherit;">O apelo à variação da sorte usa a sorte no lugar da coincidência ou do acaso.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">apelar à sorte, apelar ao azar, apelar à boa sorte</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Appeal-to-Common-Belief" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo à crença comum</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando a afirmação de que a maioria ou muitas pessoas em geral ou de um grupo particular aceita uma crença como verdadeira é apresentada como evidência para a afirmação. </font><font style="vertical-align: inherit;">Aceitar a crença de outra pessoa, ou a crença de muitas pessoas, sem exigir evidências de por que essa pessoa aceita a crença é um pensamento preguiçoso e uma forma perigosa de aceitar informações.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">argumentum ad populum, apelo à crença aceita, apelo à democracia, apelo à crença generalizada, apelo às massas, apelo à crença, apelo à maioria, argumento por consenso, falácia do consenso, autoridade de muitos, falácia do movimento, apelo ao número, argumentum ad numerum, argumentum consenso gentium, apelo à multidão, apelo à galeria, consenso gentium, apelo da multidão, conformidade social, valor da comunidade, vox populi</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Appeal-to-Common-Folk" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo ao Povo Comum</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">No lugar das evidências, tentando estabelecer uma conexão com o público a partir do fato de ser uma “pessoa comum” como cada um deles. </font><font style="vertical-align: inherit;">Em seguida, sugerindo que sua proposição é algo que todas as pessoas comuns acreditam ou deveriam aceitar.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">apelo ao homem comum</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Appeal-to-Common-Sense" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo ao bom senso</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Afirmar que sua conclusão ou fatos são apenas "senso comum" quando, na verdade, eles não são. Devemos argumentar por que acreditamos que algo é senso comum se houver alguma dúvida de que a crença não é comum, em vez de apenas afirmar que isso é.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Appeal-to-Complexity" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo à Complexidade</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Concluindo que só porque você não entende o argumento, o argumento não é verdadeiro, falho ou improvável. </font><font style="vertical-align: inherit;">Esta é uma forma específica do argumento da ignorância.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Appeal-to-Consequences" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo às Consequências</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Concluir que uma ideia ou proposição é verdadeira ou falsa porque as consequências de ser verdadeira ou falsa são desejáveis ​​ou indesejáveis. </font><font style="vertical-align: inherit;">A falácia reside no fato de que a desejabilidade não está relacionada ao valor de verdade da ideia ou proposição. </font><font style="vertical-align: inherit;">Isso vem em duas formas: a positiva e a negativa.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">argumentum ad consequenteiam, apelo às consequências de uma crença, argumento às consequências, argumento das [das] consequências</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Appeal-to-Definition" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo à Definição</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Usar a definição limitada de um termo de um dicionário como evidência de que o termo não pode ter outro significado, significado expandido ou mesmo significado conflitante.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">apelo ao dicionário, vitória por definição</font></font></i></div>
            </div>
        </a>
        <noscript><a href="/qa?seopagecat=&seobatch=30"><button type="button" class="d-inline btn btn-lg btn-primary mt-2 mb-1">Next Page</button></a></noscript>
        <a href="/logicalfallacies/Appeal-to-Desperation" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo ao desespero</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Argumentar que sua conclusão, solução ou proposição está correta com base no fato de que algo deve ser feito e sua solução é "algo".</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Appeal-to-Emotion" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo à emoção</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Esta é a categoria geral de muitas falácias que usam a emoção no lugar da razão para tentar vencer a discussão. </font><font style="vertical-align: inherit;">É um tipo de manipulação usado no lugar da lógica válida.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">apelo ao pathos, argumento pela veemência, brincar com as emoções, apelo emocional, para as crianças</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Appeal-to-Equality" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo à Igualdade</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Uma afirmação é considerada verdadeira ou falsa com base em uma suposta pretensão de igualdade, onde exatamente o que é "igual" não é esclarecido e não é suportado pelo argumento.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">apelo ao igualitarismo, apelo à equidade</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Appeal-to-Extremes" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo aos Extremos</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Tentar erroneamente transformar um argumento razoável em absurdo, levando o argumento ao extremo.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Appeal-to-Faith" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo à fé</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Isso é um abandono da razão em um argumento e um apelo à fé, geralmente quando a razão claramente leva à refutação da conclusão de um argumento. </font><font style="vertical-align: inherit;">É a afirmação de que é preciso ter (o tipo certo de) fé para entender o argumento.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Appeal-to-False-Authority" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo à falsa autoridade</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Usar uma suposta autoridade como evidência em seu argumento quando a autoridade não é realmente uma autoridade sobre os fatos relevantes para o argumento.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">apelar para autoridade duvidosa, apelar para autoridade duvidosa, apelar para autoridade imprópria, apelar para autoridade inadequada, apelar para autoridade irrelevante, apelar para autoridade mal colocada, apelar para autoridade não qualificada, argumento de autoridade falsa</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Appeal-to-Fear" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo ao medo</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando o medo, não baseado em evidências ou razão, está sendo usado como o principal motivador para fazer os outros aceitarem uma ideia, proposição ou conclusão.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">argumentum in terrorem, argumentum ad metum, argumento de consequências adversas, táticas de intimidação</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Appeal-to-Flattery" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo à lisonja</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando é feita uma tentativa de obter apoio para um argumento, não pela força do argumento, mas usando a lisonja daqueles a quem você deseja que aceitem seu argumento. </font><font style="vertical-align: inherit;">Essa falácia geralmente é a causa de as pessoas serem induzidas a fazer algo que realmente não querem fazer.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">polimento de maçã, engraxamento de rodas, focinho marrom, apelo ao orgulho / argumentum ad superbiam, apelo à vaidade</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Appeal-to-Force" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo à força</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando força, coerção ou mesmo ameaça de força é usada no lugar de uma razão na tentativa de justificar uma conclusão.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">argumentum ad baculum, argumento ao porrete, apelo ao bastão</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Appeal-to-Heaven" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo ao Céu</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Afirmar a conclusão deve ser aceito porque é a “vontade de Deus” ou “a vontade dos deuses”. </font><font style="vertical-align: inherit;">Na mente daqueles que cometem a falácia, e daqueles que permitem passar por uma razão válida, a vontade de Deus não é apenas cognoscível, mas a pessoa que argumenta a conhece, e nenhuma outra razão é necessária.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">deus vult, gott mit uns, destino manifesto, aliança especial</font></font></i></div>
            </div>
        </a>
        <noscript><a href="/qa?seopagecat=&seobatch=40"><button type="button" class="d-inline btn btn-lg btn-primary mt-2 mb-1">Next Page</button></a></noscript>
        <a href="/logicalfallacies/Appeal-to-Intuition" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo à Intuição</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Avaliar um argumento com base na "intuição" ou "intuição" que não pode ser articulado, em vez de avaliar o argumento usando a razão.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">apelo ao intestino</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/appeal-to-loyalty.html" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo à Lealdade</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando alguém é implícita ou explicitamente encorajado a considerar a lealdade ao avaliar o argumento quando a verdade do argumento é independente da lealdade. </font><font style="vertical-align: inherit;">Alternativamente, considera-se lealdade ao concluir que o argumento é verdadeiro, falso ou não...</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">apelo ao patriotismo</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Appeal-to-Nature" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo à Natureza</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando usado como falácia, a crença ou sugestão de que “natural” é melhor que “antinatural” com base em sua naturalidade. </font><font style="vertical-align: inherit;">Muitas pessoas adotam isso como uma crença padrão. </font><font style="vertical-align: inherit;">É a crença de que o que é natural deve ser bom (ou qualquer outro julgamento avaliativo positivo) e o que não é natural deve ser ruim (ou qualquer outro julgamento avaliativo negativo).</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Argumentum ad Naturam</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Appeal-to-Normality" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo à Normalidade</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Usar normas sociais para determinar o que é bom ou ruim. </font><font style="vertical-align: inherit;">É a ideia de que a normalidade é o padrão da bondade. </font><font style="vertical-align: inherit;">Isso é falacioso porque as normas sociais não são as mesmas normas encontradas na natureza ou normas que são sinônimos da função ideal de um sistema criado. </font><font style="vertical-align: inherit;">A conclusão, "portanto, é bom" muitas vezes não é dita, mas está claramente implícita.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Appeal-to-Novelty" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo à novidade</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Afirmar que algo novo ou moderno é superior ao status quo, baseado exclusivamente em sua novidade.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">argumentum ad novitatem, apelo ao novo, ad novitam [às vezes escrito como]</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Appeal-to-Pity" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo à Piedade</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A tentativa de desviar a atenção da verdade da conclusão pelo uso da piedade.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">ad misericordiam, apelo à simpatia, apelo à vitimização</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Appeal-to-Popularity" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo à popularidade</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Usar a popularidade de uma premissa ou proposição como evidência de sua veracidade. </font><font style="vertical-align: inherit;">Esta é uma falácia muito difícil de detectar porque o nosso “bom senso” nos diz que se algo é popular, deve ser bom/verdadeiro/válido, mas não é assim, especialmente em uma sociedade onde o marketing inteligente, as políticas sociais e peso e dinheiro podem comprar popularidade.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">argumentum ad numram, apelo à crença comum</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Appeal-to-Possibility" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo à Possibilidade</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando uma conclusão é assumida não porque provavelmente é verdadeira, mas porque é possível que seja verdadeira, não importa quão improvável seja.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Appeal-to-Ridicule" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo ao Ridículo</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apresentar o argumento de forma que o faça parecer ridículo, geralmente deturpando o argumento ou usando exageros.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">reductio ad ridiculum, apelo à zombaria, a risada do cavalo</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Appeal-to-Self-evident-Truth" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo à Verdade Autoevidente</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Fazer a afirmação de que algo é "auto-evidente" quando não é auto-evidente em vez de argumentar uma afirmação com a razão. </font><font style="vertical-align: inherit;">Em termos cotidianos, algo é "auto-evidente" quando entender o que significa imediatamente resulta em saber que é verdadeiro, como 2+2=4.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <noscript><a href="/qa?seopagecat=&seobatch=50"><button type="button" class="d-inline btn btn-lg btn-primary mt-2 mb-1">Next Page</button></a></noscript>
        <a href="/logicalfallacies/Appeal-to-Spite" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo ao rancor</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Substituir rancor (má vontade ou ódio mesquinho pela disposição de irritar, aborrecer ou frustrar) como evidência em um argumento ou como razão para apoiar ou rejeitar uma reivindicação.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">argumentum ad odium</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Appeal-to-Stupidity" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo à Estupidez</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Tentar fazer com que o público desvalorize a razão e o discurso intelectual, ou desvalorizar a razão e o discurso intelectual com base na retórica de um argumentador.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Appeal-to-Tradition" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo à Tradição</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Usar as preferências históricas do povo (tradição), em geral ou tão específicas quanto as preferências históricas de um único indivíduo, como evidência de que a preferência histórica está correta. </font><font style="vertical-align: inherit;">Muitas vezes as tradições são passadas de geração em geração sem outra explicação além de “sempre foi feito assim” – o que não é um motivo, é a ausência de um motivo.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">argumentum ad antiquitatem, apelo à prática comum, apelo à antiguidade, apelo à sabedoria tradicional, prova da tradição, apelo à prática passada, sabedoria tradicional</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Appeal-to-Trust" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo à confiança</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A crença de que, se uma fonte é considerada confiável ou não confiável, qualquer informação dessa fonte deve ser verdadeira ou falsa, respectivamente. </font><font style="vertical-align: inherit;">Isso é problemático porque cada argumento, reivindicação ou proposição deve ser avaliado por seus próprios méritos.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">apelo à desconfiança [oposto], apelo à confiabilidade</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Appeal-to-the-Law" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo à Lei</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando seguir a lei é considerado a coisa moralmente correta a se fazer, sem justificativa, ou quando infringir a lei é considerado a coisa moralmente errada a se fazer, sem justificativa.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Appeal-to-the-Moon" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelo à Lua</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Usando o argumento “Se pudermos colocar um homem na lua, poderíamos...” como evidência para o argumento.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">argumentum ad lunam</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Argument-by-Emotive-Language" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Argumento por linguagem emotiva</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Substituir fatos e evidências por palavras que mexam com a emoção, na tentativa de manipular os outros para que aceitem a verdade do argumento.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">palavras carregadas, linguagem carregada, eufemismos</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Argument-by-Fast-Talking" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Argumento por falar rápido</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando a fala rápida é vista como inteligência e/ou confiança na veracidade do argumento de alguém; </font><font style="vertical-align: inherit;">portanto, visto como evidência da verdade do próprio argumento. </font><font style="vertical-align: inherit;">A falácia também é cometida pela pessoa que está falando quando está tentando deliberadamente não permitir que o público tenha tempo suficiente para processar o argumento; </font><font style="vertical-align: inherit;">portanto, aceitá-lo ou, pelo menos, não rejeitá-lo.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Argument-by-Gibberish" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Argumento por Gibberish</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando um jargão incompreensível ou um jargão incoerente simples é usado para dar a aparência de um argumento forte, no lugar de evidências ou razões válidas para aceitar o argumento.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">perplexidade, argumento por jargão [prestigioso]</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Argument-by-Personal-Charm" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Argumento por charme pessoal</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando uma discussão é fortalecida pelas características pessoais da pessoa que argumenta, muitas vezes referida como “charme”.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">apelo sexual [forma de], extravagância, eloqüência</font></font></i></div>
            </div>
        </a>
        <noscript><a href="/qa?seopagecat=&seobatch=60"><button type="button" class="d-inline btn btn-lg btn-primary mt-2 mb-1">Next Page</button></a></noscript>
        <a href="/logicalfallacies/Argument-by-Pigheadedness" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Argumento da teimosia</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Esta é uma recusa em aceitar um argumento bem comprovado por uma das muitas razões relacionadas à teimosia.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">argumento por teimosia, falácia da ignorância invencível</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Argument-by-Repetition" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Argumento por Repetição</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Repetir um argumento ou uma premissa repetidas vezes no lugar de melhores evidências de apoio.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">argumento da irritação, prova por afirmação</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Argument-by-Selective-Reading" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Argumento por Leitura Seletiva</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando uma série de argumentos ou reivindicações é feita e o oponente age como se o argumento mais fraco fosse o melhor. </font><font style="vertical-align: inherit;">Esta é uma forma de escolha de cereja e muito semelhante à falácia da atenção seletiva.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Argument-from-Age" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Argumento da idade</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">O equívoco de que as gerações anteriores tinham sabedoria superior ao homem moderno, portanto, as conclusões que dependem dessa sabedoria são vistas como verdadeiras ou mais verdadeiras do que realmente são.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">sabedoria dos antigos</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Argument-from-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Argumento da falácia</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Concluir que o valor de verdade de um argumento é falso com base no fato de que o argumento contém uma falácia.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">argumentum ad logicam, refutação por falácia, argumento para a lógica, falácia de falácia, falácia de falácia, falácia de más razões [forma de]</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Argument-from-False-Authority" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Argumento da Falsa Autoridade</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando uma pessoa que faz uma reclamação é apresentada como um especialista em quem se deve confiar quando sua especialização não está na área em discussão.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Argument-from-Hearsay" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Argumento de boato</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apresentar o depoimento de uma fonte que não seja testemunha ocular do evento em questão. </font><font style="vertical-align: inherit;">Foi demonstrado conclusivamente que a cada passagem de informação, via transmissão analógica, o conteúdo da mensagem muda. </font><font style="vertical-align: inherit;">Cada pequena mudança pode e muitas vezes leva a muitas mudanças mais significativas, como no efeito borboleta na teoria do caos.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">o jogo do telefone, sussurros chineses, evidência anedótica, falácia anedótica/falácia Volvo [forma de]</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Argument-from-Ignorance" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Argumento da Ignorância</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A suposição de uma conclusão ou fato baseado principalmente na falta de evidência em contrário. </font><font style="vertical-align: inherit;">Geralmente melhor descrito por “ausência de evidência não é evidência de ausência”.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">ad ignorantiam, apelo à ignorância, apelo ao mistério [forma de], falácia do cisne negro [forma de], falácia peruca [forma de]</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Argument-from-Incredulity" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Argumento da Incredulidade</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Concluindo que, porque você não pode ou se recusa a acreditar em algo, isso não deve ser verdadeiro, improvável ou o argumento deve ser falho.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">argumento de espanto pessoal, argumento de incredulidade pessoal, incredulidade pessoal</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Argument-from-Silence" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Argumento do Silêncio</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Tirar uma conclusão com base no silêncio do oponente, quando o oponente se recusa a depor por qualquer motivo.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">argumento e silêncio</font></font></i></div>
            </div>
        </a>
        <noscript><a href="/qa?seopagecat=&seobatch=70"><button type="button" class="d-inline btn btn-lg btn-primary mt-2 mb-1">Next Page</button></a></noscript>
        <a href="/logicalfallacies/Argument-of-the-Beard" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Argumento da barba</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando alguém argumenta que nenhuma distinção útil pode ser feita entre dois extremos, apenas porque não há momento ou ponto definível no espectro onde os dois extremos se encontram. </font><font style="vertical-align: inherit;">O nome vem do paradoxo da pilha na filosofia, usando a barba de um homem como exemplo. </font><font style="vertical-align: inherit;">Em que ponto um homem passa de barbeado a ter barba?</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia da barba, falácia do monte, falácia do paradoxo do monte, falácia do homem careca, falácia do continuum, falácia do desenho de linhas, falácia dos sorites</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Argument-to-Moderation" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Argumento para Moderação</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Afirmando que, dadas quaisquer duas posições, existe um compromisso entre elas que deve ser correto.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">argumentum ad temperantiam, meio-termo, falso compromisso, falácia cinza, falácia da média dourada, falácia da média, divisão da diferença</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Argument-to-the-Purse" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Argumento para a bolsa</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Concluindo que o valor de verdade do argumento é verdadeiro ou falso com base na situação financeira do autor do argumento.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">argumentum ad crumenam, apelo à pobreza ou argumentum ad lazarum, apelo à riqueza, apelo ao dinheiro</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Arguments" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">argumentos</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando ouvimos a palavra “argumento”, tendemos a pensar em um confronto adversário entre duas ou mais pessoas, com brigas, defensividade e aumento das emoções negativas.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Avoiding-the-Issue" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Evitando o problema</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando um argumentador responde a um argumento não abordando os pontos do argumento. </font><font style="vertical-align: inherit;">Ao contrário da falácia do espantalho, evitar o problema não cria um argumento não relacionado para desviar a atenção, simplesmente evita o argumento.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">evitando a pergunta [forma de], perdendo o ponto, desviando-se do assunto, divagando, distração [forma de]</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Base-Rate-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia da taxa básica</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Ignorar informações estatísticas em favor de usar informações irrelevantes, que se acredita erroneamente serem relevantes, para fazer um julgamento. </font><font style="vertical-align: inherit;">Isso geralmente decorre da crença irracional de que as estatísticas não se aplicam a uma situação, por um motivo ou outro, quando, na verdade, se aplicam.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">negligenciar taxas básicas, negligenciar taxas básicas, falácia do promotor [forma de]</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Begging-the-Question" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Implorando a pergunta</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Qualquer forma de argumento em que a conclusão é assumida em uma das premissas. </font><font style="vertical-align: inherit;">Muitas pessoas usam a frase “implorando a pergunta” incorretamente quando a usam para significar “leva alguém a fazer a pergunta”. </font><font style="vertical-align: inherit;">Esse NÃO é o uso correto. </font><font style="vertical-align: inherit;">Implorar a questão é uma forma de raciocínio circular.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">petitio principii, assumindo o ponto inicial, assumindo a resposta, argumento da galinha e do ovo, circulus in probando, raciocínio circular [forma de], círculo vicioso</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Biased-Sample-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia de amostra tendenciosa</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Tirar uma conclusão sobre uma população com base em uma amostra tendenciosa ou escolhida para fazer parecer que a população em média é diferente do que realmente é.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">estatísticas enviesadas, amostra carregada, estatísticas prejudicadas, amostra prejudicada, estatísticas carregadas, indução tendenciosa, generalização tendenciosa, generalização tendenciosa, amostra não representativa, generalização não representativa</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Blind-Authority-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia da Autoridade Cega</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Afirmar que uma proposição é verdadeira apenas com base na autoridade que faz a afirmação. </font><font style="vertical-align: inherit;">Frequentemente, aqueles que seguem cegamente uma autoridade ignoram qualquer evidência contrária à alegação da autoridade, não importa quão forte seja. </font><font style="vertical-align: inherit;">A autoridade pode ser qualquer um ou qualquer coisa, incluindo pais, um treinador, um chefe, um líder militar, um documento ou um deus.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">obediência cega, apelo do "jogador de equipe", defesa de Nuremberg, autoridade divina [forma de], apelo/argumento da autoridade cega</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Broken-Window-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia da Janela Quebrada</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A ilusão de que a destruição e o dinheiro gasto na recuperação da destruição são um benefício líquido para a sociedade. </font><font style="vertical-align: inherit;">Uma aplicação mais ampla dessa falácia é a tendência geral de ignorar os custos de oportunidade, ou o que não é visto, seja no sentido financeiro ou outro.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia do vidraceiro</font></font></i></div>
            </div>
        </a>
        <noscript><a href="/qa?seopagecat=&seobatch=80"><button type="button" class="d-inline btn btn-lg btn-primary mt-2 mb-1">Next Page</button></a></noscript>
        <a href="/logicalfallacies/Bulverism" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">bulverismo</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Esta é uma combinação de raciocínio circular e a falácia genética. </font><font style="vertical-align: inherit;">É a suposição e afirmação de que um argumento é falho ou falso por causa de seus motivos suspeitos, identidade social ou outra característica associada à sua identidade.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Causal-Reductionism" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">reducionismo causal</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Assumir uma única causa ou razão quando na verdade havia várias causas ou razões. </font><font style="vertical-align: inherit;">Forma Lógica:</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">causa complexa, falácia da causa única, simplificação causal, falácia de redução</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Cherry-Picking" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apanhar cerejas</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando apenas evidências selecionadas são apresentadas para persuadir o público a aceitar uma posição, e as evidências que iriam contra a posição são retidas. </font><font style="vertical-align: inherit;">Quanto mais forte a evidência retida, mais falacioso o argumento. </font><font style="vertical-align: inherit;">Forma Lógica:</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">ignorar dados inconvenientes, evidência suprimida, falácia de evidência incompleta, argumento por observação seletiva, argumento por meia-verdade, empilhamento de cartas, falácia de exclusão, ignorando a evidência contrária, avaliação unilateral, inclinação, unilateralidade</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Circular-Definition" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Definição circular</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Uma definição circular é definir um termo usando o termo na definição. </font><font style="vertical-align: inherit;">Ironicamente, essa definição é parcialmente culpada pelo meu uso do termo “definição” na definição. </font><font style="vertical-align: inherit;">Ok, estou usando definição demais. </font><font style="vertical-align: inherit;">Droga! </font><font style="vertical-align: inherit;">Acabei de fazer de novo.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Circular-Reasoning" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Raciocínio circular</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Um tipo de raciocínio em que a proposição é sustentada pelas premissas, que é sustentada pela proposição, criando um círculo no raciocínio onde nenhuma informação útil está sendo compartilhada. </font><font style="vertical-align: inherit;">Essa falácia costuma ser bem humorada.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">circulus in demonstrando, pensamento paradoxal, argumento circular, causa e consequência circulares, raciocínio em círculo</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Commutation-of-Conditionals" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Comutação de Condicionais</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Alternando o antecedente e o consequente em um argumento lógico.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">a falácia do conseqüente, convertendo um condicional</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Complex-Question-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia de Pergunta Complexa</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Uma pergunta que tem uma pressuposição embutida, que implica algo, mas protege aquele que faz a pergunta de acusações de falsas afirmações. </font><font style="vertical-align: inherit;">É uma forma de discurso enganoso e uma falácia quando o público não detecta a suposta informação implícita na pergunta e a aceita como um fato.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">plurium interrogationum, falácia de muitas perguntas, falácia de pressuposição, pergunta carregada, pergunta capciosa, pergunta falsa</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Conflicting-Conditions" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Condições conflitantes</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando o argumento é autocontraditório e não pode ser verdadeiro.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">contradictio in adjecto, uma autocontradição, uma ideia auto-refutável</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Confusing-Currently-Unexplained-with-Unexplainable" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Confundir atualmente inexplicável com inexplicável</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Fazendo a suposição de que o que atualmente não pode ser explicado é, portanto, inexplicável (impossível de explicar). </font><font style="vertical-align: inherit;">Isso é um problema porque não podemos saber o futuro e quais condições podem surgir para oferecer uma explicação. </font><font style="vertical-align: inherit;">Também é importante notar que não podemos assumir que o atualmente inexplicado é explicável.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Confusing-an-Explanation-with-an-Excuse" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Confundir uma explicação com uma desculpa</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Tratar uma explicação de um fato como se fosse uma justificativa do fato, uma razão válida para o fato ou evidência para o fato.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <noscript><a href="/qa?seopagecat=&seobatch=90"><button type="button" class="d-inline btn btn-lg btn-primary mt-2 mb-1">Next Page</button></a></noscript>
        <a href="/logicalfallacies/Conjunction-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia da Conjunção</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A falácia da conjunção ocorre quando se estima que uma declaração conjuntiva (isto e aquilo) seja mais provável do que pelo menos uma de suas declarações componentes. </font><font style="vertical-align: inherit;">É a suposição de que condições mais específicas são mais prováveis ​​do que as gerais. </font><font style="vertical-align: inherit;">Essa falácia geralmente decorre de pensar que as escolhas são alternativas, em vez de membros do mesmo conjunto. </font><font style="vertical-align: inherit;">A falácia é ainda mais exacerbada ao preparar o público com informações que os levam a escolher o subconjunto como a opção mais provável.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">efeito de conjunção</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Conspiracy-Theory" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Teoria da conspiração</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Explicar que sua alegação não pode ser provada ou verificada porque a verdade está sendo ocultada e/ou as evidências destruídas por um grupo de duas ou mais pessoas. </font><font style="vertical-align: inherit;">Quando esse motivo é contestado por não ser verdadeiro ou preciso, o desafio é frequentemente apresentado como apenas outra tentativa de encobrir a verdade e apresentado como mais uma evidência de que a afirmação original é verdadeira.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">cancelamento de hipóteses, cancelamento de hipóteses, encobrimentos</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Contextomy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Contextomy</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Remover uma passagem de seu entorno de forma a distorcer seu significado pretendido.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia de citar fora de contexto, citar fora de contexto</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/deceptive-sharing.html" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Compartilhamento enganoso</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">compartilhar um artigo, postagem ou meme nas mídias sociais com a intenção de influenciar a percepção do público para que perceba um evento estatisticamente raro como um evento comum. </font><font style="vertical-align: inherit;">O viés cognitivo por trás dessa falácia é a heurística da disponibilidade que nos leva a ter uma percepção distorcida da realidade com base em exemplos específicos que facilmente vêm à mente.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Definist-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia Definitiva</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Definir um termo de forma a tornar a posição de alguém muito mais fácil de defender.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia de definição persuasiva, redefinição</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Denying-a-Conjunct" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Negando um Conjunto</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Uma falácia formal na qual a primeira premissa afirma que pelo menos um dos dois conjuntos (antecedente e consequente) é falso e conclui que o outro conjunto deve ser verdadeiro.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Denying-the-Antecedent" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Negando o Antecedente</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">É uma falácia na lógica formal onde em uma premissa padrão se/então, o antecedente (o que vem depois do “se”) não é verdadeiro, então conclui-se que o consequente (o que vem depois do “então”) não é verdadeiro.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">erro inverso, falácia inversa</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Denying-the-Correlative" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Negando o Correlativo</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apresentar alternativas quando, de fato, não existem. </font><font style="vertical-align: inherit;">Isso pode acontecer quando você tem duas declarações mutuamente exclusivas (conjunção correlativa) apresentadas como escolhas e, em vez de escolher uma ou outra, introduz uma terceira - geralmente como uma distração de ter que escolher entre as duas alternativas apresentadas.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">negando a conjunção correlativa</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Disjunction-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia da Disjunção</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Semelhante à falácia da conjunção, a falácia da disjunção ocorre quando se estima que uma declaração disjuntiva (isto ou aquilo) seja menos provável do que pelo menos uma de suas declarações componentes.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Distinction-Without-a-Difference" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Distinção sem diferença</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A afirmação de que uma posição é diferente de outra baseada na linguagem quando, na verdade, ambas as posições são iguais -- pelo menos na prática ou em termos práticos.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <noscript><a href="/qa?seopagecat=&seobatch=100"><button type="button" class="d-inline btn btn-lg btn-primary mt-2 mb-1">Next Page</button></a></noscript>
        <a href="/logicalfallacies/Double-Standard" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Padrão duplo</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Julgar duas situações por padrões diferentes quando, na verdade, você deveria estar usando o mesmo padrão. </font><font style="vertical-align: inherit;">Usado em argumentação para apoiar ou rejeitar injustamente um argumento.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Ecological-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia ecológica</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A interpretação de dados estatísticos onde as inferências sobre a natureza dos indivíduos são deduzidas da inferência para o grupo ao qual esses indivíduos pertencem.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia de inferência ecológica</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Equivocation" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Equívoco</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Usar um termo ambíguo em mais de um sentido, tornando o argumento enganoso.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">duplo sentido</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Etymological-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia etimológica</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A suposição de que o significado atual de uma palavra deve ser/é semelhante ao significado histórico. </font><font style="vertical-align: inherit;">Essa falácia ignora a evolução da linguagem e o cerne da lingüística. </font><font style="vertical-align: inherit;">Essa falácia geralmente é cometida quando alguém acha o significado histórico de uma palavra mais palatável ou propício ao seu argumento.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Exclusive-Premises" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Instalações Exclusivas</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Um silogismo categórico de forma padrão que tem duas premissas negativas na forma de “nenhum X é Y” ou “alguns X não são Y”.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia de premissas exclusivas</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Existential-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia existencial</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Uma falácia lógica formal, que é cometida quando um silogismo categórico emprega duas premissas universais (“todas”) para chegar a uma conclusão particular (“algumas”).</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">instanciação existencial</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Extended-Analogy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Analogia Estendida</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Sugerindo que, porque duas coisas são semelhantes de alguma forma e uma dessas coisas é como outra coisa, então ambas as coisas devem ser como essa "outra coisa".</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/fact-to-fiction_fallacy.html" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia do fato para a ficção</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Tentar apoiar uma narrativa ou argumento com fatos que não apóiam a narrativa ou o argumento. </font><font style="vertical-align: inherit;">A característica distintiva do...</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Failure-to-Elucidate" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falha em Elucidar</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando a definição é mais difícil de entender do que a palavra ou conceito que está sendo definido.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">obscurum per obscurius</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Fake-Precision" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Precisão Falsa</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Usar estatísticas implausivelmente precisas para dar a aparência de verdade e certeza, ou usar diferenças insignificantes nos dados para fazer inferências incorretas.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">precisão excessiva, precisão falsa, precisão mal colocada, precisão espúria</font></font></i></div>
            </div>
        </a>
        <noscript><a href="/qa?seopagecat=&seobatch=110"><button type="button" class="d-inline btn btn-lg btn-primary mt-2 mb-1">Next Page</button></a></noscript>
        <a href="/logicalfallacies/Fallacy-of-the-Undistributed-Middle" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia do (o) meio não distribuído</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Uma falácia formal em um silogismo categórico onde o meio termo, ou o termo que não aparece na conclusão, não é distribuído aos outros dois termos.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">meio mal distribuído, meio termo não distribuído</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Fallacy-of-Composition" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia de composição</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Inferir que algo é verdadeiro para o todo a partir do fato de que é verdadeiro para alguma parte do todo. </font><font style="vertical-align: inherit;">Isso é o oposto da falácia da divisão.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia de composição, falácia de exceção, indução defeituosa</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Fallacy-of-Division" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia da divisão</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Inferir que algo é verdadeiro para uma ou mais partes do fato de que é verdadeiro para o todo. </font><font style="vertical-align: inherit;">Isso é o oposto da falácia da composição.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falsa divisão, dedução defeituosa, falácia da divisão</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Fallacy-of-Every-and-All" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia de todos e de todos</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando um argumento contém quantificadores universais e quantificadores existenciais (todos, alguns, nenhum, todos) com significados diferentes, e a ordem dos quantificadores é invertida. </font><font style="vertical-align: inherit;">Esta é uma forma específica de equívoco.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Fallacy-of-Four-Terms" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia dos Quatro Termos</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Essa falácia ocorre em um silogismo categórico quando o silogismo tem quatro termos em vez dos três necessários (em certo sentido, não pode ser um silogismo categórico para começar!) Se assumir essa forma, é inválido. </font><font style="vertical-align: inherit;">A falácia do equívoco também pode se encaixar nessa falácia porque o mesmo termo é usado de duas maneiras diferentes, formando quatro termos distintos, embora pareçam ser apenas três.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">quaternio terminorum, termo médio ambíguo</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Fallacy-of-Opposition" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia da Oposição</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Afirmar que aqueles que discordam de você devem estar errados e não pensar direito, principalmente com base no fato de que eles são a oposição.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/False-Attribution" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Atribuição Falsa</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apelar para uma fonte irrelevante, não qualificada, não identificada, tendenciosa ou fabricada em apoio a um argumento.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/False-Conversion" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Conversão Falsa</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A falácia formal onde os termos sujeito e predicado da proposição são trocados (conversão) na conclusão, em uma proposição que usa “todos” em sua premissa (formas tipo “A”), ou “alguns/não” (tipo “ O” formas).</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">conversão ilícita, conversão indutiva [ilícita]</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/False-Dilemma" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falso dilema</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando apenas duas escolhas são apresentadas, ainda existem mais, ou existe um espectro de escolhas possíveis entre dois extremos. </font><font style="vertical-align: inherit;">Os falsos dilemas são geralmente caracterizados por uma linguagem “ou isto ou aquilo”, mas também podem ser caracterizados por omissões de escolhas. </font><font style="vertical-align: inherit;">Outra variedade é o falso trilema, que é quando três opções são apresentadas quando existem mais.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia do tudo ou nada, falsa dicotomia [forma de], falácia ou ou, raciocínio ou-ou, falácia de falsa escolha, falácia de falsas alternativas, pensamento em preto e branco, falácia de hipóteses exaustivas, bifurcação, meio excluído, sem meio termo, polarização</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/False-Effect" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Efeito falso</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Afirmar que a causa é verdadeira ou falsa com base no que sabemos sobre o efeito em uma alegação de causalidade que não foi devidamente estabelecida. </font><font style="vertical-align: inherit;">A causa geralmente é uma afirmação implícita, e é essa afirmação que está sendo considerada verdadeira ou falsa, certa ou errada.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <noscript><a href="/qa?seopagecat=&seobatch=120"><button type="button" class="d-inline btn btn-lg btn-primary mt-2 mb-1">Next Page</button></a></noscript>
        <a href="/logicalfallacies/False-Equivalence" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falsa equivalência</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Um argumento ou afirmação em que dois argumentos completamente opostos parecem ser logicamente equivalentes quando na verdade não são.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Fantasy-Projection" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Projeção Fantasia</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Confundir experiências subjetivas, geralmente muito carregadas emocionalmente, com a realidade objetiva, sugerindo ou exigindo que os outros aceitem a experiência subjetiva como realidade objetiva.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Far-Fetched-Hypothesis" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Hipótese Rebuscada</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Oferecer uma hipótese bizarra (rebuscada) como a explicação correta sem primeiro descartar explicações mais mundanas.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Faulty-Comparison" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Comparação Defeituosa</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Comparar uma coisa com outra que realmente não está relacionada, a fim de fazer uma coisa parecer mais ou menos desejável do que realmente é.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">comparação ruim, comparação falsa, comparação inconsistente [forma de]</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Gadarene-Swine-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia do Suíno Gadareno</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A suposição de que, porque um indivíduo não está em formação com o grupo, esse indivíduo deve ser o único fora do curso. </font><font style="vertical-align: inherit;">É possível que aquele que aparece fora do rumo seja o único no rumo certo.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Galileo-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia de Galileu</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A alegação de que, como uma ideia é proibida, processada, detestada ou ridicularizada, ela deve ser verdadeira ou deve receber mais credibilidade. </font><font style="vertical-align: inherit;">Isso se origina da famosa perseguição de Galileu Galilei pela Igreja Católica Romana por sua defesa do heliocentrismo quando a crença comumente aceita na época era um universo centrado na Terra.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Argumento de Galileu, defesa de Galileu, gambito de Galileu, aspirante a Galileu</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Gamblers-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia do jogador</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Raciocinando que, em uma situação que é puro acaso, o resultado pode ser afetado por resultados anteriores.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">a falácia de Monte Carlo, a doutrina da maturidade das chances</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Genetic-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia genética</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Basear a afirmação de verdade de um argumento na origem de suas afirmações ou premissas.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia das origens, falácia da virtude</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/gish-gallop.html" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Gish Galope</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Sobrecarregar um interlocutor com tantos argumentos quanto possível, sem levar em conta a precisão ou a força dos argumentos. </font><font style="vertical-align: inherit;">Isso é especialmente insincero quando o interlocutor não tem permissão para interromper e abordar os argumentos...</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Hasty-Generalization" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Generalização Apressada</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Tirar uma conclusão com base em um pequeno tamanho de amostra, em vez de olhar para estatísticas que estão muito mais alinhadas com a situação típica ou média.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">argumento de pequenos números, estatísticas de pequenos números, estatísticas insuficientes, argumento por generalização, generalização falha, indução precipitada, generalização indutiva, amostra insuficiente, falácia de fato solitário, generalidade excessiva, generalização excessiva, amostra não representativa</font></font></i></div>
            </div>
        </a>
        <noscript><a href="/qa?seopagecat=&seobatch=130"><button type="button" class="d-inline btn btn-lg btn-primary mt-2 mb-1">Next Page</button></a></noscript>
        <a href="/logicalfallacies/Having-Your-Cake" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary">Having Your Cake</h5>
            <p class="mb-2">Making an argument, or responding to one, in such a way that it does not make it at all clear what your position is.  This puts you in a position to back out of your claim at any time and go in a new direction without penalty, claiming that you were “right” all along. </p>
            <div class="mt-2">
            <div class="small text-muted"><i>failure to assert, diminished claim, failure to choose sides</i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Hedging" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary">Hedging</h5>
            <p class="mb-2">Refining your claim simply to avoid counter evidence and then acting as if your revised claim is the same as the original.</p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Historians-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary">Historian’s Fallacy</h5>
            <p class="mb-2">Judging a person's decision in the light of new information not available at the time.</p>
            <div class="mt-2">
            <div class="small text-muted"><i>retrospective determinism, hindsight</i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Homunculus-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary">Homunculus Fallacy</h5>
            <p class="mb-2">An argument that accounts for a phenomenon in terms of the very phenomenon that it is supposed to explain, which results in an infinite regress.</p>
            <div class="mt-2">
            <div class="small text-muted"><i>homunculus argument, infinite regress</i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Hot-Hand-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary">Hot Hand Fallacy</h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A falácia da mão quente é a crença irracional de que, se você ganhar ou perder vários jogos consecutivos, você é “quente” ou “frio”, respectivamente, o que significa que a seqüência provavelmente continuará e tem a ver com algo diferente de probabilidade pura.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">fenômeno da mão quente</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Hypnotic-Bait-and-Switch" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Isca hipnótica e troca</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Declarar várias declarações verdadeiras incontroversas em sucessão, seguidas por uma afirmação que o argumentador deseja que o público aceite como verdadeira. </font><font style="vertical-align: inherit;">Esta é uma técnica de propaganda, mas também uma falácia quando o público dá mais credibilidade à última afirmação porque foi precedida de declarações verdadeiras. </font><font style="vertical-align: inherit;">O negativo também pode ser usado da mesma maneira.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Hypothesis-Contrary-to-Fact" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Hipótese Contrária ao Fato</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Oferecer uma afirmação mal fundamentada sobre o que poderia ter acontecido no passado ou no futuro, se (a parte hipotética) as circunstâncias ou condições fossem diferentes. </font><font style="vertical-align: inherit;">A falácia também envolve tratar situações hipotéticas futuras como se fossem fatos.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia contrafactual, falácia especulativa, falácia "e se", wouldchuck</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Identity-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia de identidade</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando o argumento de alguém é avaliado com base em sua identidade física ou social, ou seja, classe social, geração, etnia, gênero ou orientação sexual, profissão, ocupação ou subgrupo quando a força do argumento independe da identidade.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">política de identidade</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/If-By-Whiskey" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">If-By-Whisky</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Uma resposta a uma pergunta que depende das opiniões do questionador e faz uso de palavras com fortes conotações. </font><font style="vertical-align: inherit;">Essa falácia parece apoiar os dois lados de uma questão - uma tática comum na política.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Illicit-Contraposition" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Contraposição Ilícita</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Uma falácia formal em que trocar os termos de assunto e predicado de uma proposição categórica e, em seguida, negar cada um, resulta em uma forma de argumento inválida. </font><font style="vertical-align: inherit;">Os exemplos abaixo deixam isso mais claro. </font><font style="vertical-align: inherit;">Esta é uma falácia apenas para formulários do tipo “E” e tipo “I”, ou formulários que usam as palavras “não” e “alguns”, respectivamente.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <noscript><a href="/qa?seopagecat=&seobatch=140"><button type="button" class="d-inline btn btn-lg btn-primary mt-2 mb-1">Next Page</button></a></noscript>
        <a href="/logicalfallacies/Illicit-Major" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Major ilícito</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Qualquer forma de silogismo categórico em que o termo maior é distribuído na conclusão, mas não na premissa maior.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">processo ilícito do termo maior</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Illicit-Minor" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">menor ilícito</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Qualquer forma de silogismo categórico em que o termo menor é distribuído na conclusão, mas não na premissa menor.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">processo ilícito de menor prazo</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Illicit-Substitution-of-Identicals" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Substituição Ilícita de Idênticos</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Uma falácia formal devido a confundir o conhecimento de uma coisa (extensão) com o conhecimento dela sob todos os seus vários nomes ou descrições (intensão).</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia do homem encapuzado, falácia do homem mascarado, falácia intensional</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/imposter-fallacy.html" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia do impostor</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando alguém sugere ou afirma, com evidências insuficientes, que os outliers do grupo que são vistos como prejudiciais ao grupo são compostos principalmente por infiltrados de outro grupo com o objetivo de fazer com que o grupo infiltrado pareça ruim.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Incomplete-Comparison" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Comparação incompleta</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Uma afirmação incompleta que não pode ser refutada. </font><font style="vertical-align: inherit;">Isso é popular na publicidade.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Inconsistency" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Inconsistência</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Em termos de um argumento falacioso, duas ou mais proposições são afirmadas que não podem ser ambas verdadeiras. </font><font style="vertical-align: inherit;">Em um sentido mais geral, manter duas ou mais visões/crenças que não podem ser todas verdadeiras juntas. </font><font style="vertical-align: inherit;">Citações de Yogi Berra (mesmo que apócrifas) são ótimos exemplos de falácias, especialmente inconsistências.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">contradição interna, inconsistência lógica</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Inflation-of-Conflict" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Inflação de Conflito</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Raciocinando que, como as autoridades não podem concordar com precisão sobre um assunto, nenhuma conclusão pode ser alcançada e, como resultado, minimizando a credibilidade das autoridades. </font><font style="vertical-align: inherit;">Esta é uma forma de pensamento em preto e branco - ou sabemos a verdade exata ou não sabemos nada.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Insignificant-Cause" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Causa insignificante</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Uma explicação que coloca um fator menor, entre vários que contribuíram, como sua única causa. </font><font style="vertical-align: inherit;">Essa falácia também ocorre quando uma explicação é solicitada, e a que é dada não é suficiente para explicar inteiramente o incidente, mas é passada como se fosse suficiente.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia da causa insignificante, genuína, mas insignificante, causa insuficiente</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Jumping-to-Conclusions" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Tirando conclusões precipitadas</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Tirar uma conclusão sem levar o tempo necessário para avaliar as evidências ou raciocinar por meio do argumento.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">conclusão precipitada, decisão precipitada, conclusões precipitadas, especificidade</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Just-Because-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Só Porque Falácia</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Recusar-se a responder para fornecer razões ou evidências para uma reclamação, declarando-se a autoridade máxima sobre o assunto. </font><font style="vertical-align: inherit;">Isso geralmente é indicado pelas frases “apenas confie em mim”, “porque eu disse”, “você verá” ou “só porque”. </font><font style="vertical-align: inherit;">A falácia do justo porque não conduz ao objetivo da argumentação – isto é, chegar a uma solução mutuamente aceitável. </font><font style="vertical-align: inherit;">Também não é útil para ajudar a outra pessoa a entender por que você está firme em sua posição. </font><font style="vertical-align: inherit;">“Apenas porque” não é uma razão que diz respeito à questão em si; </font><font style="vertical-align: inherit;">é simplesmente um desvio à autoridade (legítima ou não).</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">confie em mim, mãe sabe melhor falácia, porque eu disse, você vai ver</font></font></i></div>
            </div>
        </a>
        <noscript><a href="/qa?seopagecat=&seobatch=150"><button type="button" class="d-inline btn btn-lg btn-primary mt-2 mb-1">Next Page</button></a></noscript>
        <a href="/logicalfallacies/Just-In-Case-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia Just In Case</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Argumentar com base no pior cenário em vez do cenário mais provável, permitindo que o medo prevaleça sobre a razão.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia do pior cenário</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Kettle-Logic" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Lógica da Chaleira</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Fazer (geralmente) argumentos múltiplos e contraditórios, na tentativa de apoiar um único ponto ou ideia.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Least-Plausible-Hypothesis" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Hipótese menos plausível</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Escolher explicações mais irracionais para fenômenos em vez de explicações mais defensáveis. </font><font style="vertical-align: inherit;">Ao julgar a validade das hipóteses ou conclusões a partir da observação, o método científico se baseia no Princípio da Parcimônia, também conhecido como Navalha de Occam, que afirma, todas as coisas sendo iguais, a explicação mais simples de um fenômeno que requer menos suposições é a explicação preferida até que possa ser refutado.  </font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Limited-Depth" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Profundidade Limitada</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Deixar de apelar para uma causa subjacente e, em vez disso, simplesmente apelar para a adesão a uma categoria. </font><font style="vertical-align: inherit;">Em outras palavras, simplesmente afirmando o que você está tentando explicar sem realmente explicar nada.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Limited-Scope" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Escopo limitado</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A teoria não explica nada além do fenômeno que ela explica (aquela coisa) e, na melhor das hipóteses, é provável que seja incompleta. </font><font style="vertical-align: inherit;">Isso geralmente é feito apenas redefinindo um termo ou frase, em vez de explicá-lo.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Logic-Chopping" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Corte Lógico</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Usar as ferramentas técnicas da lógica de maneira inútil e pedante, concentrando-se em detalhes triviais, em vez de abordar diretamente a questão principal em disputa. </font><font style="vertical-align: inherit;">Irrelevante sobre a precisão.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">sofismas, picuinhas, cortina de fumaça, disputas, objeções triviais</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Ludic-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia Lúdica</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Assumir que modelos estatísticos perfeitos se aplicam a situações onde eles realmente não se aplicam. </font><font style="vertical-align: inherit;">Isso pode resultar em excesso de confiança na teoria da probabilidade ou simplesmente em não saber exatamente onde ela se aplica, em oposição a situações caóticas ou situações com influências externas muito sutis ou numerosas para prever.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">ludus</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Lying-with-Statistics" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Mentir com estatísticas</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Isso pode ser visto como toda uma classe de falácias que resultam na apresentação de dados estatísticos de maneira muito tendenciosa e, é claro, na interpretação das estatísticas sem questionar os métodos por trás da coleta e apresentação dos dados.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácias/falácias estatísticas, mal-entendido sobre a natureza das estatísticas [forma de], falácia de ajuste de curva, falácia de superajuste</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Magical-Thinking" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">pensamento mágico</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Fazer conexões causais ou correlações entre dois eventos não com base na lógica ou evidência, mas principalmente com base na superstição. </font><font style="vertical-align: inherit;">O pensamento mágico geralmente faz com que a pessoa experimente um medo irracional de realizar certos atos ou ter certos pensamentos porque eles assumem uma correlação com seus atos e calamidades ameaçadoras.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">pensamento supersticioso</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/mcnamara_fallacy.html" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia de McNamara</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando uma decisão é baseada apenas em observações quantitativas (ou seja, métricas, dados concretos, estatísticas) e todos os fatores qualitativos são ignorados.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia quantitativa, falácia Skittles</font></font></i></div>
            </div>
        </a>
        <noscript><a href="/qa?seopagecat=&seobatch=160"><button type="button" class="d-inline btn btn-lg btn-primary mt-2 mb-1">Next Page</button></a></noscript>
        <a href="/logicalfallacies/Meaningless-Question" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Pergunta sem sentido</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Fazer uma pergunta que não pode ser respondida com qualquer tipo de significado racional. </font><font style="vertical-align: inherit;">Este é o equivalente textual da divisão por zero.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Methodology" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Metodologia</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Conforme discutido no prefácio, as principais falácias detalhadas neste livro datam de milhares de anos antes de Aristóteles. </font><font style="vertical-align: inherit;">Recursos acadêmicos foram usados ​​quando possível ao compilar esta lista de falácias.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Misleading-Vividness" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Vividez enganosa</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Considera-se que um pequeno número de eventos dramáticos e vívidos supera uma quantidade significativa de evidências estatísticas.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Missing-Data-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia de dados ausentes</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Recusando-se a admitir a ignorância da hipótese e/ou da conclusão, mas insistindo que sua ignorância tem a ver com a falta de dados que validam tanto a hipótese quanto a conclusão.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia de falta de informação</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Modal-Scope-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia Modal (Escopo)</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A lógica modal estuda as maneiras pelas quais as proposições podem ser verdadeiras ou falsas, sendo as mais comuns a necessidade e a possibilidade. </font><font style="vertical-align: inherit;">Algumas proposições são necessariamente verdadeiras/falsas, e outras são possivelmente verdadeiras/falsas. </font><font style="vertical-align: inherit;">Em suma, uma falácia modal envolve invalidar um argumento formal ao confundir o escopo do que é realmente necessário ou possível.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia da lógica modal, miscondicionalization, falácia da necessidade</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Moralistic-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia moralista</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando a conclusão expressa o que é, baseado apenas no que se acredita que deveria ser, ou o que não é, baseado no que se acredita que não deveria ser.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia moral</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Moving-the-Goalposts" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Movendo as traves</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Exigir de um oponente que ele aborde mais e mais pontos após o contra-argumento inicial ter sido satisfeito, recusando-se a conceder ou aceitar o argumento do oponente.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">jogo de gravidade, elevando a fasquia, argumento exigindo perfeição impossível [forma de]</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Multiple-Comparisons-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia de Comparações Múltiplas</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Afirmar que tendências inesperadas que ocorrem apenas por acaso em um conjunto de dados com um grande número de variáveis ​​são significativas.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">comparações múltiplas, multiplicidade, problema de teste múltiplo, efeito de procurar em outro lugar</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Naturalistic-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia naturalista</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando a conclusão expressa o que deveria ser, baseado apenas no que é, ou o que não deveria ser, baseado no que não é.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia é-deve, argumentando de é para deveria, falácia é-deveria</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Negating-Antecedent-and-Consequent" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Negação de Antecedente e Consequente</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Uma falácia formal em que, na forma transposicional válida de um argumento, falhamos em trocar o antecedente e o consequente.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">transposição imprópria</font></font></i></div>
            </div>
        </a>
        <noscript><a href="/qa?seopagecat=&seobatch=170"><button type="button" class="d-inline btn btn-lg btn-primary mt-2 mb-1">Next Page</button></a></noscript>
        <a href="/logicalfallacies/Negative-Conclusion-from-Affirmative-Premises" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Conclusão Negativa de Premissas Afirmativas</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A conclusão de um silogismo categórico de forma padrão é negativa, mas ambas as premissas são positivas. </font><font style="vertical-align: inherit;">Quaisquer formas válidas de silogismos categóricos que afirmam uma conclusão negativa devem ter pelo menos uma premissa negativa.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">afirmativa ilícita</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Nirvana-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia do Nirvana</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Comparar uma solução realista com uma idealizada, e descontar ou mesmo descartar a solução realista como resultado da comparação com um “mundo perfeito” ou padrão impossível. </font><font style="vertical-align: inherit;">Ignorar o fato de que as melhorias geralmente são boas o suficiente.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia da solução perfeita, falácia perfeccionista</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/No-True-Scotsman" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Nenhum verdadeiro escocês</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando uma afirmação universal (“todos”, “todos”, etc.) especificidade.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">apelo à pureza [forma de], nenhum cristão verdadeiro, nenhuma falácia de cruzamento verdadeiro [forma de]</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Non-Sequitur" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Non Sequitur</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando a conclusão não decorre das premissas. </font><font style="vertical-align: inherit;">No raciocínio mais informal, pode ser quando o que é apresentado como evidência ou razão é irrelevante ou acrescenta muito pouco suporte à conclusão.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">descarrilamento, “que não segue”, razão irrelevante, inferência inválida, não suporte, argumento por cenário [forma de], premissa falsa [forma de], premissa questionável [forma de], non-sequitur</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Notable-Effort" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Esforço Notável</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Aceitar um bom esforço como uma razão válida para aceitar a verdade da conclusão, mesmo que o esforço não esteja relacionado à verdade.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">“E” é para esforço</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/nutpicking-fallacy.html" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia do Pecador de Nozes</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando alguém apresenta um membro atípico ou fraco de um grupo como se fosse um representante típico ou forte.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Overextended-Outrage" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Indignação Exagerada</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Essa é uma forma de pensamento estatístico ruim, em que um ou mais casos estatisticamente raros são considerados a norma ou a tendência (sem evidências) com o objetivo de expressar ou incitar indignação a um grupo inteiro. </font><font style="vertical-align: inherit;">É uma forma de estereótipo extremo.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">indignação moral exagerada, indignação política exagerada</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Oversimplified-Cause-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia de Causa Simplificada</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando um fator contribuinte é considerado a causa, ou quando um conjunto complexo de fatores causais é reduzido a uma única causa. </font><font style="vertical-align: inherit;">É uma forma de pensamento simplista que implica que algo é uma causa ou não é. </font><font style="vertical-align: inherit;">Ele ignora o fato importante de que, especialmente quando se refere ao comportamento humano, as causas são muito complexas e multidimensionais.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Overwhelming-Exception" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Exceção Esmagadora</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Uma generalização que é tecnicamente precisa, mas tem uma ou mais qualificações que eliminam tantos casos que o argumento resultante é significativamente mais fraco do que o argumentador sugere. </font><font style="vertical-align: inherit;">Em muitos casos, as exceções listadas são dadas no lugar de evidência ou suporte para a alegação, não como evidência ou suporte para a alegação.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Package-Deal-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia da Oferta de Pacote</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Assumir que coisas que são frequentemente agrupadas devem sempre ser agrupadas, ou a suposição de que o desagrupamento terá efeitos significativamente mais graves do que o previsto.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falsa conjunção</font></font></i></div>
            </div>
        </a>
        <noscript><a href="/qa?seopagecat=&seobatch=180"><button type="button" class="d-inline btn btn-lg btn-primary mt-2 mb-1">Next Page</button></a></noscript>
        <a href="/logicalfallacies/Poisoning-the-Well" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">envenenando o poço</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Cometer um ataque preemptivo ad hominem contra um oponente. </font><font style="vertical-align: inherit;">Isto é, preparar o público com informações adversas sobre o oponente desde o início, na tentativa de tornar sua afirmação mais aceitável ou diminuir a credibilidade da afirmação de seu oponente.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">desacreditar, difamar táticas, apelar para o ethos [forma de]</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Political-Correctness-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia do politicamente correto</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Isso é comum na história recente. </font><font style="vertical-align: inherit;">É a suposição ou admissão de que dois ou mais grupos, indivíduos ou ideias de grupos ou indivíduos são iguais, de igual valor, ou ambos verdadeiros, com base no recente fenômeno do politicamente correto, que é definido como, um termo que denota linguagem, ideias, políticas e comportamento vistos como buscando minimizar a ofensa social e institucional em contextos ocupacionais, de gênero, raciais, culturais, sexuais, certas outras religiões, crenças ou ideologias, deficiência e contextos relacionados à idade e, conforme pretendido por prazo, fazendo-o de forma excessiva.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">PC falácia</font></font></i></div>
            </div>
        </a>
        <a href="/post-hoc.html" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Post hoc</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Alegando que, como o evento Y seguiu o evento X, o evento Y deve ter sido causado pelo evento X, sem estabelecer a causalidade adequadamente.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">post hoc ergo propter hoc, depois disso portanto por causa disso, racionalização post hoc</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Post-Designation" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Pós-designação</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Tirar uma conclusão das correlações observadas em uma dada amostra, mas somente após a amostra já ter sido extraída e sem declarar antecipadamente quais correlações o experimentador esperava encontrar. </font><font style="vertical-align: inherit;">Isso está relacionado à falácia das comparações múltiplas.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">pescando dados</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/pragmatic-fallacy.html" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia pragmática</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Afirmar que algo é verdadeiro porque a pessoa que faz a afirmação experimentou, ou está se referindo a alguém que experimentou, algum benefício prático de acreditar que a coisa é verdadeira.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">apelo à praticidade</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Prejudicial-Language" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Linguagem Prejudicial</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Termos carregados ou emotivos usados ​​para atribuir valor ou bondade moral à crença na proposição.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">variante de imagem</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Proof-Surrogate" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Substituto de Prova</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Uma alegação disfarçada de prova ou evidência, quando nenhuma prova ou evidência está realmente sendo oferecida.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Proof-by-Intimidation" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Prova por Intimidação</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Fazer um argumento propositalmente difícil de entender na tentativa de intimidar seu público a aceitá-lo, ou aceitar um argumento sem evidências ou ser intimidado para questionar a autoridade ou suposições a priori de quem está argumentando.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">argumentum verbosium, prova por verbosidade, falácia de intimidação</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Proving-Non-Existence" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Comprovando a Inexistência</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Exigir que alguém prove a inexistência de algo no lugar para fornecer evidências adequadas para a existência desse algo. </font><font style="vertical-align: inherit;">Embora seja possível provar a inexistência em situações especiais, como mostrar que um recipiente não contém determinados itens, não se pode provar a inexistência universal ou absoluta.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Pseudo-Logical-Fallacies" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácias pseudo-lógicas</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Existem muitas falácias lógicas que podem ser encontradas na Internet que não atendem a um ou mais desses critérios, mas as pessoas ainda se referem a elas como falácias lógicas. </font><font style="vertical-align: inherit;">Como não há critérios objetivos para a maioria das falácias lógicas, as pessoas podem chamar qualquer coisa de falácia lógica, se quiserem.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <noscript><a href="/qa?seopagecat=&seobatch=190"><button type="button" class="d-inline btn btn-lg btn-primary mt-2 mb-1">Next Page</button></a></noscript>
        <a href="/logicalfallacies/Psychogenetic-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia psicogenética</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Inferir alguma razão psicológica pela qual um argumento é feito e, como resultado, assumir que é inválido.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Quantifier-Shift-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia da Mudança do Quantificador</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Uma falácia de inverter a ordem de dois quantificadores.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">mudança de quantificador ilícito</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Quantum-Physics-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia da Física Quântica</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Usando a física quântica na tentativa de apoiar sua afirmação, quando de forma alguma sua afirmação está relacionada à física quântica. </font><font style="vertical-align: inherit;">Pode-se também usar a estranheza dos princípios da física quântica para lançar dúvidas sobre as leis bem estabelecidas do mundo macro.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Questionable-Cause" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Causa questionável</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Concluindo que uma coisa causou outra, simplesmente porque estão regularmente associadas.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">cum hoc ergo propter hoc, lógica da borboleta, ignorar uma causa comum, negligenciar uma causa comum, confundir correlação e causalidade, confundir causa e efeito, causa falsa, terceira causa, terceira causa falácia, justaposição [forma de], inverter causalidade/errado direção [forma de]</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Rationalization" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Racionalização</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Oferecer desculpas falsas ou inautênticas para nossa reivindicação, porque sabemos que as verdadeiras razões são muito menos persuasivas ou mais embaraçosas de compartilhar, ou mais duras do que as fabricadas.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">dando desculpas</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Reasoning" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Raciocínio</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Os seres humanos têm a capacidade de estabelecer e verificar fatos, mudar e justificar crenças e, em geral, dar sentido às coisas. </font><font style="vertical-align: inherit;">Fazemos isso pela razão, e o processo de fazê-lo é chamado de raciocínio.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Red-Herring" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">arenque vermelho</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Tentar redirecionar o argumento para outro assunto ao qual a pessoa que está fazendo o redirecionamento pode responder melhor. </font><font style="vertical-align: inherit;">Embora seja semelhante à falácia de evitar a questão, o arenque vermelho é um desvio deliberado da atenção com a intenção de tentar abandonar o argumento original.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Ignoratio elenchi, irrelevante, desorientação [forma de], mudança de assunto, ênfase falsa, defesa de Chewbacca, conclusão irrelevante, tese irrelevante, obscurecendo a questão, ignorância da refutação</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Reductio-ad-Absurdum" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Reductio ad Absurdum</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Um modo de argumentação ou uma forma de argumento em que uma proposição é refutada seguindo suas implicações logicamente para uma conclusão absurda. </font><font style="vertical-align: inherit;">Argumentos que usam universais como “sempre”, “nunca”, “todos”, “ninguém”, etc., tendem a ser reduzidos a conclusões absurdas. </font><font style="vertical-align: inherit;">A falácia está no argumento que pode ser reduzido ao absurdo - então, em essência, reductio ad absurdum é uma técnica para expor a falácia.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">reduzir ao absurdo</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Reductio-ad-Hitlerum" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Reductio ad Hitlerum</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A tentativa de fazer um argumento análogo a Hitler ou ao partido nazista. </font><font style="vertical-align: inherit;">Hitler é provavelmente a figura mais universalmente desprezada da história, então qualquer conexão com Hitler, ou suas crenças, pode (erroneamente) fazer com que outros vejam o argumento sob uma luz semelhante. </font><font style="vertical-align: inherit;">No entanto, essa falácia está se tornando mais conhecida, assim como o fato de que, na maioria das vezes, é uma tentativa desesperada de invalidar a alegação de verdade do argumento por falta de um bom contra-argumento.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">argumentum ad Hitlerum, jogando a carta nazista, carta de Hitler</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Regression-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia de regressão</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Atribuir uma causa onde não existe nenhuma em situações onde existam flutuações naturais, deixando de levar em conta essas flutuações naturais.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia regressiva</font></font></i></div>
            </div>
        </a>
        <noscript><a href="/qa?seopagecat=&seobatch=200"><button type="button" class="d-inline btn btn-lg btn-primary mt-2 mb-1">Next Page</button></a></noscript>
        <a href="/logicalfallacies/Reification" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Reificação</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando uma abstração (crença abstrata ou construto hipotético) é tratada como se fosse um evento concreto, real ou entidade física -- quando uma ideia é tratada como se tivesse uma existência real.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">abstração, concretismo, falácia da concretude deslocada, hipostasia, falácia patética [forma de]</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Relative-Privation" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Privação Relativa</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Tentar fazer um cenário parecer melhor ou pior, comparando-o com o melhor ou o pior cenário.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">poderia ser pior, poderia ser melhor</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Retrogressive-Causation" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Causalidade Retrógrada</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Invocar a causa para eliminar o efeito ou invocar a fonte para aliviar o efeito da fonte.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Righteousness-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia da Retidão</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Supondo que só porque as intenções de uma pessoa são boas, ela tem a verdade ou os fatos do seu lado. </font><font style="vertical-align: inherit;">Veja também a falácia da justiça própria.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Rights-To-Ought-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia do direito ao dever</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando alguém confunde uma razão para os seus direitos (constitucionais ou outros) com o que se deve fazer. </font><font style="vertical-align: inherit;">Isso é comum entre ferrenhos defensores dos "direitos"...</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia dos direitos constitucionais</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Scapegoating" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">bode expiatório</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Culpar injustamente uma pessoa impopular ou grupo de pessoas por um problema ou uma pessoa ou grupo que é um alvo fácil para tal culpa.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Selective-Attention" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Atenção seletiva</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Concentrar sua atenção em certos aspectos do argumento enquanto ignora completamente ou omite outras partes. </font><font style="vertical-align: inherit;">Isso geralmente resulta em refutações irrelevantes, falácias do espantalho e argumentos desnecessariamente prolongados.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Self-Righteousness-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia da Autojustiça</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Assumindo que só porque suas intenções são boas, você tem a verdade ou os fatos do seu lado. </font><font style="vertical-align: inherit;">Veja também a falácia da justiça.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Self-Sealing-Argument" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Argumento de autovedação</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Um argumento ou posição é auto-selante se e somente se nenhuma evidência pode ser apresentada contra ele, não importa o quê.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">argumento vazio</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Shifting-of-the-Burden-of-Proof" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Deslocamento do ônus da prova</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Fazer uma afirmação que precisa de justificativa e, em seguida, exigir que o oponente justifique o contrário da afirmação. </font><font style="vertical-align: inherit;">O ônus da prova é um conceito jurídico e filosófico com diferenças em cada domínio.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">onus probandi, ônus da prova [conceito geral], falácia do ônus da prova, ônus da prova deslocado, inversão do ônus da prova</font></font></i></div>
            </div>
        </a>
        <noscript><a href="/qa?seopagecat=&seobatch=210"><button type="button" class="d-inline btn btn-lg btn-primary mt-2 mb-1">Next Page</button></a></noscript>
        <a href="/logicalfallacies/Shoehorning" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">calçadeira</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">O processo de encaixar à força algum assunto atual na agenda pessoal, política ou religiosa de alguém. </font><font style="vertical-align: inherit;">Muitas pessoas não estão cientes de como é fácil fazer com que algo pareça uma confirmação de uma afirmação após o fato, especialmente se a fonte da confirmação for algo em que já acreditam, como profecias bíblicas, previsões psíquicas, horóscopos astrológicos, fortuna biscoitos e muito mais.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Slippery-Slope" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">ladeira escorregadia</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando um primeiro evento relativamente insignificante é sugerido para levar a um evento mais significativo, que por sua vez leva a um evento mais significativo, e assim por diante, até que algum evento significativo final seja alcançado, onde a conexão de cada evento não é apenas injustificada, mas a cada passo torna-se cada vez mais improvável. </font><font style="vertical-align: inherit;">Muitos eventos geralmente estão presentes nessa falácia, mas apenas dois são realmente necessários - geralmente conectados por "a próxima coisa que você sabe ..."</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Special-Pleading" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Petição Especial</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Aplicar padrões, princípios e/ou regras a outras pessoas ou circunstâncias, isentando a si mesmo ou a certas circunstâncias dos mesmos critérios críticos, sem fornecer justificativa adequada. </font><font style="vertical-align: inherit;">A súplica especial geralmente é resultado de fortes crenças emocionais que interferem na razão.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Spin-Doctoring" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Spin Doctoring</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Apresentar informações de maneira enganosa que resulta em outros interpretando as informações de uma forma que não reflete a realidade, mas é como você deseja que as informações sejam interpretadas.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">fiação</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Spiritual-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia espiritual</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Insistir que algo que deveria ser literal é na verdade “espiritual” como uma explicação ou justificativa para algo que de outra forma não caberia em uma explicação.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">desculpa espiritual</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Spotlight-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia dos holofotes</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Assumir que a cobertura da mídia de uma determinada classe ou categoria é representativa da classe ou categoria como um todo.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Statement-of-Conversion" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Declaração de conversão</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Aceitar a veracidade de uma afirmação com base em uma história de conversão sem considerar nenhuma evidência da veracidade da afirmação.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Stereotyping-the-fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Estereótipos (a falácia)</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">As crenças gerais que usamos para categorizar pessoas, objetos e eventos enquanto assumimos que essas crenças são generalizações precisas de todo o grupo.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Stolen-Concept-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia do conceito roubado</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Exigir a verdade de algo que você está simultaneamente tentando refutar.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Strawman-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia do palhaço</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Substituir a posição ou argumento real de uma pessoa por uma versão distorcida, exagerada ou deturpada da posição do argumento.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <noscript><a href="/qa?seopagecat=&seobatch=220"><button type="button" class="d-inline btn btn-lg btn-primary mt-2 mb-1">Next Page</button></a></noscript>
        <a href="/logicalfallacies/Style-Over-Substance" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Estilo sobre Substância</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando o argumentador embeleza o argumento com linguagem ou retórica convincente e/ou estética visual.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">argumento por slogan [forma de], pensamento clichê - ou clichê de terminação de pensamento, argumento por rima [forma de], argumento por linguagem poética [forma de]</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Subjectivist-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia subjetivista</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Afirmar que algo é verdadeiro para uma pessoa, mas não para outra, quando, de fato, é verdadeiro para todos (objetivo), conforme demonstrado por evidências empíricas.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia relativista</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Subverted-Support" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Suporte subvertido</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A tentativa de explicar algum fenômeno que não ocorre de fato ou não há evidências de que ocorra. </font><font style="vertical-align: inherit;">É uma forma de petição de princípio.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Sunk-Cost-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia do custo irrecuperável</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Raciocinar que investimentos adicionais são justificados pelo fato de que os recursos já investidos serão perdidos de outra forma, não levando em consideração as perdas globais envolvidas no investimento adicional.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">argumento da inércia, falácia do acordo, falácia do fim do trabalho</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Suppressed-Correlative" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Correlativo suprimido</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A tentativa de redefinir um correlativo (uma das duas opções mutuamente exclusivas) de modo que uma alternativa englobe a outra, ou seja, tornando uma alternativa impossível. </font><font style="vertical-align: inherit;">A redefinição, portanto, torna a palavra que está redefinindo essencialmente sem sentido.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia do contraste perdido, falácia do relativo suprimido</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Survivorship-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">falácia da sobrevivência</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Melhor resumido como "homens mortos não contam histórias". </font><font style="vertical-align: inherit;">Em sua forma geral, a falácia da sobrevivência baseia uma conclusão em um número limitado de testemunhos de "vencedores" devido ao fato de não podermos ou não ouvirmos os testemunhos dos perdedores. </font><font style="vertical-align: inherit;">Isso se baseia no viés cognitivo chamado viés de sobrevivência.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Viés de sobrevivência</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Texas-Sharpshooter-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia do Atirador de Elite do Texas</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Ignorar a diferença enquanto se concentra nas semelhanças, chegando assim a uma conclusão imprecisa. </font><font style="vertical-align: inherit;">Semelhante à falácia do jogador, este é um exemplo de inserção de significado na aleatoriedade. </font><font style="vertical-align: inherit;">Isso também é semelhante à falácia pós-designação.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">ilusão de agrupamento</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Tokenism" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">tokenismo</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Interpretar um gesto simbólico como um substituto adequado para a coisa real.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Traitorous-Critic-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia crítica traidora</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Responder às críticas atacando a percepção de favorabilidade de uma pessoa a um grupo externo ou antipatia ao grupo interno como a razão subjacente para a crítica, em vez de abordar a crítica em si e sugerir que ela fique longe do problema e/ou deixe o assunto -grupo.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">ergo decedo</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Two-Wrongs-Make-a-Right" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Dois erros fazem um direito</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando uma pessoa tenta justificar uma ação contra outra pessoa porque a outra pessoa tomou ou tomaria a mesma ação contra ele ou ela.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <noscript><a href="/qa?seopagecat=&seobatch=230"><button type="button" class="d-inline btn btn-lg btn-primary mt-2 mb-1">Next Page</button></a></noscript>
        <a href="/logicalfallacies/Type-Token-Fallacy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia do Tipo-Token</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A falácia type-token é cometida quando uma palavra pode se referir a um tipo (representando um conceito descritivo abstrato) ou a um token (representando um objeto que instancia um conceito) e é usada de uma forma que não deixa claro a que se refere. </font><font style="vertical-align: inherit;">Esta é uma forma mais específica da falácia da ambigüidade.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Unfalsifiability" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Infalseabilidade</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Afirmar com confiança que uma teoria ou hipótese é verdadeira ou falsa, mesmo que a teoria ou hipótese não possa ser contestada por uma observação ou pelo resultado de qualquer experimento físico, geralmente sem fortes evidências ou boas razões.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">não testabilidade</font></font></i></div>
            </div>
        </a>
        <a href="/fallacies/unreasonable-inclusion-fallacy.html" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Falácia de inclusão irracional</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Tentar ampliar os critérios de inclusão em um grupo de má fama ou associado a um rótulo negativo a ponto de a definição do termo ser substancialmente alterada para condenar ou criminalizar um comportamento bem menos malicioso ou deletério.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Unwarranted-Contrast" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Contraste Injustificado</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Assumir que implicatura significa implicação, quando logicamente não significa. </font><font style="vertical-align: inherit;">Implicatura é uma relação entre o fato de alguém fazer uma afirmação e uma proposição. </font><font style="vertical-align: inherit;">Implicação é uma relação entre proposições, ou seja, os significados das declarações.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">alguns são, outros não</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Use-Mention-Error.html" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Erro de menção de uso</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Confundir a palavra usada para descrever uma coisa, com a própria coisa. </font><font style="vertical-align: inherit;">Para evitar esse erro, costuma-se colocar a palavra usada para descrever a coisa entre aspas.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">UME</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Weak-Analogy" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Analogia Fraca</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando uma analogia é usada para provar ou refutar um argumento, mas a analogia é muito diferente para ser eficaz, ou seja, é mais diferente do argumento do que semelhante ao argumento.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">analogia ruim, analogia falsa, analogia falha, analogia questionável, argumento de semelhança espúria, metáfora falsa</font></font></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Willed-Ignorance" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Ignorância voluntária</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Recusar-se a mudar de ideia ou considerar informações conflitantes com base no desejo de manter as crenças existentes.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        <a href="/logicalfallacies/Wishful-Thinking" class="list-group-item list-group-item-action align-center">
            <h5 class="mb-1 text-secondary"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">pensamento positivo</font></font></h5>
            <p class="mb-2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Quando o desejo de que algo seja verdadeiro é usado no lugar de/ou como evidência da veracidade da afirmação. </font><font style="vertical-align: inherit;">O pensamento positivo, mais como um viés cognitivo do que uma falácia lógica, também pode fazer com que a pessoa avalie as evidências de maneira muito diferente com base no resultado desejado.</font></font></p>
            <div class="mt-2">
            <div class="small text-muted"><i></i></div>
            </div>
        </a>
        </div></div></body></html> 
    '''

    try:
        # listaPartidas = []
        # listaPartidasFilezinho = []
        # url = "http://www.statarea.com/predictions/date/"+ data +"/competition"


        # response = urlopen("http://www.google.com/").read()

        htmlparser = etree.HTMLParser()
        # htmlparser = etree.HTMLParser(encoding='utf8')

        # tree = etree.parse(htmlCode, htmlparser)
        tree = etree.parse(StringIO(htmlCode), htmlparser)
        
        # tree = etree.parse(StringIO.StringIO(html), htmlparser)

        listaLinks = []
        translator = Translator()

        links = tree.xpath('//a[@class="list-group-item list-group-item-action align-center"]/@href')
        # hs = open("listaLinks.txt","a")
        for link in links:
            # print(link)
            listaLinks.append(link)
            # hs.write(link + '\n')
            url = "https://www.logicallyfallacious.com/" + link

            print(url)
            response = urlopen(url).read()
            # print(response)
            paginaString = response.decode("utf-8")

            # with open('file.txt', 'w') as file:
            #     file.write(paginaString)
            # break
            
            htmlparser2 = etree.HTMLParser()
            tree2 = etree.parse(StringIO(paginaString), htmlparser2)
            tituloPaginaHTML = tree2.xpath('//h1[@class="lftitle"]/text()')
            tituloTraduzido = translator.translate(tituloPaginaHTML, src='en', dest='pt')
            tituloPagina = tituloTraduzido[0].text
            print(tituloPagina)

            termoLatimPaginaHTML = tree2.xpath('//p[@class="uk-text-large"]/text()')
            termoLatim = termoLatimPaginaHTML[0]
            print(termoLatim)

            outrosNomesPaginaHTML = tree2.xpath('//p[@style="font-style: italic;"]/text()')
            outrosNomesTraduzido = translator.translate(outrosNomesPaginaHTML, src='en', dest='pt')
            outrosNomes = outrosNomesTraduzido[0].text
            print(outrosNomes)

            conteudoPaginaHTML = tree2.xpath('//p[@class="Body"]')
            conteudoPaginaHTML2 = tree2.xpath('//p[@class="Body"]/text()')


            body1StrongHTML = conteudoPaginaHTML[0].xpath('//strong/text()')
            body1StrongTraduzido = translator.translate(body1StrongHTML, src='en', dest='pt')
            body1Strong = body1StrongTraduzido[0].text
            print(body1Strong)

            body1ContentTraduzido = translator.translate(conteudoPaginaHTML2, src='en', dest='pt')
            body1Content = body1ContentTraduzido[0].text
            print(body1Content)    

            body1StrongHTML = conteudoPaginaHTML[1].xpath('//strong/text()')
            body1StrongTraduzido = translator.translate(body1StrongHTML, src='en', dest='pt')
            body1Strong = body1StrongTraduzido[0].text
            print(body1Strong)

            body1Content = body1ContentTraduzido[1].text
            print(body1Content) 



        # hs.close() 


            


        # idsCampeonatos = tree.xpath('//a[@class="list-group-item list-group-item-action align-center"]/@href')

        # for idCampeonato in idsCampeonatos :
        #     idsPartidas = tree.xpath('//div[@id="'+ idCampeonato +'"]/div[@class="body"]/div[@class="match"]/@id')
        #     # print (idsPartidas)



    except Exception as e:
        # print('Ocorreu uma falha na raspagem - %s.' % e.code)

        # if e.code == 404:
        #     print("Erro") 

        print(e)
        pass
        


rodarScript()