import os
import time
import datetime
import csv



hosts=["8.8.8.8","1.1.1.1","192.168.56.1"]
def ipcheck():
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
      
now =datetime.datetime.now()
def processed():
    with open('protses.csv', 'w',newline="",encoding="utf-8") as file:
        writer=csv.writer(file)
        writer.writerow(["TIME","Protsess name","mem usage"])

    output=os.popen("tasklist").read()
    test=output.splitlines()
    for i in range(7, len(test)):
        print(test[i])
        processname=test[i].split()
        name=processname[0]
        memory =processname[-2]
        print("time:",now,"name:", name,"memory:",memory)
        print()
        print()
        


              
        with open('protses.csv', 'a',newline="",encoding="utf-8") as file:
            writer=csv.writer(file)
            writer.writerow([now, name, memory])
            
def menu():
    print("1 ")
    print("2 ")
    
    userInput = input("Sinu valik: ")

    if userInput == "1":
        ipcheck()
    elif userInput == "2":
        processed()

    else:
        print("Vale valik!")


menu()            
#test            
