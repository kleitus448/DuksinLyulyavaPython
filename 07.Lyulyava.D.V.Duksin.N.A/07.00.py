def max_spaces(e):    
   return max(e,key=lambda s: s.count(' '))
 
def do_input():
    strings = []
    s = input()
    while s:
        strings.append(s)
        s = input()
        return strings                  
    
if __name__=="__main__":
    print(max_spaces(do_input()))
