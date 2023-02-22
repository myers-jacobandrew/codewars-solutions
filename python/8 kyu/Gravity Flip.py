def flip(d, a):
    # Do some magic
    if (d == 'R'):
        #ascending sort 
        a.sort()
        
    elif (d == 'L'):
        #descending sort
        a.sort(reverse = True)
    return a