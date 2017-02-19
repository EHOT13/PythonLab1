

def pre_process(a):
    def d_process(fn):
        print ('pre process started')
        print (s)
        i=0
        for i in range(len(s)):
            s[i] = s[i] - a*s[i-1] 
        print (s)
        print ('pre process ')
    return d_process


s = [1.2,3.0,0.79] #Nash masiv dablov

@pre_process(a=0.93) #parametr
def plot_signal(s):
    for i in s:
       print(i) #prosto zatichka na vsyakiy sluchai
    return 0