def multi_table(number):
    result=''
    for i in range(1,11):
        result+=str(i) +' * ' + str(number) + ' = ' + str(i*number) + '\n'        
    return result.rstrip()