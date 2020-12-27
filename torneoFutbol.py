'''PROGRAMA DE REGISTRO DE PARTIDOS DE FUTBOL
Se solicita crear un programa que realice lo siguiente
- registrar equipos
- registrar árbitros
- registrar resultados
- registrar jugadores
Imprimir una tabla de posiciones
Imprimir Goleadores
Los equipos, arbitros y jugadores deberan tener un
contador de partidos acumulados
(ya sean diriguidos o jugados)
El objetivo es usar clases, herencias y crear un
programa que las use'''


# CREAREMOS UNA CLASE PARA REGISTRAR LOS EQUIPOS
import  operator
class Equipos:
    codigoEquipo = ""  # no se repite -- clave primaria
    nombreEquipo = ""
    anioCreacion = 0
    partidosJugadosEQ = 0
    puntosAcumuladosEQ = 0

    def __init__(self, codigo, nombre, anio):  # este es el constructor
        self.codigoEquipo = codigo  # inicializa valores
        self.nombreEquipo = nombre
        self.anioCreacion = anio

    def conteoPartidosEq(self):
        self.partidosJugadosEQ = self.partidosJugadosEQ + 1

    def conteoGanados(self,puntos):
        self.puntosAcumuladosEQ = self.puntosAcumuladosEQ + puntos





# PERSONAS, tenemos que crear jugadores y árbitros
# ambos son personas,por lo que habra herencia
# crearemos una clase PERSONAS

class Personas:
    codigoPersona = ""
    nombrePersona = ""
    nacionalidad = ""

    def __init__(self, codigo, nombre, pais):  # este es el constructor
        self.codigoPersona = codigo  # no se repite -- clave primaria
        self.nombrePersona = nombre
        self.nacionalidad = pais


# crearemos una clase arbitro

class Arbitro(Personas):
    tipoArbitros = ""
    partidosDirigidos = 0

    def __init__(self, codigo, nombre, pais, tipo):  # este es el constructor
        super().__init__(codigo, nombre, pais)  # inicializa valores
        self.tipoArbitro = tipo

    def conteoPartidos(self):
        self.partidosDirigidos = self.partidosDirigidos + 3


# crearemos una clase jugadores

class Jugadores(Personas):
    equipoActual = ""
    partidosJugados = 0
    golesMarcados = 0
    puntosMiEquipo = 0

    def __init__(self, codigo, nombre, pais, equipo):  # este es el constructor
        super().__init__(codigo, nombre, pais)  # inicializa valores
        self.equipoActual = equipo

    def conteoPartidos(self):
        self.partidosJugados = self.partidosJugados + 1

    def conteoGoles(self,numgoles):
        self.golesMarcados = self.golesMarcados + numgoles

    def puntosdemiequipo(self,puntos):
        self.puntosMiEquipo = self.puntosMiEquipo + puntos

# RegistroPartidos
# Ahora registraremos los partidos

class Partidos():
    torneo = ""
    equipo1 = ""  # hace referencia al codigo del equipo
    marcador1 = 0
    equipo2 = ""  # hace referencia al codigo del equipo
    marcador2 = 0
    arbitro = ""  # hace referencia al codigo del arbitro

    def __init__(self, tor, equi1, equi2, mar1, mar2, arbi):
        self.torneo = tor
        self.equipo1 = equi1
        self.marcador1 = mar1
        self.equipo2 = equi2
        self.marcador2 = mar2
        self.arbitro = arbi


    # Crearemos la clase principal

