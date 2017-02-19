
def frange(start,end,step):
    #bomzh-analog range
    st = start #int start
    
    start = float(start)    #privedenie k float
    end = float(end)
    step = float(step)
    step = round(step,2)    #okruglenie
    
    adD = []        #init array
    adD.append(start)   #addition elements to array
    end = int((end-start)/step)     #counter for kol-vo shagov
   
    for i in range(st,end): 
        adD.append(adD[i-1] + step)     #-1 potomy chto startoviy element yzhe est`
        round(adD[i-1],2)
    return adD
   
for y in frange(1, 5, 0.1):
    print (round(y,2))