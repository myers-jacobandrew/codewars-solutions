def reverse_words(s):
    s1=''
    l1 = s.split() 
    l1.reverse()
    for i in l1: 
        s1 += i
        s1 += ' '
    return s1.rstrip()