class Principal():
    ListaEquipos = list()
    ListaJugadores = list()
    ListaArbitros = list()
    ListaPartidos = list()
    istaGoleadores = list()
    diccionarioGolea = {}
    diccionarioEq = {}
    listaCodEqui=[]
    listaNomEqui=[]
    listaCodPers=[]
    listaNom=[]
    listaCodArb = []
    listaNomArb = []


    # NO LE DEFINO UN CONSTRUCTOR, ENTONCES EL CONSTRUCTOR ES POR DEFECTO
    # PERO DICHO CONSTRUCTOR NO HACE NADA

    def main(self):

        while True:
            print("Bienvenido al programa de registro de resultados, seleccione la opción que desee")
            print("1.-Ingresar Equipos: ")
            print("2.-Ingresar Jugadores: ")
            print("3.-Ingresar Arbitros: ")
            print("4.-Ingresar Partidos: ")
            print("5.-Relación  de Goleadores: ")
            print("6.-Posiciones: ")
            print("7.-Salir")
            opcion = int(input("Ingrese un número del 1 al 7: "))

            if opcion == 7:
                print("Adios ..............")
                break

            elif opcion == 1:

                print("vamos a ingresar datos de los Equipos")
                codigo = input("Ingrese codigo: ")
                while codigo in self.listaCodEqui:
                    codigo = input("Ingrese codigo: ")
                self.listaCodEqui.append(codigo)
                nombre = input("Ingrese nombre: ")
                while nombre  in self.listaNomEqui:
                    nombre = input("Ingrese nombre: ")
                self.listaNomEqui.append(nombre)
                anioCreacion = input("Ingrese el año de creación: ")
                eq = Equipos(codigo, nombre, anioCreacion)  # creamos un objeto o una instancia de equipos eq
                self.ListaEquipos.append(eq)

                print("-----EQUIPO INGRESADOS------")
                for x in self.ListaEquipos:
                    print(x.nombreEquipo)
                print("-----FIN------")
################################################# crea jugadores 3#############################################
            elif opcion == 2:
                print("vamos a ingresar datos de los jugadores")
                codigoPersona = input("Ingrese codigo: ")
                while codigoPersona in self.listaCodPers:
                    codigoPersona = input("Ingrese codigo: ")
                self.listaCodPers.append(codigoPersona)
                nombrePersona = input("Ingrese persona: ")
                while nombrePersona in self.listaNom:
                    nombrePersona = input("Ingrese codigo: ")
                self.listaNom.append(nombrePersona)
                pais = input("Ingrese pais: ")

                equipo = input("Ingrese nombre Equipo: ")  # tendría que hacer una validación si existe el equipo
                while equipo not in self.listaNomEqui:
                    equipo = input("Ingrese nombre Equipo: ")

                jugador = Jugadores(codigoPersona, nombrePersona, pais,equipo)  # creamos un objeto o una instancia de la clase de jugadores

                self.ListaJugadores.append(jugador)

                print("-----JUGADORES INGRESADOS------")
                for x in self.ListaJugadores:
                    print(x.nombrePersona,x.equipoActual)
                print("-----FIN------")
######################################################### crea arbitros #############################################
            elif opcion == 3:
                print("vamos a ingresar datos de los árbitros")
                codigoPersona = input("Ingrese codigo: ")
                while codigoPersona in self.listaCodArb:
                    codigoPersona = input("Ingrese codigo: ")
                self.listaCodArb.append(codigoPersona)
                nombrePersona = input("Ingrese persona: ")
                pais = input("Ingrese pais: ")
                tipo = input("Ingrese tipo: ")
                arbitro = Arbitro(codigoPersona, nombrePersona, pais, tipo)  # creamos un objeto o una instancia de la clase de arbitro

                self.ListaArbitros.append(arbitro)

                print("-----ARBITROS INGRESADOS------")
                for x in self.ListaArbitros:
                    print(x.nombrePersona)
                print("-----FIN------")
############################################################### ingreso partidos ##################################################
            elif opcion == 4:
                print("vamos a ingresar datos de los partidos jugados")
                tor = input("Ingrese el torneo: ")

                equi1 = input("Ingrese el  equipo 1: ")
                while equi1 not in self.listaNomEqui:
                    equi1 = input("Ingrese el  equipo 1: ")

                for a in self.ListaEquipos:
                    if equi1 == a.nombreEquipo:
                        a.conteoPartidosEq()

