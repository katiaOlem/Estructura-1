#Lista Doblemente Enlazada
#Rubén es dueño de un Estacionamiento en San José, el se hace cargo de el de las 8 a.m. a las 10 a.m. & Después su Empleado, su estacionamiento por lo regular estaba lleno a partir de las 10 del día, y últimamente sus cuentas han disminuido, su empleado le dice que no llegan más autos como de costumbre por lo que él requiere de tu ayuda
#Realiza un programa en el que:
#Su empleado Ingrese el número de autos que llegaron de las 8 a.m. a las 10 a.m.
#Ingrese los datos de los autos
#Imprima el total de los autos
#Que el empleado confirme cuando llegue el primer auto después de las 10 a.m
#Ingrese los datos del primer auto
##Imprima el total de los autos
#Confirme cuando llegue otro auto
#Ingrese los datos del auto
#Ingrese en qué lugar lo estacionara
#Imprima el total de los autos
#Confirme cuando un auto se valla
#Confirme los datos del Auto
#Confirme si si modifico el lugar de los autos
#Confirme que se ha ido el último auto



class Auto:  
    def __init__(self, data):
        self.item = data
        self.nref = None
        self.pref = None

class Estacionamiento:  
    def __init__(self):
        self.start_node = None


        
    def insert_in_emptylist(self, data):
        if self.start_node is None:
            new_auto = Auto(data)
            self.start_node = new_auto
        else:
            print("list is not empty")
  

    def insert_at_start(self, data):
        if self.start_node is None:
            new_auto = Auto(data)
            self.start_node = new_auto
            print("node inserted")
            return
        new_auto = Auto(data)
        new_auto.nref = self.start_node
        self.start_node.pref = new_auto
        self.start_node = new_auto


    def insert_at_end(self, data):
        if self.start_node is None:
            new_auto = Auto(data)
            self.start_node = new_auto
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new_auto = Auto(data)
        n.nref = new_auto
        new_auto.pref = n



    def insert_after_item(self, x, data):
        if self.start_node is None:
            print("*****")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("****")
            else:
                new_auto = Auto(data)
                new_auto.pref = n
                new_auto.nref = n.nref
                if n.nref is not None:
                    n.nref.prev = new_auto
                n.nref = new_auto

    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("*****verifica los datos****")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("****verifica los datos****")
            else:
                new_auto = Auto(data)
                new_auto.nref = n
                new_auto.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_auto
                n.pref = new_auto


    def delete_at_start(self):
        if self.start_node is None:
            print("****verifica los datos****")
            return 
        if self.start_node.nref is None:
            self.start_node = None
            return
        self.start_node = self.start_node.nref
        self.start_prev = None;



    def delete_at_end(self):
        if self.start_node is None:
            print("****verifica los datos****")
            return 
        if self.start_node.nref is None:
            self.start_node = None
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        n.pref.nref = None



    def reverse_linked_list(self):
        if self.start_node is None:
            print("*****verifica los datos****")
            return 
        p = self.start_node
        q = p.nref
        p.nref = None
        p.pref = q
        while q is not None:
            q.pref = q.nref
            q.nref = p
            p = q
            q = q.pref
        self.start_node = p


    def imprimir_lista(self): 
        if self.start_node is None: 
            print("****verifica los datos****")
            return
        else:
            n = self.start_node 
            print("Autos en el Estacionamiento => ")
            while n is not None: 
                print(n.item)
                n = n.nref


objeto =Estacionamiento()

insertar = int(input("Ingrese el Total de Autos que estan=>"))
for i in range (insertar): 
    datosauto = input("Placas del auto # "+str(i+1)+" => ")
    objeto.insert_at_end(datosauto) 
objeto.imprimir_lista() 

if input("Desea Agregar otro Auto (si/no)= ").lower() == "si": 
    datosauto = input("Agregue #de Placas=> ")
    objeto.insert_at_start(datosauto) 
    objeto.imprimir_lista() 

if input("Desea agregar el auto al Final de la Fila (si/no)= ").lower() == "si": 
    datosauto = input("Ingrese #de placas del Auto ")
    objeto.insert_at_end(datosauto) 
    objeto.imprimir_lista() 

if input("Desea agregar el auto después de otro auto (si/no): ").lower() == "si": 
    datosauto = input("Ingrese # de Placas del auto => ") 
    despues = input("Después de que auto desea agregarlo? Recuerde Ingresar #de placas ")
    objeto.insert_after_item(despues, datosauto) 
    objeto.imprimir_lista() 


if input("Desea agregar el auto antes de otro auto (si/no): ").lower() == "si": 
    datosauto = input(" Ingrese # de Placas del auto => ")
    antes = input("Antes de que auto desea agregarlo? Recuerde Ingresar #de placas ")
    objeto.insert_before_item(antes, datosauto) 
    objeto.imprimir_lista() 

if input("Se a ido el primer auto ? (si/no): ").lower() == "si": 
    objeto.delete_at_start() 

if input("Moviste los Autos? (si/no): ").lower() == "si": 
    objeto.reverse_linked_list() 
    objeto.imprimir_lista()  

if input("Se a ido el Último auto ? (si/no): ").lower() == "si": 
    objeto.delete_at_end() 
    objeto.imprimir_lista() 
