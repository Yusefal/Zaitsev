# -*- coding=utf-8 -*-

time12=list(input("por favor ingresa la hora actual en formato 12 hrs: "))

if int(time12[0]) <= 1:
    hour = time12[0] + time12[1]
    minutes = time12[3] + time12[4]
    ind = time12[6]
    print("La hora es {} horas ".format(hour) + "con {} minutos".format(minutes))
    print(ind)
else: 
    hour = time12[0]
    minutes = time12[2] + time12[3]
    time12.append(" ")
    print(time12)
    ind = time12[5]
    

if ind == "a" or ind == "A": 
    print (" la hora en formato militar es 0{}".format(hour),"{}".format(minutes))
elif ind == "p" or ind == "P":
    print ("la hora en formato militar es ", int(hour)+ 12, ":", "{}".format(minutes))    
    


"""
if len(time12)==7:
    hour = time12[0]
    minutes = time12[2] + time12[3]
    ind = time12[5]
else:
    hour = time12[0] + time12[1]
    minutes = time12[3] + time12[4]
    ind = time12[6]

if ind == "A":
    print(hour,":", minutes,sep="")
elif ind == "P":
    print(int(hour) + 12, ":", minutes, sep="")
"""