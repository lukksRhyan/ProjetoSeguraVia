import json
def pesqSemana():
    with open('dados2021.json', 'r') as arqv:
        incidentes = json.load(arqv)
        dias = {
            'domingo' : 0,
            'segunda-feira' : 0,
            'terça-feira' : 0,
            'quarta-feira' : 0,
            'quinta-feira' : 0,
            'sexta-feira' : 0,
            'sábado' : 0
        }
        for caso in incidentes:
            dia = caso['dia_semana']
            dias[dia] += 1
    with open('casosSemana.json', 'w') as arqv:
        json.dump(dias, arqv)
def pesMes():
    meses =  {
        'jan':0,
        'fev':0,
        'mar':0,
        'abr':0,
        'mai':0,
        'jun':0,
        'jul':0,
        'ago':0,
        'set':0,
        'out':0,
        'nov':0,
        'dez':0,
    }
    with open('datas.json', 'r') as listaMeses:
       listaMeses = json.load(listaMeses)#váriavel adquire o "nome" do arquivo que não vai ser mais utilizado.

    with open('dados2021.json', 'r') as arqv:

        incidentes = json.load(arqv)
        for caso in incidentes:
            mes = caso['data_inversa'][5:7]
            meses[listaMeses[mes]] +=1
    with open('casosMeses.json','w') as arqv:
        json.dump(meses, arqv)
def pesqUF():    
    with open('dados2021.json', 'r') as arqv:
        incidentes = json.load(arqv)

    estados = {}

    for caso in incidentes:
        #salvos = caso
        #salvos.pop('municipio')
        #salvos.pop('uf')
        if not caso['uf'] in list(estados.keys()):
            estados.update({ caso['uf'] : {}})
            estados[caso['uf']].update({caso['municipio']: []})
        else:
            if not caso['municipio'] in estados[caso['uf']]:
                estados[caso['uf']].update({caso['municipio']: []})
            else:
                estados [caso['uf']][caso['municipio']].append()
    for uf in list(estados.keys()):
        with open(f'Nestados\{uf}.json', 'w') as arqv:
            json.dump(estados[uf], arqv)

pesqUF()