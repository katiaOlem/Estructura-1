
#3. Crear un programa en python que muestre la estructura de la definición, llenado y despliegue de resultados en donde describan la funcionalidad de una lista circular


#Las clase Node es igual que la de la singly linked list. Por su parte la clase CircularLinkedList se diferencia de SinglyLinkedList en que, durante la inicialización, el primer nodo se apunta al  siguiente

class Nodo:
    def __init__(self, dato):
        self.date = dato 
        self.sig = None 

    def obtenerLista(self):
        return self.date

#Class de la lista circular
class CircularLinkedList:
    def __init__(self): 
        self.start = None 
        self.end = None 

#Se verificara que la lista este vacia


    def Vacia(self):
        if self.start == None: 
            return True
#se Insertara el primer nodo si la lista esta vacia, de no ser asi pasa a ser el primer nodo y el ultimo
    def  insert_at_start(self, dato):
        nuevo_nodo = Nodo(dato) 
        if self.Vacia() == True: 
            self.start = self.end = nuevo_nodo 
            self.end.sig = self.start 
        else: 
            self.end.sig = nuevo_nodo 
            nuevo_nodo.sig = self.stard 
            self.start = nuevo_nodo 


#se Insertara el ultimo nodo si la lista esta vacia, de no ser asi pasa a ser otro nodo nuevo
    def insert_at_end(self, dato):
        nuevo_nodo = Nodo(dato) 
        if self.Vacia() == True: 
            self.start = self.end = nuevo_nodo 
            self.end.sig = self.start 
        else: 
            self.end.sig = nuevo_nodo 
            self.end = nuevo_nodo 
            self.end.sig = self.start 

#Se imprimira la lista con los elementos ya recorridos
    def imprimir_lista(self):  
        if self.Vacia() == True:
            print("Su lista esta Vacia")
        else:
            n = self.start 
            print("Lista= ")
            while True: 
                print(n.obtenerLista()) 
                if n == self.end: 
                    break
                else:
                    n = n.sig 

objeto = CircularLinkedList ()

agregar = int(input("Agregue cantidad de la lista=  ")) 
for i in range (agregar): 
    numero = int(input("Agregue número= ) "+str(i+1)+"=> "))
    objeto.insertar_final(numero) 
objeto.imprimir_lista() 
if input("Desea agregar un número al inicio de la lista (si/no)= ").lower() == "si": 
    numero = int(input("número= ")) 
    objeto.insert_at_start(numero) 
    objeto.imprimir_lista() 

if input("Desea agregar un número al final de la lista (si/no)= ").lower() == "si":
    numero = int(input("Agregar número= ")) 
    objeto.insert_at_end(numero) 
    objeto.imprimir_lista() 
    