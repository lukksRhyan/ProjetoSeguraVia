import numpy as np
import matplotlib.pyplot as plt
import json

with open('D:\coordenadas.json', 'r') as arqv:
    dados = json.load(arqv)

plt.title("Acidentes por mês 2018 - 2022", loc = 'left')
plt.xlabel("tempo")
plt.ylabel('Número de acidentes')


#valores = list(dados.values())
valores = len(dados)
print(valores)
numCasos = np.array(valores)

#nomeMeses = list(dados.keys())
meses = np.array([0, 30])

plt.bar(meses, numCasos)
plt.show()
