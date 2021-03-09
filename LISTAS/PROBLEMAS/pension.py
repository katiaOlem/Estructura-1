#LISTA SIMPLE
#Juan tiene un nueva Pensión de Autos en la Avenida Juárez por lo cual quiere llevar el control de todo un día. Realiza un programa en el que:
#Se ingresen cuántos autos se quedaron guardados toda la noche
#Se ingresen las placas de cada Auto
#Cuando llegue el primer auto la persona confirme 
#Se ingresen los datos del primer Auto
#Que cada que llegue un Auto la persona diga qué lugar está disponible e Ingrese los Datos del auto
#Por ultimo agregar el último Auto que llega 
#Imprimir el total de Autos que se quedaron


class Auto:  
    def __init__(self, dato):
        self.elemento = dato 
        self.sig = None 

class Pension: 
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

    def insertar_auto(self, lugar, dato): 
        auto = self.inicio_auto

        while auto is not None: 
            if auto.elemento == lugar: 
                break
            auto = auto.sig 
        if auto is None: 
            print("**Auto no Registrado**")
        else:
            nuevo_auto = Auto(dato) 
            nuevo_auto.sig = auto.sig 
            auto.sig = nuevo_auto 

    def imprimir_lista_autos(self):  
        if self.inicio_auto is None: 
            print("***Verifique no Existen autos Registrados***")
            return
        else:
            n = self.inicio_auto 
            print("**Autos en la Pensión=>** ")
            while n is not None:
                print(n.elemento)
                n = n.sig 
                
objeto = Pension() 

agregar = int(input("Total de Autos en el Estacionamiento=> ")) 
for i in range (agregar):
    numeroautos =input("Ingrese sus datos) "+str(i+1)+"=> ")
    objeto.insertar_ultimo_auto(numeroautos) 
objeto.imprimir_lista_autos() 

if input("Desea agregar el primer Auto (si/no): ").lower() == "si": 
    numeroautos = input("Ingrese Datos del Auto=> ")
    objeto.insertar_primer_auto(numeroautos) 
    objeto.imprimir_lista_autos() 


if input("Agregaras otro Auto (si/no): ").lower() == "si":
    numeroautos =input("Ingrese Datos del Auto=> ")
    lugar = input("Después de que Auto? =>")
    objeto.insertar_auto(lugar, numeroautos)
    objeto.imprimir_lista_autos() 

if input("Agregaras otro Auto (si/no): ").lower() == "si":
    numeroautos =input("Ingrese Datos del Auto=> ")
    lugar = input("Después de que Auto? =>")
    objeto.insertar_auto(lugar, numeroautos)
    objeto.imprimir_lista_autos() 

if input("Es el ultimo auto a Registrar? (si/no): ").lower() == "si":
    numeroautos = input("Ingrese Datos del Auto=> ")
    objeto.insertar_ultimo_auto(numeroautos) 
    objeto.imprimir_lista_autos()  