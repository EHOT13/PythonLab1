text = input('Your text here -> ').split()

for i in range(len(text)):
    if len(text[i])>7:
        print(text[i])
    #elif 4<len(text[i]) and len(text[i])<=7:
   #            print(text[i])
   # else:
       # print(text[i])
for i in range(len(text)):
    if  4<len(text[i]) and len(text[i])<=7:
        print(text[i])
for i in range(len(text)):
    if len(text[i])<4:
        print(text[i])