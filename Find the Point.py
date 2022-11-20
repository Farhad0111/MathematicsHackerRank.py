class Farhad:
    def __init__(self,i):
        self.i=i
    def faru(self):
        for i in range (0,self.i):
            self.d=list(map(int,input().split()))
            print(2*self.d[2]-self.d[0],2*self.d[3]-self.d[1])

farhad=Farhad(i=int(input()))
farhad.faru()