import platform
import subprocess
import threading
import datetime


ip = input("Podaj IP: ")

def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()

def ping(host):
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '1', host]
    return subprocess.call(command)

def writeScoreToFile():
    score = ping(ip)
    file = open("LostPings.txt", "a")
    loss = 0
    if score == 1:
        loss = loss + 1
        file.write(ip + "   Straconych: " + str(loss) + "       Kiedy:        " + str(datetime.datetime.now()) + "\n")


setInterval(writeScoreToFile, 1)