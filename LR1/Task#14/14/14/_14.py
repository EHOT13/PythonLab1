#decorator bez parametrov
def non_empty(funcToDec):
    def wrapper(): #obertka
        #before 
        print ('--Before-------------')
        print (funcToDec())
        print ('---------------------\n')
        #after
        print ('--After--------------')
        temp = funcToDec() # esli rabotat` s func to dannie pochemy to ne sohranyauco
        temp = [x for x in funcToDec() if x != '']
        print (temp)
                
        print ('---------------------\n')
    return wrapper()

@non_empty 
def get_pages():
    return ['chapter1', '', 'contents', '', 'line1']