#======================================ingresando los goles marcados=======================================================

                mar1 = int(input(
                    "Ingrese los goles marcados por el el equipo 1: "))  # tendría que hacer una validación si existe el tipo
                suma=0
                while mar1>suma:
                    print("-----JUGADORES INGRESADOS------")
                    for x in self.ListaJugadores:
                        print(x.nombrePersona, x.equipoActual)
                    print("-----FIN------")
                    JugGol = input("ingrese nombre q anotaron gol  del equipo 1: ")




                    for a in self.ListaJugadores:
                        if JugGol == a.nombrePersona:

                            a.conteoPartidos()
                            numGOl = int(input("ingrese numero de goles: "))
                            suma=suma+numGOl

                            a.conteoGoles(numGOl)


                equi2 = input("Ingrese el equipo 2: ")
                while equi2==equi1:
                    equi2 = input("Ingrese el equipo 2: ")
                while equi2 not in self.listaNomEqui:
                    equi2 = input("Ingrese el  equipo 2: ")

                for b in self.ListaEquipos:
                    if equi2 == b.nombreEquipo:
                        b.conteoPartidosEq()



                mar2 = int(input("Ingrese los goles marcados por el el equipo 2: "))


                suma2=0
                while mar2 > suma2:# seguira ingresando jugadores y goles hasta q sea igual a la cantidad de goles del equipo

                    print("-----JUGADORES INGRESADOS------")
                    for x in self.ListaJugadores:
                        print(x.nombrePersona, x.equipoActual)
                    print("-----FIN------")

                    JugGol2 = input("ingrese nombre q anotaron gol  del equipo 2: ")

                    for c in self.ListaJugadores:
                        if JugGol2 == c.nombrePersona:
                            c.conteoPartidos()
                            numGOl = int(input("ingrese numero de goles: "))
                            suma2 = suma2+ numGOl
                            c.conteoGoles(numGOl)


    #===============================sumando puntos y  los goles =====================================================

                if mar1 < mar2:
                    for w in self.ListaEquipos:
                        if equi2 == w.nombreEquipo:
                            w.conteoGanados(3)

                    for w in self.ListaEquipos:
                        if equi1 == w.nombreEquipo:
                            w.conteoGanados(0)



                if mar1 > mar2:
                    for a in self.ListaEquipos:
                        if equi1 == a.nombreEquipo:
                            a.conteoGanados(3)
                    for w in self.ListaEquipos:
                        if equi2 == w.nombreEquipo:
                            w.conteoGanados(0)

                if mar1 == mar2:
                    for a in self.ListaEquipos:
                        if equi1 == a.nombreEquipo:
                            a.conteoGanados(1)
                    for w in self.ListaEquipos:
                        if equi2 == w.nombreEquipo:
                            w.conteoGanados(1)

#=====================================================ingreso del arbitro=======================================
                nomarbitro = input("Ingrese  arbitro: ")
                for arb in self.ListaArbitros:
                    if nomarbitro == arb.nombrePersona:
                        print(arb.nacionalidad)
                        arb.conteoPartidos()

                partido = Partidos(tor, equi1, equi2, mar1, mar2,
                                   nomarbitro)  # creamos un objeto o una instancia de la clase de arbitro
                self.ListaPartidos.append(partido)

                print("-----ARBITROS INGRESADOS------")
                for x in self.ListaArbitros:
                    print(x.nombrePersona)
                print("-----FIN------")


 #-----------------------------------------reporte por partido ------------------------------------------
                print("-----PARTIDOS JUGADOS INGRESADOS------")
                for x in self.ListaPartidos:
                    print(x.torneo)
                    print(x.equipo1, "vs", x.equipo2)
                    print("   ", x.marcador1, " - ", x.marcador2)

                for y in self.ListaEquipos:
                    print("nombre", y.nombreEquipo, "partidos jugados", y.partidosJugadosEQ)

#-------------------------llenando los diccionarios---------------------------------------------------------
                for y in self.ListaJugadores:
                    if y.golesMarcados >= 0:
                        self.diccionarioGolea[y.nombrePersona] = y.golesMarcados

                for e in self.ListaEquipos:
                    if e.puntosAcumuladosEQ >= 0:
                        self.diccionarioEq[e.nombreEquipo] = e.puntosAcumuladosEQ


#----------------------------------ordenando de mayor a menor ---------------------------------------------
                print("-----TABLA DE POSICIONES------")
                EquipoOrde=sorted(self.diccionarioEq.items(),key=operator.itemgetter(1),reverse=True)
                for self.name in enumerate(EquipoOrde):
                    print(self.name[1][0],'PUNTOS',self.diccionarioEq[self.name[1][0]] )

                print("-----TABLA DE GOLEADORES------")
                GOleadoresOrde = sorted(self.diccionarioGolea.items(), key=operator.itemgetter(1), reverse=True)
                for self.name in enumerate(GOleadoresOrde):
                    print(self.name[1][0], 'GOLES', self.diccionarioGolea[self.name[1][0]])



                print("-----FIN------")


# Ejecutamos el programa
# para esto tenemos que crear un objeto de la clase principal y llamar al metodo main

p1=Principal()
p1.main()