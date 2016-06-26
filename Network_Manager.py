#!/usr/bin/env python
# -*- coding: utf-8 -*-

import NetworkManager


class Network_Manager:

    def __init__(self):
        self.__devicetype=NetworkManager.const('device_type', 2)
        self._status=NetworkManager.const('state', 40)



    def imprimir(self):
        #for dev in NetworkManager.NetworkManager.GetDevices():
        #    if dev.DeviceType != NetworkManager.NM_DEVICE_TYPE_WIFI:
        #    #NetworkManager.NM_DEVICE_TYPE_ETHERNET
        #        continue
        #    for ap in dev.SpecificDevice().GetAccessPoints():
        #        print '%-15s %dMHz %d%%' % (ap.Ssid, ap.Frequency, ap.Strength)

        #print("Available connections")
        #print("%-30s %s" % ("Name", "Type"))
        #for conn in NetworkManager.Settings.ListConnections():
        #    settings = conn.GetSettings()['connection']
        #    print("%-30s %s" % (settings['id'], settings['type']))

        print("")

        print("Active connections")
        print("%-30s %-20s %-10s %s" % ("Name", "Type", "Default", "Devices"))
        for conn in NetworkManager.NetworkManager.ActiveConnections:
            settings = conn.Connection.GetSettings()['connection']
            print("%-30s %-20s %-10s %s" % (
            settings['id'], settings['type'], conn.Default, ", ".join([x.Interface for x in conn.Devices])))


