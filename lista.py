#Un grupo de soldados se encuentran rodeados por una abrumadora fuerza enemiga. No hay esperanza de victoria sin refuerzos, pero sólo hay un caballo disponible para escapar. Los soldados hacen un pacto de sangre para determinar cuál de ellos va a escapar y pedir ayuda. Para ello, forman un círculo y van eligiendo un número de un sombrero. Iniciando con el soldado cuyo número de sombrero se eligió, se empieza a contar en el sentido de las manecillas del reloj alrededor del círculo. Cuando la cuenta llega a n, este soldado se retira del círculo y la cuenta vuelve a empezar con el soldado siguiente. El proceso continúa análogamente hasta que sólo quede un soldado, el cuál será el que va a tomar el caballo y escapar.

class Node(object):
         "" "Crear una clase de nodo" ""
    def __init__(self, data):
        self.data = data
        self.next = None
 
class create_circular_linked_list(object):
         "" "Crear una clase que cree una lista circular vinculada" ""
    
    def __init__(self):
        self.head = None
 
    def is_empty(self):
                 "" "Determine si la lista circular está vacía" ""
        return self.head is None
 
    def length(self):
                 "" "Obtenga la longitud de la lista circular" ""
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
                         # Si el siguiente nodo del nodo actual es el nodo principal, significa que este nodo es el nodo de cola
                         # Si no, mueva el puntero hacia atrás
            if cur.next == self.head:
                break
            else:
                cur = cur.next
        return count
 
    def add_first(self, data):
                 "" "Agregar un nodo en la cabeza" ""
        node = Node(data)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            cur = self.head
                         # Mueva el puntero al nodo de cola
            while cur.next is not self.head:
                cur = cur.next
                         # El nodo de cola apunta al nuevo nodo
            cur.next = node
                         # El nuevo nodo apunta al nodo principal original
            node.next = self.head
                         # Luego dele el título del nodo principal al nuevo nodo
            self.head = node
 
    def add_last(self, data):
                 "" "Agregar un nodo al final" ""
        node = Node(data)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            cur = self.head
                         # Mueve el puntero al final
            while cur.next is not self.head:
                cur = cur.next
                         # El nodo de cola apunta al nuevo nodo
            cur.next = node
                         # El nuevo nodo apunta al nodo principal
            node.next = self.head
 
    def insert_node(self, index, data):
                 "" "Insertar un nodo en una posición especificada" ""
        node = Node(data)
        if index < 0 or index > self.length():
                         print ("Posición de inserción incorrecta")
            return False
        elif index == 0:
            self.add_first(data)
        else:
            cur = self.head
                         pre = Ninguno # pre es el nodo anterior del nodo señalado por el puntero actual
            count = 0
                         # Mueva el puntero a la posición para insertar
            while count < index:
                pre = cur
                cur = cur.next
                count += 1
            pre.next = node
            node.next = cur
 
    def remove_node(self, data):
                 "" "Eliminar nodo especificado" ""
        if self.is_empty():
            return
                 # Si el nodo a eliminar es el nodo principal
        elif data == self.head.data:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head
            pre = None
                         # Mover a la posición del nodo que se va a eliminar
            while cur.data != data:
                pre = cur
                cur = cur.next
                         # Apunte el nodo precursor del nodo que se va a eliminar al nodo posterior, de modo que se omita el nodo central
            pre.next = cur.next
 
    def travel(self):
                 "" "Recorriendo la lista vinculada" ""
        if self.is_empty():
            return
        cur = self.head
        print(cur.data)
        while cur.next != self.head:
            cur = cur.next
            print(cur.data)
 
    def is_exist(self, data):
                 "" "Buscar si el nodo especificado existe" ""
        cur = self.head
        while cur is not None:
                         # Encuentra el nodo encontrado
            if cur.data == data:
                return True
                         # La cola ha sido encontrada
            elif cur.next == self.head:
                return False
            else:
                cur = cur.next
        return False