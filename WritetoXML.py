#!/usr/bin/env python
# -*- coding: utf-8 -*-
from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement


class WriteXMLNetwork:
    def __init__(self):
        self._root = Element('Root')

    def write(self, SSID, Strenght):
        network = SubElement(self._root, 'Network')
        SSID1 = SubElement(network, 'SSID')
        SSID1.text = SSID
        Strenght1 = SubElement(network, 'Strenght')
        Strenght1.text = Strenght
        output_file = open('Networks.xml', 'w+')
        output_file.write('<?xml version="1.0"?>')
        output_file.write(ElementTree.tostring(self._root))
        output_file.close()


if __name__ == '__main__':
    M = WriteXMLNetwork()
    M.write("VR", "34%")
    M.write("LAla", "24%")
    M.write("L23la", "24%")
    M.write("hgs", "2%")
