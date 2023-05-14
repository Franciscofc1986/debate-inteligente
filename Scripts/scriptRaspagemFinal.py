
def extrairTexto(texto):
    resposta = texto
    try:
        posicaoDoisPontos = texto.find(":", 1) + 2

        if posicaoDoisPontos > 1:
            resposta = texto[posicaoDoisPontos:-1]
    except:
        pass
    return resposta

with open('./bd/listaC4.csv', 'a', errors='ignore') as file:

    f = open("./bd/listaC.csv", "r")
    for l in f:
        try:
            dados = l.split(';')
            id = dados[0]
            nome = dados[1]
            outrosNomes = extrairTexto(dados[2])
            outrosNomes = outrosNomes[0:-1]
            latim = dados[3]
            descricao = extrairTexto(dados[4])
            formaLogica = extrairTexto(dados[5])
            excecao = extrairTexto(dados[6])
            solucao = dados[7]
            curiosidades = extrairTexto(dados[8])
            variacao = extrairTexto(dados[9])
            dica = extrairTexto(dados[10])

            file.write(str(id) + ";" + nome + ";" + outrosNomes + ";" + latim + ";" + descricao + ";" + formaLogica + ";" + excecao + ";" + solucao + ";" + curiosidades + ";" + variacao + ";" + dica + ";" + "\n")
            print(id)
            # print(outrosNomes)
            # print(descricao)
            # print(formaLogica)
            # print(excecao)
            # print(solucao)
            # print(curiosidades)
            # print(variacao)
            # print(dica)

            # break

        except:
            pass
