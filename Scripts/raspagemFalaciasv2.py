# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
from googletrans import Translator

translator = Translator()

with open('falacias3.csv', 'a') as file:
    f = open("listaLinks.txt", "r")
    for x in f:
    
        url = "https://www.logicallyfallacious.com" + x
        try:
            page = urlopen(url)
        except:
            print("Error opening the URL")
            pass

        soup = BeautifulSoup(page, 'html.parser')

        try:
            content = soup.find('h1', {"class": "lftitle"})
            titulo = content.text
            tituloTranslate = translator.translate(titulo, src='en', dest='pt')
            tituloTraduzido = tituloTranslate.text
            file.write(tituloTraduzido + ";")
            print(tituloTraduzido)
        except:
            pass

        try:
            content = soup.find('p', {"class": "uk-text-large"})
            termoLatim = content.text
            file.write(termoLatim + ";")
            print(termoLatim)
        except:
            pass


        conteudoPagina = soup.find('div', {"class": "mx-auto"})

        
        for i in conteudoPagina.findAll('p'):
            try:
                textoTraduzido = translator.translate(i.text, src='en', dest='pt')
                textoPronto = textoTraduzido.text
                print(textoPronto)
                print("--------------------")
                
                file.write(textoPronto + ";")
            except:
                pass
        file.write("\n")

# article = ''
# for i in content.findAll('p'):
#     article = article + ' ' +  i.text
# print(article)

# Saving the scraped text
# with open('scraped_text.txt', 'w') as file:
#     file.write(article)