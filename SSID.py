import yaml


class SSID(yaml.YAMLObject):
    yaml_loader = yaml.SafeLoader
    yaml_tag = u'!SSID'

    def __init__(self, ssid='', strenght=0.0, upspeed=0.0, dospeed=0.0, count=1):
        self.ssid = ssid
        self.upspeed = upspeed
        self.dospeed = dospeed
        self.strenght = strenght
        self.count = count

    def getSSID(self):
        return self.ssid

    def getUpspeed(self):
        return self.upspeed

    def getDospeed(self):
        return self.dospeed

    def getStrenght(self):
        return self.strenght


    def __add__(self, other):
        self.strenght += other.getStrenght()
        self.upspeed += other.getUpspeed()
        self.dospeed += other.getDospeed()
        self.count += 1
        return SSID(self.ssid, self.strenght, self.upspeed, self.dospeed, self.count)

    def __repr__(self):
        return "%s(SSID=%r, Strenght=%r, DownloadSpeed=%r,UploadSpeed=%r,count=%r)" % (
            self.__class__.__name__, self.ssid, self.strenght, self.dospeed, self.upspeed, self.count)

    def __str__(self):
        st = '  SSID: ' + self.ssid
        st += '  Strenght: ' + str(self.strenght)
        st += '  Upload Speed: ' + str(self.upspeed)
        st += '  Download Speed: ' + str(self.dospeed)
        st += '  Count: ' + str(self.count)

        return st

    def averages(self):
        return (self._strenght / self._count, self._dospeed / self._count, self._upspeed / self._count)


if __name__ == '__main__':
    S1 = SSID('lala', 2, 3, 4)
    S2 = SSID('lwle', 1.22, 3.3, 1)

    print(S1 + S1 + S2 + S2)
