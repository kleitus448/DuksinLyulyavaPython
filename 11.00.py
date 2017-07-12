def gen(num):
    print("start")
    yield 100500
    print("continue")
    for i in range(num):
        yield i*2+1
    print("Done")    
    yield -1500500
    print("finish")


for c in gen(4):
    print("########",c)       
