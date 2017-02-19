def Enter():
    return float(input('Your money here -> '))

cheker = False

while cheker == False:
    try:
        money = Enter()
        if money<=0:
            raise ValueError
        cheker = True
    except ValueError:
        print('SYMBOLS or LETTERS or MINUS-BALANCE NOT ALLOWED, INPUT YOUR MONEY!')

RUB = int(money)
COP = money % 1
COP = round(COP,2) * 100


print('Your balance is -> %s rub %s cop' %(RUB,int(COP)))