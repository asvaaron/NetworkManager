#!/usr/bin/env python
# -*- coding: utf-8 -*-

import NetworkManager
import os
import subprocess
import re
from WritetoXML import WriteXMLNetwork

class Network_Manager:

    def __init__(self,SSID,Strenght):

        self._device=''
        self._SSID=SSID
        self._Strenght=Strenght
        self._upspeed=''
        self._dospeed=''


    def initialize(self):
        self.__device=NetworkManager.const('device_type', 2)
        self._status=NetworkManager.const('state', 40)
        self._dospeed, self._upspeed = self.speed_test()

    def speed_test(self):
        p = subprocess.Popen("speedtest", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p_status = p.wait()
        print "Command output : ", output
        print "Command exit status/return code : ", p_status
        a=(re.findall('\d+.\d+', output))
        return (a[4],a[5])

    def __str__(self):
        str='Network: '
        str += '  SSID: '+ self._SSID
        str += '  Strenght: '+ self._Strenght
        str +='  Upload Speed: '+ self._upspeed
        str +='  Download Speed: '+ self._dospeed
        str+='  Device:  '+ self._device
        return str;

    def writeXml(self):
        W=WriteXMLNetwork();
        W.write(self._SSID,self._Strenght,self._dospeed,self._dospeed)