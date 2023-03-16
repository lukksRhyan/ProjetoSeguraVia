import json

def CSVparaJson(fonte, destino):

    with open(fonte, 'r', encoding='UTF-8') as arqv:

        chaves = arqv.readline().replace('"', '').split(';')
        print("Arquivo aberto, lendo informações...")
        lista = []
        for linha in arqv:
            dicio = {}
            semAspas = linha.replace('"', '')
            colun = semAspas.split(';')
            for i in range(len(chaves)):
                dicio.update({ chaves[i] : colun[i]})

            lista.append(dicio)
        print("Leitura completa, salvando arquivo de destino...")
    with open(destino, 'w', encoding='UTF-8') as arqv:
        json.dump(lista, arqv)        
    print("Arquivo convertido com sucesso.")
        
fonte = 'D:\\datatran2018   .csv'
destino = fonte.replace('csv', 'json')
CSVparaJson(fonte, destino)