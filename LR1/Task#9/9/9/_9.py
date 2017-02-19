#«5*1000 + 3*100 + 1*50 + 2*10». 
#bank = [10[1000],100[100],150[50],500[10]]

def cashInput():
    print ('How much you want to cash out?: ')
    return int(input('Enter amount: '))
#Govnokod sluchilsya, sore
bank = {1000:10, 100:100, 50:150, 10:500} #abstract money
print ('Money available:')
print ('Denomination - \'1000\', count -',bank[1000],', Summ = ',bank[1000]*1000)
print ('Denomination - \'100\', count -',bank[100],', Summ = ',bank[100]*100)
print ('Denomination - \'50\', count -',bank[50],', Summ = ',bank[50]*50)
print ('Denomination - \'10\', count -',bank[10],', Summ = ',bank[10]*10)

normalBank = [10,100,150,500] #Money in fact 0-1000 1-100 2-150 3-500
#cash = 0
out = False

while out == False:
    try:
        #cashInput()
        cash = 0
        cash = cashInput()
        if cash % 10 != 0:
            raise ValueError
        else:
            out = True
    except ValueError:
        cash = 0
        print ('Only INT allowed & ten fold')
        #cash = cashInput()

#cash = cashInput()
listCash = list(str(cash))      #trash
#--------1000------------------------
thousands = int(cash/1000)
cashOut = 0
i = 0
while i<thousands:           #working fine
    if normalBank[0] != 0:
        cashOut = cashOut + 1000
        normalBank[0] = normalBank[0]-1 
    else:
        print('Not enough denominations, proccess decline!')
        input()
        raise SystemExit
    i = i + 1

#--------100-------------------------
hundreds = int ((cash-cashOut)/100)
i = 0
while i<hundreds:
    if normalBank[1] != 0:
        cashOut = cashOut + 100
        normalBank[1] = normalBank[1]-1
    else:
        print('Not enough denominations, proccess decline!')
        input()
        raise SystemExit
    i = i + 1
#--------50--------------------------
halfs = int((cash-cashOut)/50)
i = 0
while i<halfs:
    if normalBank[2] != 0:
        cashOut = cashOut + 50
        normalBank[2] = normalBank[2]-1
    else:
        print('Not enough denominations, proccess decline!')
        input()
        raise SystemExit
    i = i + 1
#--------10--------------------------
tens = int((cash-cashOut)/10)
i = 0
while i<tens:
    if normalBank[3] != 0:
        cashOut = cashOut + 10
        normalBank[3] = normalBank[3]-1
    else:
        print('Not enough denominations, proccess decline!')
        input()
    i = i + 1

#TODO: if net denom
print(cashOut)
print('Denominations at this moment(1000/100/50/10)  :   ',normalBank)
