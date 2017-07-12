def ndir(obj):
    return [c for c in dir(obj) if not c.startswith("_")]
class empty:
    pass
    
print("empty:", ndir(empty))
a = empty()
print("a:", ndir(a))
empty.common = "ALL"
empty.list = [1,56,2,45]
print("New empty:", ndir(empty))
b = empty()
print("a:", ndir(a), a.common)
print("b:", ndir(b), b.common)
a.common = "For A"
a.list[1] = "QKRQ!"
b.list = "ZZZ"
print("New empty:", ndir(empty), empty.common)
print("a:", ndir(a), a.common, a.list)
print("b:", ndir(b), b.common, b.list)

