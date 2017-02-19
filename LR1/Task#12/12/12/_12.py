
def get_frames(signal,size,overlap):
    #tyt m9so
   
    print ('Step: ')
    x = signal
    step = size * overlap
    print (step)
    i = 0
    while i<len(signal):
        print (signal[i:i+size])
        i = i + int(step)
    """
    for i in signal:
        print (signal[i:i+4])
        print (i)        
    y = signal[5:]
    """
    #nado return frame



size = 4     #shag, razmer 'ekrana'(?), oblast zahvata?
signal = [i for i in range(0,1024)] #signal with 1024kb//nash potok
overlap = 0.5 #stepen nalozhenia kadra ili chto to tipa takogo


get_frames(signal,size,overlap)
