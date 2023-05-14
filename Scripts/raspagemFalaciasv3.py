import sys

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
from googletrans import Translator
from falacia_objeto import Falacia


termoLatim = False
outrosNomes = False
novasTerminologias = False
descricao = False
formaLogica = False
exemplo1 = False
explicacao1 = False
exemplo2 = False
explicacao2 = False
exemplo3 = False
explicacao3 = False
exemplo4 = False
explicacao4 = False
excecao = False
curiosidades = False
variacao = False
dica = False
referencias = False
resto = False

translator = Translator()

def tudoFalso():
    global termoLatim, outrosNomes, novasTerminologias, descricao, formaLogica, exemplo1, explicacao1, exemplo2, explicacao2, exemplo3, explicacao3, exemplo4, explicacao4, excecao, curiosidades, variacao, dica, referencias, resto

    termoLatim = False
    outrosNomes = False
    novasTerminologias = False
    descricao = False
    formaLogica = False
    exemplo1 = False
    explicacao1 = False
    exemplo2 = False
    explicacao2 = False
    exemplo3 = False
    explicacao3 = False
    exemplo4 = False
    explicacao4 = False
    excecao = False
    curiosidades = False
    variacao = False
    dica = False
    referencias = False
    resto = False

def processar(objFalacia, text):
    global termoLatim, outrosNomes, novasTerminologias, descricao, formaLogica, exemplo1, explicacao1, exemplo2, explicacao2, exemplo3, explicacao3, exemplo4, explicacao4, excecao, curiosidades, variacao, dica, referencias, resto
    # print(text)

    partesTexto = text.split(":")
    antesDoisPontos = ""
    apenasDados = False
    textoParaSalvar = text

    try:
        antesDoisPontos = partesTexto[0].lower()
        if len(antesDoisPontos) < 1:
            apenasDados = True
    except:
        apenasDados = True
        pass

    # print(termoLatim, outrosNomes, novasTerminologias, descricao, formaLogica, exemplo1, explicacao1, exemplo2, explicacao2, exemplo3, explicacao3, exemplo4, explicacao4, excecao, curiosidades, variacao, dica, referencias, resto)


    # print(antesDoisPontos)

    if not apenasDados:
        if termoLatim:
            tudoFalso()
            # print("passo1")
        elif antesDoisPontos == "(também conhecido como":
            tudoFalso()
            outrosNomes = True
            # print("passo2")
        elif antesDoisPontos == "nova terminologia" or antesDoisPontos == "novas terminologias":
            tudoFalso()
            novasTerminologias = True
            # print("passo3")
        elif antesDoisPontos == "descrição":
            tudoFalso()
            descricao = True
            # print("passo4")
        elif antesDoisPontos == "forma lógica" or antesDoisPontos == "formas lógicas":
            tudoFalso()
            formaLogica = True
            # print("passo5")
        elif antesDoisPontos == "exemplo 1" or antesDoisPontos == "exemplo #1" or antesDoisPontos == "exemplo nº 1":
            tudoFalso()
            exemplo1 = True
            # print("passo6")
        elif exemplo1 and antesDoisPontos == "explicação":
            tudoFalso()
            explicacao1 = True
            # print("passo7")
        elif antesDoisPontos == "exemplo 2" or antesDoisPontos == "exemplo #2" or antesDoisPontos == "exemplo nº 2":
            tudoFalso()
            exemplo2 = True
            # print("passo8")
        elif exemplo2 and antesDoisPontos == "explicação":
            tudoFalso()
            explicacao2 = True
            # print("passo9")
        elif antesDoisPontos == "exemplo 3" or antesDoisPontos == "exemplo #3" or antesDoisPontos == "exemplo nº 3":
            tudoFalso()
            exemplo3 = True
            # print("passo10")
        elif exemplo3 and antesDoisPontos == "explicação":
            tudoFalso()
            explicacao3 = True
            # print("passo11")
        elif antesDoisPontos == "exemplo 4" or antesDoisPontos == "exemplo #4" or antesDoisPontos == "exemplo nº 4":
            tudoFalso()
            exemplo4 = True
            # print("passo12")
        elif exemplo4 and antesDoisPontos == "explicação":
            tudoFalso()
            explicacao4 = True
            # print("passo13")
        elif antesDoisPontos == "exceção":
            tudoFalso()
            excecao = True
            # print("passo14")
        elif antesDoisPontos == "curiosidade":
            tudoFalso()
            curiosidades = True
            # print("passo15")
        elif antesDoisPontos == "variação":
            tudoFalso()
            variacao = True
            # print("passo16")
        elif antesDoisPontos == "dica":
            tudoFalso()
            dica = True
            # print("passo17")
        elif antesDoisPontos == "referências":
            tudoFalso()
            referencias = True
            # print("passo18")

    textoParaSalvar += " " 

    # print(termoLatim, outrosNomes, novasTerminologias, descricao, formaLogica, exemplo1, explicacao1, exemplo2, explicacao2, exemplo3, explicacao3, exemplo4, explicacao4, excecao, curiosidades, variacao, dica, referencias, resto)

    if outrosNomes:
        objFalacia.outrosNomes += textoParaSalvar
    elif novasTerminologias:
        objFalacia.novasTerminologias += textoParaSalvar
    elif descricao:
        objFalacia.descricao += textoParaSalvar
    elif formaLogica:
        objFalacia.formaLogica += textoParaSalvar
    elif exemplo1:
        objFalacia.exemplo1 += textoParaSalvar
    elif explicacao1:
        objFalacia.explicacao1 += textoParaSalvar
    elif exemplo2:
        objFalacia.exemplo2 += textoParaSalvar
    elif explicacao2:
        objFalacia.explicacao2 += textoParaSalvar
    elif exemplo3:
        objFalacia.exemplo3 += textoParaSalvar
    elif explicacao3:
        objFalacia.explicacao3 += textoParaSalvar
    elif exemplo4:
        objFalacia.exemplo4 += textoParaSalvar
    elif explicacao4:
        objFalacia.explicacao4 += textoParaSalvar
    elif excecao:
        objFalacia.excecao += textoParaSalvar
    elif curiosidades:
        objFalacia.curiosidades += textoParaSalvar
    elif variacao:
        objFalacia.variacao += textoParaSalvar
    elif dica:
        objFalacia.dica += textoParaSalvar
    elif referencias:
        objFalacia.referencias += textoParaSalvar
        tudoFalso()
    else:
        objFalacia.resto += textoParaSalvar


