
def extrairTexto(texto):
    resposta = texto
    try:
        posicaoDoisPontos = texto.find(":", 1) + 2

        if posicaoDoisPontos > 1:
            resposta = texto[posicaoDoisPontos:-1]
    except:
        pass
    return resposta 

# contador = 0
with open('./bd/listaC3.csv', 'a', errors='ignore') as file:

    f = open("./bd/listaC1.csv", "r")
    for l in f:
        try:
            dados = l.split(';')
            id = dados[0]
            exem1 = extrairTexto(dados[7])
            exp1 = extrairTexto(dados[8])    
            exem2 = extrairTexto(dados[9])
            exp2 = extrairTexto(dados[10]) 
            exem3 = extrairTexto(dados[11])
            exp3 = extrairTexto(dados[12]) 
            exem4 = extrairTexto(dados[13])
            exp4 = extrairTexto(dados[14]) 
            if len(exem1) > 1:
                file.write(str(id) + ";" + exem1 + ";" + exp1 + ";" + "\n")
            if len(exem2) > 1:
                file.write(str(id) + ";" + exem2 + ";" + exp2 + ";" + "\n")
            if len(exem3) > 1:
                file.write(str(id) + ";" + exem3 + ";" + exp3 + ";" + "\n")
            if len(exem4) > 1:
                file.write(str(id) + ";" + exem4 + ";" + exp4 + ";" + "\n")

            print(id)
            print(exem1)
            print(exp1)
            print(exem2)
            print(exp2)
            print(exem3)
            print(exp3)
            print(exem4)
            print(exp4)
        except:
            pass
