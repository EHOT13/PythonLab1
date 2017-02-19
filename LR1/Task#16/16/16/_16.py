#from random import random #���������� ��� �������(?) ne srabotalo
import random #edet normalno
import itertools #for iterations
import time
#from datetime import datetime #date for shedule
from datetime import datetime, timedelta
TeamList = [           #������ 16 ��� ������ �� ������ UEFA (16�� ����� �������� �� 17��)
    'Real Madrid',
    'Bayern M?nchen',
    'FC Barcelona',
    'Atl?tico Madrid',
    'Juventus',
    'Paris Saint-Germain',
    'Borussia Dortmund',
    'Benfica',
    'Sevilla',
    'Chelsea',
    'Arsenal',
    'FC Porto',
    'Manchester City',
    'Bayer Leverkusen',
    'Schalke 04',
    'Shakhtar Donetsk'
    ]


random.shuffle(TeamList) #randomize spiska
print ('\n--Team List:----------------------')
print ('\n'.join(TeamList)) #test. vivod po-strochno. v c++ bilo proshe((9(
 
TeamList = [TeamList[d:d+4] for d in range(0, len(TeamList), 4)] #��������� �� ������

print ('\n--Group List:----------------------')
print ('Group A: ',TeamList[0])
print ('Group B: ',TeamList[1])
print ('Group C: ',TeamList[2])
print ('Group D: ',TeamList[3])
print ('\n--Match schedule:------------------')

#-------date----------
tempDate = "14.09.2017"
#startDate = datetime.datetime.strptime(tempDate, "%d.%m.%Y")
startTime = [14,9,2017]
endTime = [14,4,2018]

print ('Season starts in', str(startTime[0])+'/'+str(startTime[1])+'/'+str(startTime[2])+' '+ str('22:45') )
print ('Season ends in', str(endTime[0])+'/'+str(endTime[1])+'/'+str(endTime[2])+' '+ str('22:45') )

now_date = datetime.now()
now_date = now_date.replace(2017,9,14)
#TODO: ���� �������������� ������ ���� �� �������� ����. ���� ������� ���� == ����� - ����� �� ������ ����� � 2�� ��������� �� ����
print ('\n')
#Test---------------
a = datetime(2017, 9, 20)
b = timedelta(days=7)
#print ('%s/%s/%s' % (now.month, now.day, now.year))
#print (str(a.day, a.month, a.year))
#print ('%s/%s/%s' % (a.day, a.month, a.year) + '   22:45')
#print (str(a+b))
while a<=datetime(2018, 4, 14):
    a=a+b
    print ('%s/%s/%s' % (a.day, a.month, a.year) + '   22:45')
#Test---------------

input() #�������� ��� �������� ������