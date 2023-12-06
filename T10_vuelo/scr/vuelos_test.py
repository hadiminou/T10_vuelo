from vuelos import*
from datetime import date

def test_lee_vuelos(vuelos):
    print("###test lee vuelos###")
    print(f"\n{len(vuelos)} registros leidos")
    print("\nlos tres primeros son:", vuelos[:3])
    print("\nlos tres ultimos son:", vuelos[-3:])
    '''print("\nlos tres primeros son:")
    for i in (0,3):
        print(vuelos[i])
    print("\nlos tres ultimos son:")
    for i in (1,4):
        print(vuelos[-i])'''

def test_filtra_vuelos_a(vuelos:list[Vuelo]):
    print("\n###test filtra vuelos a###")
    destino="Madrid"
    print(f"vuelos con destino {destino}:")
    for i in filtra_vuelos_a(vuelos, destino):
        print (i)

def test_vuelos_mas_velocidad_que(vuelos:list[Vuelo]):
    print("\n###test vuelos mas velocidad que###")
    velo=900
    print(f"vuelos con mas velocidad de {velo}:")
    for i in vuelos_mas_velocidad_que(vuelos, velo):
        print(i)

def test_todos_vuelos_mas_velocidad_que(vuelos:list[Vuelo]):
    print("\n###test todos vuelos mas velocidad que###")
    velo=100
    print(f"Are every flights have velocity more than {velo}? {todos_vuelos_mas_velocidad_que(vuelos, velo)}")

def test_vuelos_mas_velocidad(vuelos:list[Vuelo]):
    print("\n###test vuelos mas velocidad###")
    print("vuelo con mayor velocidad es:", vuelos_mas_velocidad(vuelos))

def test_vuelos_por_horario(vuelos:list[Vuelo]):
    print("\n###test vuelos por horario###")
    mes = 7
    print(f"vuelos en el mes {mes} ordenados por hora:")
    for i in vuelos_por_horario(vuelos, mes):
        print(i)

def test_distintas_escalas(vuelos:list):
    print("\n###test distintas escalas###")
    print(distintas_escalas(vuelos))

def test_vuelos_con_escalas_en(vuelos:list[Vuelo]):
    print("\n###test vuelos con  escalas en###")
    ciudad= 'Mallorca'
    for i in vuelos_con_escalas_en(vuelos, ciudad):
        print (i)

def test_numero_de_vuelo_por_destino(vuelos:list[Vuelo]):
    print("\n###test numero de vuelos por destino###")
    print("\ndiccionario de una vez:",numero_de_vuelo_por_destino(vuelos))
    res = numero_de_vuelo_por_destino(vuelos)
    print("\ndiccionario pareja a pareja:")
    for i in res.items():
        print (i)
    destin= input("\nTeclea un destino:")
    if destin in res.keys():
        print(f"Hay {res.get(destin)} vuelos de {destin}")
    else:
        print(f"No hay vuelos del destino {destin}")

def test_suma_de_pasajeros_por_fecha(vuelos:list[Vuelo]):
    print("\n###test suma de pasajeros por fecha###")
    res = suma_de_pasajeros_por_fecha(vuelos)
    print(res)
    for i in res.items():
        print(i)
    fecha = datetime.strptime(input("\nTeclea una fecha:"), "%Y-%m-%d").date()  #how to change str to date
    # dia=int(input("dia:"))
    # mes=int(input("mes:"))
    # ano=int(input("ano:"))
    # fecha=date(ano,mes,dia)
    # print("Numero pasajeros:", suma_de_pasajeros_por_fecha(vuelos).get(fecha,0))
    if fecha in res.keys():
        print(f"suma de los pasajeros de fecha {fecha} es: {res.get(fecha,0)}")
    else:
        print(f"No hay pasajeros para {fecha}")

def test_lista_distintos_por_compania(vuelos:list[Vuelo]):
    print("\n###test lista distintos por compania###")
    res = lista_distintos_por_compania(vuelos)
    for i in res.items():
        print(i)

def test_vuelos_entre_fechas(vuelos:list[Vuelo]):
    print("\n###test vuelos entre fechas###")
    #fecha1 = datetime.strptime("2021-8-8", "%Y-%m-%d").date()
    #fecha2 = datetime.strptime("2022-9-5", "%Y-%m-%d").date()
    fech1 = date(2021,8,1)
    fech2 = date(2022,9,5)
    res = vuelos_entre_fechas(vuelos, fech1,fech2)
    print(f"\nlos vuelos entre {fech1} y {fech2} son: {res}")
    print(f"\nlos vuelos desde {fech1} son: {vuelos_entre_fechas(vuelos, fech1)}")
    print(f"\nlos vuelos hasta {fech2} son: {vuelos_entre_fechas(vuelos, fecha2=fech2)}")

def test_destinos_distintos_por_compania(vuelos:list[Vuelo]):
    print("\n###test destinos distintos por compania###")
    res = destinos_distintos_por_compania(vuelos)
    for i in res.items():
        print(i)

