i = 1;
while i < 10 :
    j = 1;
    while j < 10 :
        if i*j < 10 : print (j, "*" , i, "=", i*j, end = '  ', sep = '');
        elif i*j < 100 : print (j, "*" , i, "=", i*j, end = ' ' , sep = ''); 
        j += 1;
    i += 1;
    print('');
   

    
