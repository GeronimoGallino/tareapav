from registro import *
import random


# Ordenamos la variable part de menor a mayor
def ordenar_ranking(part):
    n = len(part)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if part[i].ranking > part[j].ranking:
                part[i], part[j] = part[j], part[i]
    return part


# Cargamos el registro Participantes automaticamnte
def cargar_automatico():
    name = ['Juan', 'Gero', 'Nacho', 'Torra', 'King Kong', 'Mateo', 'Clemente', 'Fran',
            'Valen', 'Facu', 'Tomas', 'Pedro', 'Alejo', 'Agus', 'Lauti', 'Bernardo']
    part = [0] * 16
    print('LISTA DE CONTINENTES\n-0: América\n-1: Europa\n-2: Asia\n-3: África\n-4: Oceanía')
    for i in range(16):
        nom = name[i]
        cont = random.randint(0, 4)
        rank = random.randint(1, 30)
        part[i] = Participante(nom, cont, rank)
    return part


# Cargamos el registro Participantes manualmente
def cargar_manual():
    part = [0] * 16
    print(
        'LISTA DE CONTINENTES(Ingrese el N° según su continente)\n-0: América\n-1: Europa\n-2: Asia\n-3: África\n-4: Oceanía')
    for i in range(16):
        nom = input('Ingrese Nombre del participante N°[' + str(i) + ']: ')
        cont = validar(0, 4, 'Ingrese Contienente al que pertenece: ')
        rank = validar(1, 30, 'Ingrese Ranking Mundial (1-30) del participante N°[' + str(i) + ']: ')
        part[i] = Participante(nom, cont, rank)
    return part


# Funcion de validacion para cargar los continentes y rankings
def validar(inf, sup, mensaje):
    cont = int(input(mensaje))
    while inf > cont or cont > sup:
        print('ERROR...El N° debe ir entre', inf, 'y', sup, '...')
        cont = int(input(mensaje))
    return cont


# Contamos la cantidad de participantes por continente
def partxcont(part):
    cant_part = [0] * 5
    for i in range(16):
        for j in range(5):
            if part[i].continente == j:
                cant_part[j] += 1
    return cant_part


# Generacion de puntos para cada ronda
def cargar_puntaje(part):
    n = len(part)
    for i in range(n):
        punt = random.randint(0, 1000)
        part[i].puntaje = punt
    return part


# Funcion para poder jugar cada ronda del torneo
# Si el parametro partidos es igual a 0 significa que se quiere  jugar el tercer y cuarto puesto
def jugar(part, partidos):
    if partidos != 0:
        for i in range(partidos):
            j = partidos * 2 - 1 - i
            if part[i].puntaje < part[j].puntaje:
                part[i].eliminado = 1
            else:
                part[j].eliminado = 1

    else:
        if part[2].puntaje > part[3].puntaje:
            part[2].eliminado = 0
        else:
            part[3].eliminado = 0


# Funcion para poner a los ganadores primeros en la variable part
def ordenar_ganadores(part, jugadores):
    for i in range(jugadores):
        j = jugadores * 2 - 1 - i
        if part[i].eliminado == 1:
            part[i], part[j] = part[j], part[i]


# Funcion para calcular el promedio en cada ronda
def puntaje_promedio(part, jugadores):
    acumulador = 0
    for i in range(jugadores):
        acumulador += part[i].puntaje
    promedio = round(acumulador / jugadores, 2)
    return promedio


def validar_enter(mensaje):
    enter = input(mensaje)
    while enter != '':
        print('Error debe apretar enter')
        enter = input(mensaje)
    return True


