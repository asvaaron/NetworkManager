#!/usr/bin/python
import time
from daemon import runner
import os
import subprocess
import re
import commands

class App():
    
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path =  '/tmp/foo.pid'
        self.pidfile_timeout = 5

    def speed_test(self):

        a = subprocess.Popen("speedtest", stdout=subprocess.PIPE, shell=True)
        output = a.communicate()
        b = (re.findall('\d+.\d+', output))
        return (a[4],a[5])
        """
            a = commands.getstatusoutput('speedtest')
            b = (re.findall('\d+.\d+', a))
            #return (a[4],a[5])
            print b
        """

    def get_ssids(self):
        os.system("sudo iwlist wlan0 scan | grep ESSID")
        os.system("sudo iwlist wlan0 scan | grep Signal")
        os.system("sudo iwlist wlan0 scan | grep Encryption")

        ssid = commands.getstatusoutput('sudo iwlist wlan0 scan | grep ESSID')
        signal = commands.getstatusoutput('sudo iwlist wlan0 scan | grep Signal')
        opens = commands.getstatusoutput('sudo iwlist wlan0 scan | grep Encryption')

        print ssid
        print signal
        print opens

        a = re.findall('"(.*?)"', str(ssid))
        b = re.findall('-\d+', str(signal))
        c = re.findall(':\w+', str(opens))
        print a
        print b
        print c

        return (c,b,a)

    def run(self):
        while True:
              
        
            print("-----Inicio------")
            c,b,a = self.get_ssids()
            ssid=" "
            signal=" "
            j = 0
            for i in c:
                print i
                if(i == ":off"):
                    ssid=a[j]
                    signal=b[j]
                    os.system("echo Descontando red actual...")
                    os.system("ifconfig wlan0 down")
                    time.sleep(2)
                    os.system("ifconfig wlan0 up")
                    os.system("echo Conectando...")
                    os.system("iwconfig wlan0 essid " + ssid)
                    os.system("echo Conectado a: " + ssid)
                    os.system("dhclient wlan0")
                    time.sleep(4)
                    os.system("echo Conexion establecida")
                    #self.speed_test()
                    os.system("speedtest")
                    time.sleep(10)

                j += 1
                

app = App()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()

#sudo iwconfig wlan0 essid Wifi2Home key s:ABCDE12345
