def lovefunc( flower1, flower2 ):
    even1 = True
    even2 = True
    if (flower1 % 2) == 0:
        #flower1 is even
        even1 = True
    else:
        #flower1 is odd
        even1 = False
    if (flower2 % 2) == 0:
        #flower2 is even
        even2=True
    else:
        #flower2 is odd
        even2 = False
        
        
        
    if (even1 == even2):
        return False
    else: 
        return True