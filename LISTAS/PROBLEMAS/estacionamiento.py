#Juan tiene un nuevo Estacionamiento en la Avenida Juarez por lo cual quiere llevar el control de todo un dia, Realiza un programa en el que:
#Se ingresen cuántos autos se quedaron guardados toda la noche
#Se ingresen las placas de cada Auto
#Cuando llegue el primer auto la persona confirme para tener el control de la hora en que se empieza a Ocupar el Estacionamiento
#Se ingresen los datos del primer Auto
#Que cada que llegue un Auto la persona diga que lugar esta disponoble dentras, o delante de que auto
#Ir eliminando los autos que se retiran
#Por ultimo agregar el ultimo Auto que llega 
#Imprimir el total de Autos que se quedaron

class Auto:  
    def __init__(self, dato):
        self.elemento = dato 
        self.sig = None 

class Estacionamiento: 
    def __init__(self): 
        self.inicio_auto = None 

    def insertar_primer_auto(self, dato):
        nuevo_auto = Auto(dato) 
        nuevo_auto.sig = self.inicio_auto
        self.inicio_auto= nuevo_auto

    def insertar_ultimo_auto(self, dato): 
        nuevo_auto = Auto(dato) 
        if self.inicio_auto is None: 
            self.inicio_auto = nuevo_auto 
            return
        n = self.inicio_auto 
        while n.sig is not None: 
            n= n.sig 
        n.sig = nuevo_auto; 

    def insertar_despues_auto(self, x, dato): 
        n = self.inicio_auto 

        while n is not None: 
            if n.elemento == x: 
                break
            n = n.sig 
        if n is None:
            print("***Verifique nuevamente ese lugar esta Ocupado***")
        else:
            nuevo_auto = Auto(dato) 
            nuevo_auto.sig = n.sig 
            n.sig = nuevo_auto 

    def insertar__auto_posicion (self, index, dato): 
        if index == 1: #
            nuevo_auto = Auto(dato) 
            nuevo_auto.sig = self.inicio_auto
            self.inicio_auto = nuevo_auto
        i = 1 
        n = self.inicio_auto
        while i < index -1 and n is not None: 
            n = n.sig 
            i = i+1 
        if n is None: 
            print("***Verifique nuevamente ese lugar esta Ocupado***")
        else: 
            nuevo_auto = Auto(dato) 
            nuevo_auto.sig = n.sig 
            n.sig = nuevo_auto 

    def imprimir_lista_autos(self):  
        if self.inicio_auto is None: 
            print("***Verifique no Existen autos Registrados***")
            return
        else:
            n = self.inicio_auto 
            print("**Autos en el Estacionamiento=>** ")
            while n is not None:
                print(n.elemento)
                n = n.sig 
                
objeto = Estacionamiento() 

agregar = int(input("Total de Autos en el Estacionamiento=> ")) 
for i in range (agregar):
    numeroautos = int(input("Ingrese sus datos) "+str(i+1)+"=> "))
    objeto.insertar_ultimo_auto(numeroautos) 
objeto.imprimir_lista_autos() 

if input("Desea agregar el primer Auto (si/no): ").lower() == "si": 
    numeroautos = int(input("Ingrese Datos del Auto=> ")) 
    objeto.insertar_primer_auto(numeroautos) 
    objeto.imprimir_lista_autos() 


if input("Agregaras Otro Auto (si/no): ").lower() == "si":
    numeroautos = int(input("Ingrese datos del auto=> ")) 
    despues = int(input("Despues de que Auto =>")) 
    objeto.insertar_despues_auto(despues, numeroautos) 
    objeto.imprimir_lista_autos() 

if input("Agregaras otro Auto (si/no): ").lower() == "si":
    numero = int(input("Ingrese Datos del Auto=> ")) 
    indice = int(input("Despues de que Auto? =>")) 
    objeto.insertar_auto_posicion(indice, numero) 
    objeto.imprimir_lista() 


if input("Es el ultimo auto a Reguustar? (si/no): ").lower() == "si":
    numeroautos = int(input("Ingrese Datos del Auto=> ")) 
    objeto.insertar_final(numeroautos) 
    objeto.imprimir_lista()  


