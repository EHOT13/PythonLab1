isRise = False

array = [0,1,2,3,4,5]
sum = 0

for i in range(len(array)-1):
    if array[i+1]>array[i]:
       sum = sum + 1 
       isRise = True
if isRise == True:
    print('EVO')