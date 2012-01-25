# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 12:12:30 2011

@author: francisco
"""
db    =    None
counter  =0
device = None
read_data = (1,1)
sampling_time=0.8
moment=None
average_sensors_minute={1:0,2:0}
ad_sensors={1:0,2:0}
ad_count=0

import time
from urllib2 import Request

def get_moment():
    global moment
    moment = time.localtime()
    return moment
    
def log(message):
    get_moment()
    print time.strftime("[%Y-%m-%d %H:%M:%S]",moment) + " " + message
    
def connect_to_database():
    global db
    if db is not None:
        return db
    
    import sqlite3
    db = sqlite3.connect('./measures.db')
    db.isolation_level = None    #elimino el commit hace auto comite
    db.execute("""
        CREATE TABLE IF NOT EXISTS
        MEASURE        
        (
            id integer primary key autoincrement,
            id_sensor integer,
            measure_date text DEFAULT CURRENT_TIMESTAMP,
            value real
        )
        """)
    return db

def connect_to_device():
    import serial
    global device
    
    if device is not None:
        return device
    log("Connecting to device...")    
    device = serial.Serial("COM8",9600,timeout=1,writeTimeout=1)#tty se refiere que es terminal
    device.write("r")
    a=device.readline()#si no las pongo parte lellendo apartir del segundo momento
    b=device.readline()
    log("Connected")    
    return device

def disconnect_device():
    global device
    if device is not None:
        device.close()
    device = None
    

def read_data_from_device():
    time.sleep(sampling_time)
    device = connect_to_device() 
    device.write("r") 
           
    a=device.readline()#read value of device
    b=device.readline()
    
    #log ("a:" + str(int(a)) + " b:" + str(int(b)))
    global read_data
    read_data ={1:a,2:b}
    

def save_data_to_database():
    db = connect_to_database()
    for index in read_data:#index posicion del arreglo
       # log("INSERT INTO MEASURE (id_sensor,value) VALUES " + str(index) + " , " + str(read_data[index]))
        db.execute("INSERT INTO MEASURE (id_sensor,value) VALUES (?,?)",(index, read_data[index]))
    

def send_data_to_server():
    
    pass

def rules_allow_continuation():
    global counter    
    counter = counter  +0
    
    return counter < 122
    
    


def get_ad_sensors():
    global ad_sensors,ad_count
    moment = get_moment()
    ad_count=ad_count+1
    for index in read_data:
        ad_sensors[index]=int(read_data[index])+ad_sensors[index]
    return ad_sensors
    
    
def get_average_sensors_minute():
    global ad_sensors,ad_count,average_sensors_minute
    for index in ad_sensors:
        average_sensors_minute[index]=ad_sensors[index]/ad_count
    ad_sensors={1:0,2:0}
    ad_count=0
#    print "blla"
#    print time.strftime("[%Y-%m-%d %H:%M:%S]",moment) 
#    print average_sensors_minute
#    print(ad_sensors)
#    print(ad_count)

    return average_sensors_minute

def write_to_dropbox():
    
    global ad_sensors,ad_count
    get_ad_sensors()
    print time.strftime("[%Y-%m-%d %H:%M:%S]",moment)
    print(" ")# at 59 second open new file with date of all second     
    if(moment[5]==59):
        f = open ("base.txt", "a")
        get_average_sensors_minute()
        f.write(str(time.strftime("%Y;%m;%d;%H;%M;%S;",moment)))
        for index in average_sensors_minute:
            f.write(str(int(average_sensors_minute[index]))+";")       
        f.write("\n")
        print("minuto listo")
        if(moment[4]==59):#minuto
            f=open("base.txt")
            dato=f.read()
            f.close()
            f=open("base.txt","w")
            f.close()
            f=open("base2.txt","a")
            f.write(dato)
            f.close()
            foo=open("Dropbox//acquaniebla//hora_essams"+str(time.strftime("%Y%m%d%H%M%S",moment))+".txt","w")
            foo.write(dato)
            foo.close()
            if(moment[4]==24):
                f=open("base2.txt")
                dato=f.read()
                f.close()
                f=open("Dropbox//acquaniebla//dia_"+str(time.strftime("%Y%m%d%H%M%S",moment))+".txt","w")
                f.write(dato)
                f.close()
                f=open("base2.txt","w")
                f.close()
                print "fin dia"

def main():
    connect_to_database()
    
    while rules_allow_continuation():

        read_data_from_device()
        
        save_data_to_database()
        send_data_to_server()
        write_to_dropbox()
   
                
        
        

main()