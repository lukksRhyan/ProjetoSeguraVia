import json
anos = ["08"]#,"08","09","10","11","12","13","14","15","16","17","18","19","20","21","22"]

for ano in anos:
    url = f"D:\Dados em json\datatran20{ano}.json"
    print(url)
    with open(url,"r") as arqv:
        casos = json.load(arqv)
        chaves = []
        for chave in casos[0].keys():
            chaves.append(chave)
        print(chaves)

with open("chaves.txt", "w") as arqv:
    json.dump(chaves, arqv)