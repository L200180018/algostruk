class DNode(object):
    def __init__ (self, data):
        self.data = data
        self.next = None
        self.prev = None
a = DNode("Dono")
b = DNode("kasino")
c = DNode("indro")

a.next = b
b.next = c
b.prev = a
c.prev = b
