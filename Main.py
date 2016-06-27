#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Network_Manager import Network_Manager
from WritetoXML import WriteXMLNetwork
import NetworkManager


if __name__ == '__main__':
    for dev in NetworkManager.NetworkManager.GetDevices():
        if dev.DeviceType != NetworkManager.NM_DEVICE_TYPE_WIFI:
            continue
        for ap in dev.SpecificDevice().GetAccessPoints():
            M=Network_Manager(ap.Ssid,str(ap.Strength))
            print(M)