def test_codigos_vuelos_mas_plazas_que_por_numero_de_escalas(vuelos:list[Vuelo]):
    print("\n###test_codigos_vuelos_mas_plazas_que_por_numero_de_escalas###")
    num = 300
    for i in codigos_vuelos_mas_plazas_que_por_numero_de_escalas(vuelos, num).items():
        print(i)

def test_vuelo_menor_duracin_por_destino(vuelos:list[Vuelo]):
    print("\n###test_vuelo_menor_duracin_por_destino###")
    for i in vuelo_menor_duracin_por_destino(vuelos).items():
        print(i)

def test_promedio_de_precios_por_compania(vuelos:list[Vuelo]):
    print("###test_promedio_de_precios_por_compania###")
    print("el promedio de precios para vuelos economicos")
    for i in promedio_de_precios_por_compania(vuelos, booleano=True):
        print(i)
    print("el promedio de precios para vuelos no economicos")
    for i in promedio_de_precios_por_compania(vuelos, booleano=False):
        print(i)

def test_n_vuelos_mayor_velocidad_por_meses(vuelos:list[Vuelo]):
    print("test_n_vuelos_mayor_velocidad_por_meses")
    num = 4
    for i in n_vuelos_mayor_velocidad_por_meses(vuelos, num).items():
        print(i)

def test_escala_por_la_que_pasan_más_vuelos_entre_fechas(vuelos:list[Vuelo]):
    print("test_escala_por_la_que_pasan_más_vuelos_entre_fechas")
    fech1 = date(2023,1,1)
    fech2 = date(2023,12,31)
    print("la escala con mas vuelos es:", escala_por_la_que_pasan_más_vuelos_entre_fechas(vuelos))
    print(f"la escala con más vuelos entre {fech1} y {fech2}:\
          {escala_por_la_que_pasan_más_vuelos_entre_fechas(vuelos, fech1, fech2)}")
    print(f"la escala con más vuelos desde {fech1}:\
           {escala_por_la_que_pasan_más_vuelos_entre_fechas(vuelos, fech1)}")
    print(f"la escala con más vuelos hasta {fech2}:\
           {escala_por_la_que_pasan_más_vuelos_entre_fechas(vuelos,fecha2=fech2)}")

def test_vuelo_con_mayor_porcentaje_de_ocupacion_por_destino(vuelos:list[Vuelo]):
    print("test_vuelo_con_mayor_porcentaje_de_ocupacion_por_destino")
    for i in vuelo_con_mayor_porcentaje_de_ocupacion_por_destino(vuelos).items():
        print(i)

def test_destino_menor_promedio_de_precios_mayor_porcentaje_ocupacion(vuelos:list[Vuelo]):
    print("\ntest_destino_menor_promedio_de_precios_mayor_porcentaje_ocupacion")
    n = 60
    print(destino_menor_promedio_de_precios_mayor_porcentaje_ocupacion(vuelos, n))

def test_compania_con_mas_pasajeros_por_destino(vuelos:list[Vuelo]):
    print("\ntest_compania_con_mas_pasajeros_por_destino")
    for i in compania_con_mas_pasajeros_por_destino(vuelos).items():
        print(i)

def test_calcular_el_incremento_o_decremento_de_pasajeros(vuelos:list[Vuelo]):
    print("\ntest_calcular_el_incremento_o_decremento_de_pasajeros")
    for i in calcular_el_incremento_o_decremento_de_pasajeros(datos):
        print(i)

if __name__=="__main__":
    datos=lee_vuelos("Proyectos Python/T10_vuelo/data/vuelos.csv")
    #test_lee_vuelos(datos)
    #test_filtra_vuelos_a(datos)
    #test_vuelos_mas_velocidad_que(datos)
    #test_todos_vuelos_mas_velocidad_que(datos)
    #test_vuelos_mas_velocidad(datos)
    #test_vuelos_por_horario(datos)
    #test_distintas_escalas(datos)
    #test_vuelos_con_escalas_en(datos)
    #test_numero_de_vuelo_por_destino(datos)
    #test_suma_de_pasajeros_por_fecha(datos)
    #test_lista_distintos_por_compania(datos)
    #test_vuelos_entre_fechas(datos)
    #test_destinos_distintos_por_compania(datos)
    #test_codigos_vuelos_mas_plazas_que_por_numero_de_escalas(datos)
    #test_vuelo_menor_duracin_por_destino(datos)
    #test_promedio_de_precios_por_compania(datos)
    #test_n_vuelos_mayor_velocidad_por_meses(datos)
    #test_escala_por_la_que_pasan_más_vuelos_entre_fechas(datos)
    #test_vuelo_con_mayor_porcentaje_de_ocupacion_por_destino(datos)
    #test_destino_menor_promedio_de_precios_mayor_porcentaje_ocupacion(datos)
    #test_compania_con_mas_pasajeros_por_destino(datos)
    test_calcular_el_incremento_o_decremento_de_pasajeros(datos)