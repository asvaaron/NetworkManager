#!/usr/bin/python
import time
from daemon import runner
import yaml
from SSID import SSID
class App():
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path =  '/tmp/foo.pid'
        self.pidfile_timeout = 5

    def funciondecostos(self,sig,dow,up,SSDI):
        (a,b,c) = SSDI.averages

        return ((a*sig+b*dow+c*up)/sig+dow+up)

    def run(self):
        dic = {}
        file=open("pesos.yml", "r")
        doc = yaml.safe_load_all(file)
        sig=doc["Signal"]
        dow=doc["Download"]
        up=doc["Upload"]
        while True:
            stream = open("test.yml", "r")
            l = yaml.safe_load_all(stream)
            for red in l:
                SSID1=red
                dic=[SSID1.getSDDI]+=red
        for n in dic:
             print("Para la red: "+n.key)
             print(self.funciondecostos(sig,dow,up,n))
        time.sleep(10)

app = App()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()