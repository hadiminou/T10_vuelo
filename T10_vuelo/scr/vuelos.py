from collections import namedtuple
import csv
from datetime import date, time, datetime 
Vuelo=namedtuple("vuelo","destino, precio, num_plazas, num_pasajeros, \
                 codigo,fecha,duracion,hora,velocidad,escalas,economico")

def a_booleano(a)->bool:
    res = None
    if a!= None:
        if a.upper().strip()=="S":
            res = True
        elif a.upper().strip()=="N":
            res = False
    return res

def parsea_escalas(lista):
    res = list()
    for i in lista.split("-"):
        res.append(i.strip())
    return res

def lee_vuelos(ruta:str)->list[Vuelo]:
    res=[]
    with open (ruta, "rt", encoding="utf-8") as f:
        lector=csv.reader(f, delimiter=";")
        next(lector)
        for destino, precio, num_plazas, num_pasajeros, \
                 codigo,fecha,duracion,hora,velocidad,escalas,economico in lector:
            precio = float(precio.replace(",","."))
            fecha = datetime.strptime(fecha.strip(),"%d/%m/%Y").date()
            hora = datetime.strptime(hora.strip(),"%H:%M:%S").time()
            res.append(Vuelo(destino.strip(), precio, int(num_plazas.strip()),\
                         int(num_pasajeros.strip()), codigo.strip(),fecha,int(duracion),\
                            hora,float(velocidad.strip()),parsea_escalas(escalas),a_booleano(economico)))
    return res

def filtra_vuelos_a(vuelos:list[Vuelo], destino)->list[Vuelo]:
    res=[]
    for i in vuelos:
        if i.destino == destino:
            res.append(i)
    return res

def vuelos_mas_velocidad_que(vuelos:list[Vuelo], velo:int)->list[(str, date, float)]:
    res=[]
    for i in vuelos:
        if i.velocidad>velo:
            res.append((i.destino, i.fecha, i.velocidad))
    return res

def todos_vuelos_mas_velocidad_que(vuelos:list[Vuelo], velo:int)->bool:
    res= True
    for i in vuelos:
        if i.velocidad<=velo:
            res=False
    return res

def vuelos_mas_velocidad(vuelos:list[Vuelo])->Vuelo:
    return max(vuelos, key= lambda e:e.velocidad)

def vuelos_por_horario(vuelos:list[Vuelo], mes)->list[(str, float, date,time)]:
    res = []
    for i in vuelos:
        if i.fecha.month == mes:
            res.append((i.destino, i.precio, i.fecha, i.hora))
    return sorted(res, key= lambda e:e[3])

def distintas_escalas(vuelos:list[Vuelo])->list[str]:
    res=set()
    for i in vuelos:
        res.add(i.destino)
        for e in i.escalas:
            res.add(e)
    return sorted(res)

def vuelos_con_escalas_en(vuelos:list[Vuelo], ciudad:str)->list:
    res=[]
    for i in vuelos:
        if ciudad in i.escalas:
            res.append((i.destino, i.precio, i.num_plazas-i.num_pasajeros))
    #return sorted([(i.destino, i.precio, i.num_plazas-i.num_pasajeros)\
    #  for i in vuelos if ciudad in i.escalas], key = lambda e:e[1])        
    return sorted(res, key = lambda e:e[1])

def numero_de_vuelo_por_destino(vuelos:list[Vuelo])->dict[str, int]:
    res=dict()
    for v in vuelos:
        if  v.destino not in res:
            res[v.destino]=0
        res[v.destino]+=1
    return res

def suma_de_pasajeros_por_fecha(vuelos:list[Vuelo])->dict[date, int]:
    res=dict()
    for i in vuelos:
        if i.fecha not in res:
            res[i.fecha] = 0
        res[i.fecha]+=i.num_pasajeros
    return res

def lista_distintos_por_compania(vuelos:list[Vuelo])->dict[str, list[str]]:
    res = dict()
    lista_destino = []
    for i in vuelos:
        # compania = i.codigo[:3]
        # if compania not in res:
        #     res[compania]=list()
        # res[compania].append(i.destino)
        if parsea_escalas(i.codigo)[0] not in res:
            res[parsea_escalas(i.codigo)[0]] = 0
        lista_destino.append(i.destino)
        res[parsea_escalas(i.codigo)[0]] = lista_destino
    return res

def vuelos_entre_fechas(vuelos:list[Vuelo], fecha1:date = None, fecha2:date = None)->\
                        list[tuple[date, str, float, list[str]]]:
    res = []
    #fecha_intervalo = [min(fecha1, fecha2), max(fecha1, fecha2)]
    for i in vuelos:
        if (fecha1==None or fecha1<=i.fecha) and (fecha2==None or i.fecha<=fecha2):
            res.append((i.fecha, i.destino, i.precio, i.escalas))
    return sorted(res)
    #     if fecha1 != None and fecha2 != None:
    #         if i.fecha>=fecha_intervalo[0] and i.fecha<=fecha_intervalo[1]:
    #             res.append((i.destino, i.precio, i.fecha, i.escalas))
    #     if min(fecha_intervalo) == None and max(fecha_intervalo) != None:
    #         if i.fecha<=max(fecha_intervalo):
    #             res.append((i.destino, i.precio, i.fecha, i.escalas))
    #     if max(fecha_intervalo) == None and min(fecha_intervalo) != None:
    #         if i.fecha>=min(fecha_intervalo):
    #             res.append((i.destino, i.precio, i.fecha, i.escalas))
    # return sorted(res, key = lambda e:e[2]) 

