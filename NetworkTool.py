import os
import platform
import subprocess
import threading
import datetime
import time

def ipChange(networkCard):
    os.system('cmd /c cls')
    print("1.DHCP")
    print("2.STATIC")
    print("3.CANCEL")
    choice = int(input())
    if choice == 1:
        os.system('cmd /c "netsh interface ip set address "' + networkCard + '" source=dhcp"')
        os.system('cmd /c "netsh interface ip set dns "' + networkCard + '" source=dhcp"')
        time.sleep(3)
        os.system('cmd /c cls')
    elif choice == 2:
        print("ENTER IP:")
        ip = input()
        print("ENTER SUBNET MASK :")
        subnetMask = input()
        print("ENTER DEFAULT GATEWAY:")
        defaultGateway = input()
        os.system('cmd /c "netsh interface ip set address "' + networkCard + '" static ' + ip + " " + subnetMask + " " + defaultGateway + " " + '"')
        time.sleep(3)
        os.system('cmd /c cls')
        return 0
    elif choice == 3:
        os.system('cmd /c cls')
        return 0
    else:
        print("INVALID OPTION")
        time.sleep(1)
        os.system('cmd /c cls')
        return 1


def ipCheck():
    os.system('cmd /c cls')
    os.system('cmd /c "ipconfig"')
    print("\n")
    print("\n")

def testConnection():
    os.system('cmd /c cls')
    ip = input("Podaj IP: ")

    def setInterval(func, time):
        e = threading.Event()
        while not e.wait(time):
            func()

    def ping(host):
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        command = ['ping', param, '1', host]
        return subprocess.call(command)

    def writeScoreToFile():
        score = ping(ip)
        file = open("LostPings.txt", "a")
        loss = 0
        if score == 1:
            loss = loss + 1
            file.write(
                ip + "   Straconych: " + str(loss) + "       Kiedy:        " + str(datetime.datetime.now()) + "\n")

    setInterval(writeScoreToFile, 1)

def readNetworkCards():
    cards = []
    try:
        file = open("NetworkCards.txt", "r")
    except OSError:
        os.system('cmd /c cls')
        print("FILE ERROR: NetworkCards.txt")
        time.sleep(3)
        return 1
    for index in range(2):
        cards.append(file.readline().replace("\n", ""))
    return cards


def main():

    print("1.IP LAN CHANGE")
    print("2.IP WLAN CHANGE")
    print("3.IPCONFIG")
    print("4.TEST CONNECTION")

    service = int(input())

    if service == 1:
        ipChange(readNetworkCards()[0])
    elif service == 2:
        ipChange(readNetworkCards()[1])
    elif service == 3:
        ipCheck()
    elif service == 4:
        testConnection()
    else:
        print("INVALID OPTION")
        time.sleep(1)
        os.system('cmd /c cls')


while 1:
 main()


