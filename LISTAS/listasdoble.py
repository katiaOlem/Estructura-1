#2. Crear un programa en python que muestre la estructura de la definición, llenado y despliegue de resultados en donde describan la funcionalidad de una lista doblemente enlazada

#primero creamos una clase para el nodo único en la lista.
#creamos una Nodeclase con tres variables miembro: item, nref, y pref. La itemvariable almacenará los datos reales para el nodo. Las nreftiendas de la referencia a la siguiente nodo, mientras que prefalmacena la referencia al nodo anterior en la lista doblemente enlazada.

class Node:  
    def __init__(self, data):
        self.item = data
        self.nref = None
        self.pref = None

#crear la DoublyLinkedListclase, que contiene diferentes funciones relacionadas con la lista de enlaces dobles.

class DoublyLinkedList:  
    def __init__(self):
        self.start_node = None

#insertar un elemento en la lista vacía
        
    def insert_in_emptylist(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("list is not empty")
  
  # insertar un elemento al comienzo de la lista doblemente enlazada, primero debemos verificar si la lista está vacía o no. Si la lista está vacía, simplemente podemos usar la lógica definida en insert_in_emptylist()el elemento para insertar el elemento, ya que en una lista vacía, el primer elemento siempre está al principio.
#De lo contrario, si la lista no está vacía, debemos realizar tres operaciones:
#Para el nuevo nodo, la referencia al siguiente nodo se establecerá en self.start_node.
#Para que la self.start_nodereferencia al nodo anterior se establezca en el nodo recién insertado.
#Finalmente, self.start_nodese convertirá en el nodo recién insertado.

    def insert_at_start(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            print("node inserted")
            return
        new_node = Node(data)
        new_node.nref = self.start_node
        self.start_node.pref = new_node
        self.start_node = new_node

#Insertar un elemento al final de la lista doblemente enlazada es algo similar a insertar un elemento al comienzo. Al principio, necesitamos verificar si la lista está vacía. Si la lista está vacía, simplemente podemos usar el insert_in_emptylist()método para insertar el elemento. Si la lista ya contiene algún elemento, atravesaremos la lista hasta que la referencia al siguiente nodo se convierta en None. Cuando la siguiente referencia de nodo se convierte None, significa que el nodo actual es el último nodo.
#La referencia anterior para el nuevo nodo se establece en el último nodo, y la siguiente referencia para el último nodo se establece en el nodo recién insertado

    def insert_at_end(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new_node = Node(data)
        n.nref = new_node
        new_node.pref = n


#Para insertar un elemento después de otro, primero verificamos si la lista está vacía o no. Si la lista está realmente vacía, simplemente mostramos el mensaje de que la "lista está vacía".
#De lo contrario, iteramos a través de todos los nodos en la lista doblemente enlazada. En caso de que no se encuentre el nodo después del cual deseamos insertar el nuevo nodo, le mostraremos al usuario el mensaje de que no se encontró el elemento. De lo contrario, si se encuentra el nodo, se selecciona y realizamos cuatro operaciones:
#Establezca la referencia anterior del nodo recién insertado en el nodo seleccionado.
#Establezca la siguiente referencia del nodo recién insertado en la siguiente referencia del seleccionado.
#Si el nodo seleccionado no es el último nodo, establezca la referencia anterior del siguiente nodo después del nodo seleccionado al nodo recién agregado.
#Finalmente, establezca la siguiente referencia del nodo seleccionado al nodo recién insertado.
    def insert_after_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.pref = n
                new_node.nref = n.nref
                if n.nref is not None:
                    n.nref.prev = new_node
                n.nref = new_node
    
#Para insertar un elemento antes de otro, primero verificamos si la lista está vacía o no. Si la lista está realmente vacía, simplemente mostramos el mensaje de que la "lista está vacía".
#De lo contrario, iteramos a través de todos los nodos en la lista doblemente enlazada. En caso de que no se encuentre el nodo antes del cual queremos insertar el nuevo nodo, le mostraremos al usuario el mensaje de que no se encontró el elemento. De lo contrario, si se encuentra el nodo, se selecciona y realizamos cuatro operaciones:
#Establezca la siguiente referencia del nodo recién insertado en el nodo seleccionado.
#Establezca la referencia anterior del nodo recién insertado en la referencia anterior del seleccionado.
#Establezca la siguiente referencia del nodo anterior al nodo seleccionado, al nodo recién agregado.
#Finalmente, configure la referencia anterior del nodo seleccionado al nodo recién insertado.
    
    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                n.pref = new_node



#La forma más fácil de eliminar un elemento de una lista doblemente enlazada es desde el principio. Para hacerlo, todo lo que tiene que hacer es establecer el valor del nodo de inicio en el siguiente nodo y luego establecer la referencia anterior del nodo de inicio en None. Sin embargo antes de que hagamos eso necesitamos realizar dos verificaciones. Primero, necesitamos ver si la lista está vacía. Y luego tenemos que ver si la lista contiene solo un elemento o no. Si la lista contiene solo un elemento, simplemente podemos establecer el nodo de inicio en None. La siguiente secuencia de comandos se puede utilizar para eliminar elementos desde el inicio de la lista con doble enlace.

    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        if self.start_node.nref is None:
            self.start_node = None
            return
        self.start_node = self.start_node.nref
        self.start_prev = None;


#Para eliminar el elemento del final, nuevamente verificamos si la lista está vacía o si la lista contiene un solo elemento. Si la lista contiene un solo elemento, todo lo que tenemos que hacer es establecer el nodo de inicio en None. Si la lista tiene más de un elemento, recorreremos la lista hasta llegar al último nodo. Una vez que llegamos al último nodo, establecemos la siguiente referencia del nodo anterior al último nodo, a la Noneque en realidad elimina el último nodo.
    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        if self.start_node.nref is None:
            self.start_node = None
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        n.pref.nref = None

#Para revertir una lista doblemente enlazada, básicamente tiene que realizar las siguientes operaciones:
#La siguiente referencia del nodo de inicio debe establecerse en ninguno porque el primer nodo se convertirá en el último nodo en la lista invertida.
#La referencia anterior del último nodo debe establecerse en, Noneya que el último nodo se convertirá en el nodo anterior.
#Las siguientes referencias de los nodos (excepto el primero y el último nodo) en la lista original deben intercambiarse con las referencias anteriores.

    def reverse_linked_list(self):
        if self.start_node is None:
            print("The list has no element to delete")
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

 ##Imprimir la Lista Doble, verificando si la lista esta vacia dira que No existen los elementos en la Lista, Imprimira cada elemento de la LISTA que se alamaceno
    
    def imprimir_lista(self): 
        if self.start_node is None: 
            print("The list has no element=")
            return
        else:
            n = self.start_node 
            print("List= ")
            while n is not None: 
                print(n.item)
                n = n.nref


objeto =DoublyLinkedList()

insertar = int(input("Agregue cantidad de la lista= "))
for i in range (insertar): 
    numero = int(input("Número) "+str(i+1)+"=> "))
    objeto.insert_at_end(numero) 
objeto.imprimir_lista() 

if input("Desea agregar un número al inicio de la lista (si/no)= ").lower() == "si": 
    numero = int(input("Agregue número= ")) 
    objeto.insert_at_start(numero) 
    objeto.imprimir_lista() 

if input("Desea agregar un número al final de la lista (si/no)= ").lower() == "si": 
    numero = int(input("Agregue número= ")) 
    objeto.insert_at_end(numero) 
    objeto.imprimir_lista() 

if input("Desea agregar un número después de otro numero (si/no): ").lower() == "si": 
    numero = int(input("Cúal es el número que desea agregar? = ")) 
    despues = int(input("Después de que número desea agregarlo? ")) 
    objeto.insert_after_item(despues, numero) 
    objeto.imprimir_lista() 


if input("Desea agregar un número antes de otro número (si/no): ").lower() == "si": 
    numero = int(input("Cúal es el número que desea agregar? = ")) 
    antes = int(input("Antes de que número desea agregarlo? ")) 
    objeto.insert_before_item(antes, numero) 
    objeto.imprimir_lista() 

if input("Desea ver al reverso su lista doble (si/no): ").lower() == "si": 
  objeto.reverse_linked_list()
  objeto.imprimir_lista()

  if input("Desea eliminar el primer elemento de la Lista(si/no): ").lower() == "si": 
    objeto.delete_at_start() 
    objeto.imprimir_lista() 
  
  if input("Desea eliminar el último elemento de la Lista(si/no): ").lower() == "si": 
    objeto.delete_at_end() 
    objeto.imprimir_lista() 
