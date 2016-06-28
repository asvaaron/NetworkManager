
class SSID:

    def __init__(self,ssid):
        self._ssid=ssid
        self._upspeed=0.0
        self._dospeed=0.0
        self._strenght=0.0
        self.count=0


    def getUpspeed(self):
        return self._upspeed

    def getDospeed(self):
        return self._dospeed
    def getStrenght(self):
        return self._strenght

    def __add__(self, other):
        self._strenght=other.getStrenght()
        self._upspeed=other.getUpspeed()
        self._dospeed=other.getDospeed()
        self.count+=1


    def __str__(self):
        str ='  SSID: '+self._ssid
        str += '  Strenght: ' + self._strenght
        str += '  Upload Speed: ' + self._upspeed
        str += '  Download Speed: ' + self._dospeed



