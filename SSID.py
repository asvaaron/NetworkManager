
class SSID:

    def __init__(self,ssid='',strenght=0.0,upspeed=0.0,dospeed=0.0):
        self._ssid=ssid
        self._upspeed=upspeed
        self._dospeed=dospeed
        self._strenght=strenght
        self.count=0


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
        self.count+=1
        return SSID(self._ssid,self._strenght,self._upspeed,self._dospeed)


    def __str__(self):
        st ='  SSID: ' + self._ssid
        st += '  Strenght: ' + str(self._strenght)
        st += '  Upload Speed: ' + str(self._upspeed)
        st += '  Download Speed: ' + str(self._dospeed)
        return st

if __name__ == '__main__':
    S1=SSID('lala',2,3,4)
    S2=SSID('lwle',1.22,3.3)

    print(S1+S2)



