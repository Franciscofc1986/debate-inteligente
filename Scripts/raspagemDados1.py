# import json
# import sys
# import datetime
# import urllib2
# from lxml import etree
# from lxml import html
# from partida import *
# from arquivos import *


# def acharJogosBons(data) :
#     try:
#         listaPartidas = []
#         listaPartidasFilezinho = []
#         url = "http://www.statarea.com/predictions/date/"+ data +"/competition"

#         response = urllib2.urlopen(url)
#         htmlparser = etree.HTMLParser()
#         tree = etree.parse(response, htmlparser)

#         idsCampeonatos = tree.xpath('//div[@class="competition"]/@id')

#         for idCampeonato in idsCampeonatos :
#             idsPartidas = tree.xpath('//div[@id="'+ idCampeonato +'"]/div[@class="body"]/div[@class="match"]/@id')
#             # print (idsPartidas)

#             for idPartida in idsPartidas :
#                 try :
#                     timeDaCasa = tree.xpath('//div[@id="'+ idCampeonato +'"]/div[@class="body"]/div[@id="' + idPartida + '"]/div[@class="matchrow"]/div[@class="teams"]/div[@class="hostteam"]/div[@class="name"]/a/text()')
#                     timeVisitante = tree.xpath('//div[@id="'+ idCampeonato +'"]/div[@class="body"]/div[@id="' + idPartida + '"]/div[@class="matchrow"]/div[@class="teams"]/div[@class="guestteam"]/div[@class="name"]/a/text()')
#                     tips = tree.xpath('//div[@id="'+ idCampeonato +'"]/div[@class="body"]/div[@id="' + idPartida + '"]/div[@class="inforow"]/div[@class="coefrow"]/div[@class="coefbox"]/div/text()')
#                     linksInfo = tree.xpath('//div[@id="'+ idCampeonato +'"]/div[@class="body"]/div[@id="' + idPartida + '"]/div[@class="inforow"]/div[@class="userrow"]/div[@class="actions"]/div[@class="info"]/a/@href')
#                     response1 = urllib2.urlopen(linksInfo[0])
                    
#                     tree1 = etree.parse(response1, htmlparser)

#                     golsAFavor = tree1.xpath('//div[contains(text(),"Average scored")]/ancestor::*/div[@class="value"]/text()')
#                     golsContra = tree1.xpath('//div[contains(text(),"Average conceded")]/ancestor::*/div[@class="value"]/text()')
#                     golsFavorTexto = golsAFavor[0] + " " + golsAFavor[1] if len(golsAFavor) == 2 else ""
#                     golsContraTexto = golsContra[0] + " " + golsContra[1] if len(golsContra) == 2 else ""
#                     golFavor0 = float(golsAFavor[0])
#                     golFavor1 = float(golsAFavor[1])
#                     golContra0 = float(golsContra[0])
#                     golContra1 = float(golsContra[1])
#                     pontos = (((golFavor0 + golFavor1) * 1.5) + (golContra0 + golContra1)) / 2
#                     linhaDados = tips[4] + "\t " + golsFavorTexto + " - " + golsContraTexto + "\t\t" +  idCampeonato + "," + idPartida + "," + timeDaCasa[0] + " x " + timeVisitante[0] + "\n"
#                     listaPartidas.append(Partida(linhaDados, tips[4], pontos, timeDaCasa[0], timeVisitante[0]))
#                     if (golFavor0 > 2 or golFavor1 > 2) and ((golFavor0 + golFavor1) > 3.1) and ((golContra0 + golContra1) > 2.1) and tips[4] > 75 :
#                         listaPartidasFilezinho.append(Partida(linhaDados, tips[4], pontos, timeDaCasa[0], timeVisitante[0]))
#                     print(linhaDados)
#                 except (Exception) as error:
#                     print("Ocorreu um erro ao tentar pegar jogos. Mas foi contornado...")


#         listaPartidasOrdenadas = sorted(listaPartidas, reverse=True)
#         listaPartidasFilezinhoOrdenada = sorted(listaPartidasFilezinho, reverse=True)

#         listaStatarea = []
#         for umaPartida in listaPartidasOrdenadas :
#             listaStatarea.append(umaPartida.getTexto())

#         arquivo = "Dados/"+data+"(todosTips).txt"
#         registrarArquivo(arquivo, listaStatarea)

#         return listaPartidasFilezinhoOrdenada

#     except urllib2.HTTPError, e:
#         print 'Ocorreu uma falha na raspagem - %s.' % e.code

#         if e.code == 404:
#             acharJogosBons(data) 

#         return None
