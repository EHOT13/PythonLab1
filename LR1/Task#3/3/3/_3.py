import re

def enter():
    return str(input('Enter your card number -> '))

cheker = False
while cheker == False:
    try:
        code = enter()
        code = re.sub(r'\s', '', code)
        code = int(code)
        if len(str(code)) !=16:
            raise ValueError
        cheker = True
    except ValueError:
        print('INVALID INPUT!')
   
     
strCode = str(code)
print(strCode[:4]+' **** **** '+strCode[12:])