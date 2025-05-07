import os
import time
import datetime
import csv



hosts=["8.8.8.8","1.1.1.1","192.168.56.1"]

with open('ping_log.csv', 'w',encoding="utf-8") as file:
    writer=csv.writer(file)
    writer.writerow(["TIME","Status"])

while True:
    print("kätesadevuse kontroll")
    now =datetime.datetime.now()
    for elem in hosts:
        response=os.system(f"ping -n 1 {elem}> null")
        if response == 0:
            result= "OK"
            print(elem,"kättesadavalt")
        else:
            result= "Fail"
            print(elem, "ei ole kättesadavalt")
            
          
    with open('ping_log.csv', 'a',encoding="utf-8") as file:
        writer=csv.writer(file)
        writer.writerow([now,result])    
            
        print("-"*30)
        time.sleep(5)
  
