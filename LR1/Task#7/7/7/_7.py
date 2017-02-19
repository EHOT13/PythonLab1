import random
#---------ArrayGen------------------------------------------------
realAdressList = ['vk.com','www.music','www.monster.com','odnoklasniki']
random.shuffle(realAdressList)
AdressList = [c for c in realAdressList]
print (AdressList) 
print('')
#---------wwwControl-----------------------------------------------------
g = AdressList[0]
for i in range(len(AdressList)):
    g = AdressList[i]
    www = g[:3]
    if www != 'www':
        AdressList[i] = 'www.' + AdressList[i]
   
        #print(AdressList[i])
    print(AdressList[i])
print('')
#---------http://--------------------------------------------------------
for i in range(len(AdressList)):
    g = AdressList[i]
    AdressList[i] = 'http://' + AdressList[i]
    print(AdressList[i])
print('')
#---------.com-----------------------------------------------------------
for i in range(len(AdressList)):
    g = AdressList[i]
    com = g[len(AdressList[i])-3:]
    AdressList[i] = AdressList[i] + '.com'
    print(AdressList[i])
print('')

#print (g[:3])