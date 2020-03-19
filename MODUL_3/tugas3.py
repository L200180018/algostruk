class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
class LinkedList: 
    def __init__(self): 
        self.head = None
#3a
    def cari(self, x): 
        current = self.head 
        while current != None: 
            if current.data == x: 
                return "True"
            current = current.next
        return "False"
#3b
    def tambahDepan(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node
#3c
    def tambahAkhir(self, data):
        if (self.head == None):
            self.head = Node(data)
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = Node(data)
        return self.head

#3d
    def tambah(self,data,pos):
        node = Node(data)
        if not self.head:
            self.head = node
        elif pos==0:
            node.next = self.head
            self.head = node
        else:
            prev = None
            current = self.head
            current_pos = 0
            while(current_pos < pos) and current.next:
                prev = current
                current = current.next
                current_pos +=1
            node.next = prev.next
            prev.next = node
        return self.head
#3e
    def hapus(self, position): 
        if self.head == None: 
            return 
        temp = self.head 
        if position == 0: 
            self.head = temp.next
            temp = None
            return 
        for i in range(position ):
            prev = temp
            temp = temp.next
            if temp is None: 
                break
        if temp is None: 
            return 
        if temp.next is None: 
            return 
        prev.next = temp.next
        temp= None 

    def tampil(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next   
    
a = LinkedList() 
a.tambahDepan(21)
a.tambahDepan(22)
a.tambahDepan(12)
a.tambahDepan(14)
a.tambahDepan(2)
a.tambahDepan(19)
a.tambahAkhir(9)
a.tampil()
a.hapus(5)
a.tambah(1,5)
print(a.cari(21))
print(a.cari(29))
a.tampil()