def destinos_distintos_por_compania(vuelos:list[Vuelo])->dict[str, set[str]]:
    res = dict()
    for i in vuelos:
        compania=i.codigo[:3]
        if compania not in res:
            res[compania] = set()
        res[compania].add(i.destino)
    return res

def codigos_vuelos_mas_plazas_que_por_numero_de_escalas(vuelos:list[Vuelo], num_plaz:int)->dict[list, list]:
    res = dict()
    for i in vuelos:
        if i.num_plazas > num_plaz:
            num_escalas=len(i.escalas)
            if num_escalas not in res:
                res[num_escalas]=list()
            res[num_escalas].append(i.codigo)
    return res

def vuelo_menor_duracin_por_destino(vuelos:list[Vuelo])->dict[str, set[str, int]]:
    dict_aux = dict()
    res = dict()
    for i in vuelos:
        if i.destino not in dict_aux:
            dict_aux[i.destino] = list()
        dict_aux[i.destino].append((i.codigo,i.duracion))
    for clave, valor in dict_aux.items():
        res[clave] = min(valor, key = lambda e:e[1])
    return res

def promedio_de_precios_por_compania(vuelos:list[Vuelo], booleano:bool)->list[str, float]:
    res = dict()
    for i in vuelos:
        if i.economico == booleano:
            compania = i.codigo[:3]
            if compania not in res:
                res[compania] = list()
            res[compania].append(i.precio)
    for c,v in res.items():
        res[c] = sum(v)/len(v)
    return list(res.items())

def n_vuelos_mayor_velocidad_por_meses(vuelos:list[Vuelo], n:int)->dict[int, list[tuple[str, date, float]]]:
    res = dict()
    aux = dict()
    for i in vuelos:
        if i.fecha.month not in aux:
            aux[i.fecha.month] = list()
        aux[i.fecha.month].append((i.codigo, i.fecha, i.velocidad))
        for c,v in aux.items():
            res[c] = sorted(v, key = lambda e:e[2], reverse = True)[:n]
    return res

def  escala_por_la_que_pasan_más_vuelos_entre_fechas(vuelos:list[Vuelo], \
                                                    fecha1:date=None, fecha2:date=None)->str:
    res = None
    aux = dict()
    for i in vuelos:
        if (fecha1==None or fecha1<=i.fecha) and (fecha2==None or i.fecha<=fecha2):
            for escala in i.escalas:
                if escala not in aux:
                    aux[escala] = 0
                aux[escala]+=1
    if len(aux)>0:
        res=max(aux.items(), key = lambda e:e[1])[0]
    return res

def vuelo_con_mayor_porcentaje_de_ocupacion_por_destino(vuelos:list[Vuelo])->dict[str,tuple[str,int,int,float]]:
    res = dict()
    dic_aux = dict()
    for i in vuelos:
        porcentaje = (i.num_pasajeros/i.num_plazas)*100
        if i.destino not in res:
            res[i.destino] = list()
        res[i.destino].append((i.codigo, i.num_plazas, i.num_pasajeros, porcentaje))
        for c,v in res.items():
            dic_aux[c] = max(v, key = lambda e:e[3])
            #dic_aux[c] = min(v, key = lambda e:e[3])
    return dic_aux

def destino_menor_promedio_de_precios_mayor_porcentaje_ocupacion(vuelos:list[Vuelo], n_porcentaje:int)->str:
    res = dict()
    dic_aux = dict()
    for i in vuelos:
        porcentaje = (i.num_pasajeros/i.num_plazas)*100
        if porcentaje >= n_porcentaje:
            if i.destino not in dic_aux:
                dic_aux[i.destino] = list()
            dic_aux[i.destino].append(i.precio)
    for c,v in dic_aux.items():
        res[c] = sum(v)/len(v)
    print (res)
    return min(res.items(), key = lambda e:e[1])[0]

def compania_con_mas_pasajeros_por_destino(vuelos:list[Vuelo])->dict[str, str]:
    aux = dict()
    aux2 = dict()
    res = dict()
    for i in vuelos:
        clave = (i.destino,i.codigo[:3])
        if i.destino not in aux:
            aux[clave] = 0
        aux[clave]+=i.num_pasajeros
        for c,v in aux.items():
            if c[0] not in aux2:
                aux2[c[0]] = list()
            aux2[c[0]].append((c[1],v))
        for c,v in aux2.items():
            res[c] = max(v, key = lambda e:e[1])[0]            
    return res

def calcular_el_incremento_o_decremento_de_pasajeros(vuelos:list[Vuelo])->list[tuple[date]]:
    aux = dict()
    res = list()
    for i in vuelos:
        if i.fecha not in aux:
            aux[i.fecha] = 0
        aux[i.fecha]+=i.num_pasajeros
    lista_ordenada = sorted(aux.items())
    for tupla1, tupla2 in zip(lista_ordenada[1:], lista_ordenada[0:]):
        res.append((tupla1[0], tupla1[1]-tupla2[1]))
    return res