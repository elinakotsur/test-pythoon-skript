import os
import time

hosts=["8.8.8.8","1.1.1.1","192.168.56.1"]

while True:
    print("kätesadevuse kontroll")
    for elem in hosts:
        response=os.system(f"ping -n 1 {elem}> null")
        if response == 0:
            print(elem,"kättesadavalt")
        else:
            print(elem, "ei ole kättesadavalt")
        print("-"*30)
        time.sleep(5)
            