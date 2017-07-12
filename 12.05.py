import sys
class dummy:
    data = 100500
    name = "QQQ"
    
    def ID(self):
        return "{}:{}".format(self.data, self.name)
    
a, b, e = dummy(), dummy(), dummy()
a.data = -1
e.data, e.name = 777, "EEE"
print(a.ID())
print(b.ID())
print(e.ID())
print("a:", dummy.ID(a))
