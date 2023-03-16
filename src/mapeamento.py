import numpy as np, matplotlib.pyplot as plt, json


with open('dados2021.json', 'r') as arqv:
    incidentes = json.load(arqv)

latitude = []
longitude = []
for caso in incidentes:
    if caso['uf'] == 'BA':
        latitude.append(float(caso['latitude']))
        longitude.append(float(caso['longitude']))

ponta={
    'norte': max(latitude), 
    'sul': min(latitude) , 
    'leste': max(longitude), 
    'oeste':  min(longitude)
}
print(ponta['norte'] - ponta['sul'])
print(ponta['leste'] - ponta['oeste'])

lat = np.array(latitude)
lon = np.array(longitude)
print(ponta)

plt.grid(True)
plt.scatter(lon, lat, s = 0.5)
plt.show()