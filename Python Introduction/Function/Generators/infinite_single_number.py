def infinite_single_num():
    
    while True:
        
        yield 26
        

for i in infinite_single_num():
    
    print(i)