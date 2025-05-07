import os
import time
import datetime
import csv


now =datetime.datetime.now()

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
            
      