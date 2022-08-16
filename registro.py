class Participante:
    def __init__(self, nom, cont, rank, punt = 0, elm = 0):
        self.nombre = nom
        self.continente = cont
        self.ranking = rank
        self.puntaje = punt
        self.eliminado = elm


def write(part):
        print('\nNombre: ', part.nombre, end= '')
        print('\nContinente: ', part.continente, end= '')
        print('\nRanking: ', part.ranking, end= '')
        print()


# Funcion para mostrar los cruces de las rondas y los ganadores de cada ronda
def write_partidos(part, partidos):
    if partidos != 0 and partidos != 1:
        for i in range(partidos):
            j = partidos*2-1-i
            print(part[i].nombre, ' VS ', part[j].nombre)
        print('Los Ganadores de esta ronda son: ')
        for k in range(len(part)):
            if part[k].eliminado == 0:
                print(part[k].nombre)
    else:
        if partidos == 1:
            print(part[0].nombre, ' VS ', part[1].nombre)
            print('El Gran Campeon es: ')
            if part[0].eliminado == 0:
                print(part[0].nombre, '!!!!!!!!')
            else:
                print(part[1].nombre, '!!!!!!!!')
        else:
            print(part[2].nombre, ' VS ', part[3].nombre)
            print('El tercer puesto es para: ')
            if part[2].eliminado == 0:
                print(part[2].nombre, '!!!!!!!!')
            else:
                print(part[3].nombre, '!!!!!!!!')


# Funcion para Mostrar el Podio de ganadores y aumentar el ranking
def write_podio_incremento_ranking(part):
    print('PODIO DE GANADORES')
    print('Primer puesto: ')
    if part[0].eliminado == 0:
        write(part[0])
        part[0].ranking += 25
        print('\nSegundo puesto: ')
        write(part[1])
        part[1].ranking += 15
    else:
        write(part[1])
        part[1].ranking += 25
        print('\nSegundo puesto: ')
        write(part[0])
        part[0].ranking += 15
    print('\nTercer puesto: ')
    if part[2].eliminado == 0:
        write(part[2])
        part[2].ranking += 5
    else:
        write(part[3])
        part[3].ranking += 5


def write1(part):
    for i in range(16):
     s = '{:<20}'.format('Nombre: ' + part[i].nombre)
     s += '{:<15}'.format('Continente: ' + str(part[i].continente))
     s += '{:<15}'.format('Ranking: ' + str(part[i].ranking))
     print(s)