def test():
    print('MUNDIAL VIRTUAL')
    print('~' * 17)
    # Preguntamos al usuario si quiere hacer la carga de datos de los participantes manualmente o automaticamnete
    carga = input('Para carga manual inserte "M", para carga automática pulse ENTER: ')
    # Cargamos la variable part manualmente
    if carga == 'M':
        part = cargar_manual()
    # Cargamos la variable part automaticamnte
    else:
        part = cargar_automatico()
    # Ordenamos la variable part por ranking de menor a mayor
    ordenar_ranking(part)
    # Mostramos la variable part por ranking de menor a mayor
    write1(part)
    print()
    # Contamos la cantidad de participantes por continente
    cant_part = partxcont(part)
    print('America tiene: ', cant_part[0], ' participantes')
    print('Europa tiene: ', cant_part[1], ' participantes')
    print('Asia tiene: ', cant_part[2], ' participantes')
    print('África tiene: ', cant_part[3], ' participantes')
    print('Oceanía tiene: ', cant_part[4], ' participantes')
    print()


    if validar_enter('Aprete enter para jugar octavos de final: '):
        print('\nOCTAVOS DE FINAL!')
        print('~' * 17)
        # Cargamos el puntaje para octavos
        cargar_puntaje(part)
        # Se juegan los octavos de final
        jugar(part, 8)
        # Se muestran los cruces y los ganadores de los octavos de final
        write_partidos(part, 8)
        # Calculamos el promdio de puntos por jugador para octavos de final
        promedio_octavos = puntaje_promedio(part, 16)
        print('El puntaje promedio por jugador para esta ronda es de: ', promedio_octavos)
        print()
    if validar_enter('Aprete enter para jugar cuartos de final: '):
        print('\nCUARTOS DE FINAL!')
        print('~' * 17)
        # Para jugar cuartos de final ordenamos el vector part con los ganadores al principio
        ordenar_ganadores(part, 8)
        # Cargamos el puntaje para cuartos
        cargar_puntaje(part)
        # Se juegan los octavos de final
        jugar(part, 4)
        # Se muestran los cruces y los ganadores de los cuartos de final
        write_partidos(part, 4)
        # Calculamos el promdio de puntos por jugador para Cuartos de final
        promedio_cuartos = puntaje_promedio(part, 8)
        print('El puntaje promedio por jugador para esta ronda es de: ', promedio_cuartos)
        print()
    if validar_enter('Aprete enter para jugar semifinales: '):
        print('\n SEMIFINALES')
        print('~' * 17)
        # Ordenamos el vector part con los ganadores al principio para poder jugar las semi finales al igual que lo hicimos en cuartos
        ordenar_ganadores(part, 4)
        # Cargamos el puntaje para semifinales
        cargar_puntaje(part)
        # Se juegan las semi finales
        jugar(part, 2)
        # Se muestran los cruces y los ganadores de los semifinales
        write_partidos(part, 2)
        # Calculamos el promdio de puntos por jugador para semi final
        promedio_semifinal = puntaje_promedio(part, 4)
        print('El puntaje promedio por jugador para esta ronda es de: ', promedio_semifinal)
        print()
    if validar_enter('Aprete enter para jugar tercer y cuarto puesto: '):
        print('\n TERCER Y CUARTO PUESTO')
        print('~' * 17)
        # Ordenamos el vector part acomodando los ganadores al principio al igual que en las otras rondas
        ordenar_ganadores(part, 2)
        # Cargamos el puntaje para tercer y cuarto
        # Se juega el tercer y cuarto puesto
        jugar(part, 0)
        # SE muestra el cruce y el ganador del t puesto y final
        #     cargar_puntaje(part)ercer y cuarto puesto
        write_partidos(part, 0)
    if validar_enter('Aprete enter para jugar la Gran Final: '):
        print('\nLA GRAN FINAL ')
        print('~' * 17)
        # Se juega la gran final
        jugar(part, 1)
        # Se muestran el cruce y el campeon
        write_partidos(part, 1)
        print()
        # Mostramos el podio de ganadores e incrementamos el ranking
        write_podio_incremento_ranking(part)
        # Ordenamos la variable part por ranking
        ordenar_ranking(part)
        # Mostramos la variable part ordenada por ranking
        print()
        print('Lista de Participantes con Rankings Acutualizados')
        write1(part)


# Scrip principal
if __name__ == '__main__':
    test()
