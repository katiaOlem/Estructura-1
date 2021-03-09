#En una escuela la maestra decidio hacer un juego, en total tenia 10 alumnos y el juego consistia  en que cada alumno era un número, debian responder una pregunta y si respondian mal eran eliminados, y los 5 que se quedaran ganarian un punto extra 
#Realiza un programa en que:
#Ingreses los 10 alumnos
#Ingrese numero de cada alumno
#se elimine al que responda mal
#Agregue los nombres de los 5 alumnos
#Se Impriman el total de alumnos ganadores


class Alumno: 
    def __init__(self, dato):
        self.dato = dato 
        self.sig = None 

 
class ListaCircular: 
    def __init__(self): 
        self.inicio_nodo = None 
    def lista_vacia(self): 
        return self.inicio_nodo is None 
 
    def insertar_nombre(self, dato): 
        nuevo_nodo = Alumno(dato) 
        if self.lista_vacia(): 
            self.inicio_nodo = nuevo_nodo 
            nuevo_nodo.sig = self.inicio_nodo 
        else:
            n = self.inicio_nodo 
            while n.sig is not self.inicio_nodo:
                n = n.sig 
            n.sig = nuevo_nodo 
            nuevo_nodo.sig = self.inicio_nodo 
            self.inicio_nodo = nuevo_nodo 
 
    def insertar_nombres(self, index, dato): 
        nuevo_nodo = Alumno(dato) 
        if index < 0 or index > self.contar_alumnos(): 
            print ("***Verifica Tus datos***")
        elif index == 0: 
            self.insertar_nombre(dato)
        else:
            n = self.inicio_nodo
            ant = None
            contador = 0
            while contador < index:
                ant = n 
                n = n.sig 
                contador += 1
            ant.sig = nuevo_nodo 
            nuevo_nodo.sig = n
 
    def insertar_nombrealumno(self, index, dato): 
        n = self.inicio_nodo

        while n is not None: 
            if n.dato == index: 
                break
            n = n.sig 
        if n is None: 
            print("**Verfica Datos**")
        else:
            nuevo_nodo = Alumno(dato) 
            nuevo_nodo.sig = n.sig 
            n.sig = nuevo_nodo
 
    def eliminarAlumno(self, dato):
        if self.lista_vacia(): 
            return
                 
        elif dato == self.inicio_nodo.dato:
            n = self.inicio_nodo
            while n.sig != self.inicio_nodo: 
                n = n.sig 
            n.sig = self.inicio_nodo.sig 
            self.inicio_nodo = self.inicio_nodo.sig 
        else: 
            n = self.inicio_nodo 
            ant = None
            while n.dato != dato:  
                ant = n
                n = n.sig
            ant.sig = n.sig
 

    def contar_alumnos(self):        
        if self.lista_vacia(): 
            return
        n = self.inicio_nodo 
        contador = 0 
        while n.sig != self.inicio_nodo: 
            n = n.sig 
            contador+=1 
        return contador+1 

    def imprimir_ganadores(self):
                 
        if self.lista_vacia(): 
            return
        n = self.inicio_nodo 
        print("Cuentas registradas:")
        print(n.dato)
        while n.sig != self.inicio_nodo: 
            n = n.sig 
            print(n.dato) 
  
 

objeto = ListaCircular()


agregar = int(input("Cuántos alumnos son=> ")) 
for i in range (agregar): 
    numero = int(input("Ingrese el # asignado a cada alumno "+str(i+1)+"=> "))
    objeto.insertar_nombre(numero) 
objeto.imprimir_ganadores() 


if input("Desea seleccionar quien es el primer Eliminado (si/no)=> ").lower() == "si": 
    al = int(input("Ingrese número del alumno eliminado => "))
    objeto.eliminarAlumno(al) 
    objeto.imprimir_ganadores() 

if input("Desea seleccionar quien es el segundo Eliminado (si/no)=> ").lower() == "si": 
    al = int(input("Ingrese número del alumno eliminado => "))
    objeto.eliminarAlumno(al) 
    objeto.imprimir_ganadores() 

if input("Desea seleccionar quien es el tercer Eliminado (si/no)=> ").lower() == "si": 
    al = int(input("Ingrese número del alumno eliminado => "))
    objeto.eliminarAlumno(al) 
    objeto.imprimir_ganadores() 

if input("Desea seleccionar quien es el cuarto Eliminado (si/no) => ").lower() == "si": 
    al = int(input("Ingrese número del alumno eliminado => "))
    objeto.eliminarAlumno(al) 
    objeto.imprimir_ganadores() 

if input("Desea seleccionar quien es el quinto Eliminado (SI/NO)=> ").lower() == "si": 
    al = int(input("Ingrese número del alumno eliminado =>   "))
    objeto.eliminarAlumno(al) 
    objeto.imprimir_ganadores() 

if input("Agregara el nombre del primer alumno ganador? (si/no)=> ").lower() == "si": 
    numero = input("Escriba el nombre del Alumno =>  ")
    objeto.insertar_nombre(numero) 
    objeto.imprimir_ganadores() 

if input("Agregara el nombre del segudo alumno ganador?(si/no)=> ").lower() == "si": 
    numero = input("Escriba el nombre del Alumno => ") 
    index = int(input("Ingrese el numero asignado")) 
    objeto.insertar_nombrealumno(index,numero) 
    objeto.imprimir_ganadores() 

if input("Agregara el nombre del tercer alumno ganador?(si/no)=> ").lower() == "si": 
    numero = input("Escriba el nombre del Alumno => ") 
    index = int(input("Ingrese el numero asignado")) 
    objeto.insertar_nombrealumno(index,numero) 
    objeto.imprimir_ganadores() 

if input("Agregara el nombre del cuarto alumno ganador?(si/no)=> ").lower() == "si": 
    numero = input("Escriba el nombre del Alumno => ") 
    index = int(input("Ingrese el numero asignado")) 
    objeto.insertar_nombrealumno(index,numero) 
    objeto.imprimir_ganadores() 

if input("Agregara el nombre del quinto alumno ganador?(si/no)=> ").lower() == "si":
    numero = int(input("Escriba el nombre del Alumno =>  "))
    objeto.insertar_nombres(numero) 
    objeto.imprimir_ganadores() 

