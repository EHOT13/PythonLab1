
def extra_enumerate(someArray, start):
    #enum ne enum
    n = start
    cum = 0
    for elem in someArray:   
        yield n, elem  #vozvrashaet generator
        n += 1
        cum = cum + elem
        print(n,'|---|',elem,'|---|',cum,'|---|',cum*0.1)


x  = [1,3,4,2] 
print ('id|---|num|---|sum|---|10%')
for i in extra_enumerate(x,0):
    print() 