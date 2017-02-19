import random
n = int(random.uniform(0, 10000))
print(n)

nArray = [random.randrange(0, 10000) for i in range(n)]
print (nArray)

p = 2
i = 0
while p**i <= n:
    #print(p**i, end=' ')
    zero = p**i
    print('zero',zero)
    i = i + 1

zero = (p**i+1)    #pochemy to pri adekvatnom sintaxise eto ne rabotalo, prishlos pisat tak
print('zero',zero)

appendix = zero - n
for i in range(appendix):
    nArray.append(0)

print(nArray)