def salvarCampo(campoParaSalvar):
    campoParaSalvar = campoParaSalvar.replace(";", ",")
    try:
        file.write(campoParaSalvar + ";" )
    except Exception as e:
        print("Erro salvando o texto: " + campoParaSalvar)
        print(e)
        print("Tentando corrigi-lo: " )
        campoAlterado = campoParaSalvar.encode('utf-8', errors='ignore')
        print(campoAlterado)
        campoAlterado = campoParaSalvar.decode('utf-8', errors='ignore')
        print(campoAlterado)
        pass

with open('./bd/falacias14.csv', 'a', errors='ignore') as file:
    file.write("titulo;termoLatim;outrosNomes;novasTerminologias;descricao;formaLogica;exemplo1;explicacao1;exemplo2;explicacao2;exemplo3;explicacao3;exemplo4;explicacao4;excecao;curiosidades;variacao;dica;referencias;" + "\n")
    f = open("listaLinks.txt", "r")
    for x in f:

        _falacia = Falacia("")
        tudoFalso()

        url = "https://www.logicallyfallacious.com" + x
        try:
            page = urlopen(url)
        except:
            print("Error opening the URL")
            pass

        soup = BeautifulSoup(page, 'html.parser')

        paginaFalacia = soup

        try:
            content = paginaFalacia.find('h1', {"class": "lftitle"})
            titulo = content.text
            tituloTranslate = translator.translate(titulo, src='en', dest='pt')
            tituloTraduzido = tituloTranslate.text
            # file.write(tituloTraduzido + ";")
            _falacia.titulo = tituloTraduzido
            # print(tituloTraduzido)
        except:
            pass

        try:
            content = paginaFalacia.find('p', {"class": "uk-text-large"})
            termoLatim = content.text
            # file.write(termoLatim + ";")

            _falacia.termoLatim = termoLatim
            termoLatim = True
            # print(termoLatim)
        except:
            pass


        conteudoPagina = paginaFalacia.find('div', {"class": "mx-auto"})
        
        for i in conteudoPagina.findAll('p'):
            try:
                textoBody = i.text
                textObjectTranslator = translator.translate(textoBody, src='en', dest='pt')
                textoTraduzido = textObjectTranslator.text

                processar(_falacia, textoTraduzido)

                # print(textoTraduzido)
                # print("--------------------")
                
                # file.write(textoPronto + ";")
            except:
                pass
        # print(_falacia.__dict__)
        print("------------------------------------------------------------------" + "\n" )
        print("---Titulo---" + "\n" )
        print(_falacia.titulo)
        print("---Latim---" + "\n" )
        print(_falacia.termoLatim)
        print("---Tambem conhecido como---"+ "\n" )
        print(_falacia.outrosNomes)
        print("---Novas Terminologias---"+ "\n" )
        print(_falacia.novasTerminologias)
        print("---Descricao---"+ "\n" )
        print(_falacia.descricao)
        print("---Forma Logica---"+ "\n" )
        print(_falacia.formaLogica)
        print("---Exemplo 1---"+ "\n" )
        print(_falacia.exemplo1)
        print("---Explicacao 1---"+ "\n" )
        print(_falacia.explicacao1)
        print("---Exemplo 2---"+ "\n" )
        print(_falacia.exemplo2)
        print("---Explicacao 2---"+ "\n" )
        print(_falacia.explicacao2)
        print("---Exemplo 3---"+ "\n" )
        print(_falacia.exemplo3)
        print("---Explicacao 3---"+ "\n" )
        print(_falacia.explicacao3)
        print("---Exemplo 4---"+ "\n" )
        print(_falacia.exemplo4)
        print("---Explicacao 4---"+ "\n" )
        print(_falacia.explicacao4)
        print("---Excecao---"+ "\n" )
        print(_falacia.excecao)
        print("---Curiosidades---"+ "\n" )
        print(_falacia.curiosidades)
        print("---Variacao---"+ "\n" )
        print(_falacia.variacao)
        print("---Dica---"+ "\n" )
        print(_falacia.dica)
        print("---Referencias---"+ "\n" )
        print(_falacia.referencias)

        
        salvarCampo(_falacia.titulo) 
        salvarCampo(_falacia.termoLatim) 
        salvarCampo(_falacia.outrosNomes) 
        salvarCampo(_falacia.novasTerminologias) 
        salvarCampo(_falacia.descricao) 
        salvarCampo(_falacia.formaLogica) 
        salvarCampo(_falacia.exemplo1) 
        salvarCampo(_falacia.explicacao1) 
        salvarCampo(_falacia.exemplo2) 
        salvarCampo(_falacia.explicacao2) 
        salvarCampo(_falacia.exemplo3) 
        salvarCampo(_falacia.explicacao3) 
        salvarCampo(_falacia.exemplo4) 
        salvarCampo(_falacia.explicacao4) 
        salvarCampo(_falacia.excecao) 
        salvarCampo(_falacia.curiosidades) 
        salvarCampo(_falacia.variacao) 
        salvarCampo(_falacia.dica) 
        salvarCampo(_falacia.referencias)
        file.write( "\n")

# article = ''
# for i in content.findAll('p'):
#     article = article + ' ' +  i.text
# print(article)

# Saving the scraped text
# with open('scraped_text.txt', 'w') as file:
#     file.write(article)