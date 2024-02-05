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
    # time.sleep(3)

    # memory information
    print ("Memory information")
    print ("\n")
    memory_table = PrettyTable(['Total(GB)', 'Used(GB)', 'Free(GB)', 'Percentage'])
    vm = psutil.virtual_memory()
    memory_table.add_row([vm.total / (1024 ** 3), vm.used / (1024 ** 3),
                          vm.free / (1024 ** 3), vm.percent])
    print (memory_table)
    print ("\n")

    # disk information
    print ("Disk information")
    print ("\n")
    disk_table = PrettyTable(['Partition', 'Total(GB)', 'Used(GB)', 'Free(GB)', 'Percentage'])
    partitions = psutil.disk_partitions()
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        disk_table.add_row([partition.device, usage.total / (1024 ** 3),
                            usage.used / (1024 ** 3), usage.free / (1024 ** 3), usage.percent])
    print (disk_table)
    print ("\n")

    # Top 10 processes by memory usage
    print ("Top 10 processes by memory usage")
    print ("\n")
    proccess_table = PrettyTable(['PID', 'PNAME', 'STATUS', 'CPU(%)', 'MEM(%)'])
    proc = []

    for pid in psutil.pids()[-200:]:
        try:
            p = psutil.Process(pid)
            p.cpu_percent()
            proc.append(p)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    # Sort by cpu percent
    top = {}
    time.sleep(0.1)
    for p in proc:
        top[p] = p.cpu_percent() / psutil.cpu_count()
    top_list = sorted(top.items(), key=lambda x: x[1], reverse=True)
    top10 = top_list[-10:]
    top10.reverse()

    for p, cpu_persent in top10:
        try:
            with p.oneshot():
                proccess_table.add_row([str(p.pid), p.name(), p.status(), p.cpu_percent(),
                                        p.memory_percent()])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    print (proccess_table)
    time.sleep(5)


