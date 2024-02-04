import psutil
import os
import platform
import time
import socket
from subprocess import call
from prettytable import PrettyTable

while True:
    call ("clear")

    print ("Server Health Checker")

    # server os info
    print ("\n")
    print ("Operating system info")
    print ("\n Operating System: ", os.name)
    print ("\n Operating System name: ", platform.system())
    print ("\n Operating System version: ", platform.version())
    print ("\n Operating System release: ", platform.release())
    print ("\n Operating System architecture: ", platform.machine())
    print ("\n Computer name : ", platform.node())
    hostname = platform.node()
    IPAddr = socket.gethostbyname(hostname)
    print ("\n Computer IP address : ", IPAddr)
    print ("\n")

    # network information
    print ("Network information")
    table = PrettyTable(['Network', 'status', 'speed'])
    for key in psutil.net_if_stats().keys():
        name = key
        up = "Up" if psutil.net_if_stats()[key].isup else "Down"
        speed = psutil.net_if_stats()[key].speed
        table.add_row([name, up, speed])

    print (table)
    print ("\n")
    time.sleep(3)


