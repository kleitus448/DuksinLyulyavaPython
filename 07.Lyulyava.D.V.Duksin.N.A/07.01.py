 def maxmod(seq,N):
     return max(s%N for s in seq)
 
 N = int(input("Modulo= "))
 print(maxmod(eval(input("list of numbers = "))),
