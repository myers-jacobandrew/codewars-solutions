def get_real_floor(n):
    if (n > 0) and (n<=12):
        n = n-1
    elif (n >= 13):
        n = n-2
    return n        
                