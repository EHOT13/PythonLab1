print('Your pass must containe atleast 4 symbols')
def password():
    pswrd = input('ENTER YOUR PASS:')
    #print(pswrd)
    return pswrd

passwordAr = ''

while len(passwordAr)<4:
    passwordAr = password()
    if len(passwordAr)<4:
        print('Minimum 4 symbols require')
        
digit = False 
uppeR = False 
loweR = False
symbs = False 
counter = 0

nums = ['0','1','2','3','4','5','6','7','8','9']
alphaL = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphaU = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols = ['!','@','#','$','%','^','&','*','(',')','_','+','-','=',' ']
print ('Lets chek security lvl of your pass...')
for x in passwordAr:
    if x in nums:
        digit = True
    if x in alphaU:
        uppeR = True
    if x in alphaL:
        loweR = True
    if x in symbols:
        symbs = True
        

if digit == True:
    counter = counter + 1
if uppeR == True:
    counter = counter + 1
if loweR == True:
    counter = counter + 1
if symbs == True:
    counter = counter + 1

lvl = ['RUSSIAN DETECTED!11!','EASY','NORMAL','SECURE','OVERSECURE']
print('Your Securuty level is:',lvl[counter])   
    
    
