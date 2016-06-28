
class SSID:

    def __init__(self,ssid='',strenght=0.0,upspeed=0.0,dospeed=0.0,count=1):
        self._ssid=ssid
        self._upspeed=upspeed
        self._dospeed=dospeed
        self._strenght=strenght
        self._count=count


    def getUpspeed(self):
        return self._upspeed

    def getDospeed(self):
        return self._dospeed
    def getStrenght(self):
        return self._strenght

    def __add__(self, other):
        self._strenght+=other.getStrenght()
        self._upspeed+=other.getUpspeed()
        self._dospeed+=other.getDospeed()
        self._count+=1
        return SSID(self._ssid,self._strenght,self._upspeed,self._dospeed,self._count)


    def __str__(self):
        st ='  SSID: ' + self._ssid
        st += '  Strenght: ' + str(self._strenght)
        st += '  Upload Speed: ' + str(self._upspeed)
        st += '  Download Speed: ' + str(self._dospeed)
        st += '  Count: ' + str(self._count)

        return st

    def averages(self):
        return (self._strenght/self._count,self._dospeed/self._count,self._upspeed/self._count)

if __name__ == '__main__':
    S1=SSID('lala',2,3,4)
    S2=SSID('lwle',1.22,3.3,1)

    print(S1+S1+S2+S2)



