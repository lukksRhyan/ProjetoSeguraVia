import json,Acidentes
with open('./assets/datatran2022.json','r') as arqv:
    incidentes = json.load(arqv)
    #print(incidentes[0])
    for caso in incidentes:

        atual = Acidentes.Acidente(caso)
        atual.databaseInsert()
        i = 0