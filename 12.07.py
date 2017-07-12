class test():
    '''Dummy test class that implements nothing'''
    name = "DUMMY"
    
    def __init__(self, x, y, size = 2):
        self.X = x
        self.Y = y
        self.SZ = size
        self.store = []
        
    def __str__(self):
        return "({}) {}:{}/{} {}".format(
            self.name, self.X, self.Y, self.SZ, self.store)
    
    def __add__(self, other):
        return test(self.Xz+other.X, self.Y+other.Y, max(self.SZ,other.SZ))
    
    def right(self):
        return self.X + self.SZ
        
    def bottom(self):
        return self.y + self.SZ
        
def ndir(obj):
    return [c for c in dir(obj) if not c.startswith("_")]
    
print(ndir(test))
a, b, c = test(10,10,100), test(20,20), test(30,30,10)
print(ndir(a))
print(a, b, c)
print(a+b)
