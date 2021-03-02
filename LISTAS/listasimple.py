# Crear un programa en python que muestre la estructura de la definición, llenado y despliegue de resultados en donde describan la funcionalidad de una lista simple.


#En primer lugar, definimos una clase que va a ser la clase Node. Los objetos de esta contendrán sus propios datos y un enlace al siguiente elemento de la lista

class Nodo:  #Class
    def __init__(self, dato):
        self.elemento = dato #Se almacenan los datos
        self.sig = None 

class ListaSimple: #Class de la lista, donde se agragara el primer Nodo de la lista, se agregara el dato del Inicio de la Lista , con su variable y la variable sig, ayudara a seleccionar desde el nodo principal y llamaremos al elemento nuevo nodo
    def __init__(self): 
        self.inicio_nodo = None #Primer nodo 

    def insertar_inicio(self, dato): #Agrega
        nuevo_nodo = Nodo(dato) #variable 
        nuevo_nodo.sig = self.inicio_nodo #sig
        self.inicio_nodo= nuevo_nodo #su elemento

#Se agregara otro Nodo al Final de la Lista llamando a la variable del dato y con condicionales para que si en la lista el ultimo dato es NULL se agregara el nuevo elemento y de no ser asi, se agragara en el siguiente elemnto hasta encontrar el valor NULL
    def insertar_final(self, dato): #Agrega el dato al Final de la lista
        nuevo_nodo = Nodo(dato) #Variable para la creacion de los nodos
        if self.inicio_nodo is None: #Conditional 
            self.inicio_nodo = nuevo_nodo
            return
        nulo = self.inicio_nodo #No Aceptado
        while nulo.sig is not None: #se agarega al siguiente
            nulo= nulo.sig 
        nulo.sig = nuevo_nodo; 
  


  #Agregar un elemento despues de otro, Si el elemento es NUll el elemento se agregara y se recorreran todos los nodos, si el elemento es el mismo al ya asignado solo se queda asi, de no ser recorre toda la lista y este sera el nuevo elemnto insertado

    def insertar_despues_elemento(self, ele, dato): 
        nulo = self.inicio_nodo 

        while nulo is not None: 
            if nulo.elemento == ele: 
                break
            nulo = nulo.sig 
        if nulo is None: 
            print("*Numero No encontrado*")
        else:
            nuevo_nodo = Nodo(dato) 
            nuevo_nodo.sig = nulo.sig 
            nulo.sig = nuevo_nodo 

    
  #Imprimir la Lista, verificando si la lista esta vacia dira que No existen los elementos en la Lista, Imprimira cada elemento de la LISTA que se alamaceno


    def imprimir_lista(self):  
        if self.inicio_nodo is None: 
            print("No tiene elementos")
            return
        else:
            nulo = self.inicio_nodo 
            print("Lista: ")
            while nulo is not None:
                print(nulo.elemento) 
                nulo = nulo.sig 
                
objeto = ListaSimple() #Objeto que llamara a la clase


# Se insertara la catidad de los elementos a Agregar en la Lista en este caso seran numeros, preguntara si quiere Agregar un nuemero al Inicio de la Lista asi como en el Final y si quiere despues de otro elemento agregado y se Imprimira la LISTA

insertar = int(input("Agregue la Cantidad Total de numeros que desea= ")) 
for i in range (insertar): 
    numero = int(input("Agregue número) "+str(i+1)+"  =>"))
    objeto.insertar_final(numero) 
objeto.imprimir_lista() 

if input("Desea agregar un número al inicio de la lista (s/n)= ").lower() == "s": 
    numero = int(input("Agregue número= ")) 
    objeto.insertar_inicio(numero) 
    objeto.imprimir_lista() 

if input("Desea agregar un número al final de la lista (s/n)= ").lower() == "s": 
    numero = int(input("Agregue número= ")) 
    objeto.insertar_final(numero) 
    objeto.imprimir_lista()  

if input("Desea agregar un número despues de otro numero (s/n): ").lower() == "s":
    numero = int(input("Agregue número = ")) 
    despues = int(input("Agregue número existente= ")) 
    objeto.insertar_despues_elemento(despues, numero) 
    objeto.imprimir_lista() 
