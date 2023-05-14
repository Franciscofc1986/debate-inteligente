from googletrans import Translator

translator = Translator()

textoTraduzido = translator.translate('안녕하세요.')
# tituloTraduzido = translator.translate('dog', src='en', dest='pt')
print(textoTraduzido)