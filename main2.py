# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 12:12:30 2011

@author: francisco
"""
db    =    None
counter  =0
device = None
read_data = (1,1)
sampling_time=1
moment=None


import time
from urllib2 import Request

def get_moment():
    global moment
    moment = time.localtime() 
    
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
    device = serial.Serial("/dev/ttyUSB0",9600,timeout=1,writeTimeout=1)#tty se refiere que es terminal
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
    device = connect_to_device() 
    device.write("r") 
    time.sleep(sampling_time)
       
    a=device.readline()#read value of device
    b=device.readline()
    
    log ("a:" + str(int(a)) + " b:" + str(int(b)))
    global read_data
    read_data ={1:a,2:b}
    

def save_data_to_database():
    db = connect_to_database()
    for index in read_data:#index posicion del arreglo
        log("INSERT INTO MEASURE (id_sensor,value) VALUES " + str(index) + " , " + str(read_data[index]))
        db.execute("INSERT INTO MEASURE (id_sensor,value) VALUES (?,?)",(index, read_data[index]))
    

def send_data_to_server():
    
    pass

def rules_allow_continuation():
    global counter    
    counter = counter  +1
    
    return counter < 5
    


def get_average_values_sensors():
    for index in read_data:
        average_a[index]=average_a[index]+int(read_data[index])
        log(average_a)
    
    pass



def write_to_dropbox():
    f = open ("base.txt", "a")
    f.write(str(time.strftime("%Y;%m;%d;%H;%M;%S;",moment)))
  
    for index in read_data:
        f.write(str(int(read_data[index]))+";")
        
    f.write("\n")
    f.close()
    if(moment[5]==59): # at 59 second open new file with date of all second 
        f=open("base.txt")
        dato=f.read()
        f.close
        f=open("base.txt","w")
        f.close()
        log("delete base.txt")
        f=open("base2.txt","a")
        f.write(dato)
        f.close()
        log("created base2.txt")
        if(moment==59):#minutos
                    f=open("base2.txt")
                    dato=f.read()
                    f.close()
                    f=open("base2.txt","w")
                    f.close()
                    f=open("base3.txt","a")
                    f.write(dato)
                    f.close()
                    f=open("base3.txt")
                    f.close()
                    foo=open("Dropbox//acquaniebla//hora_essams"+str(time.strftime("%Y%m%d%H%M%S",moment))+".txt","w")
                    foo.write(dato)
                    foo.close()
                    print "bb"
                    if(moment==1):#hora la 1 actualiza
                        f=open("base3.txt")
                        dato=f.read()
                        f.close()
                        f=open("Dropbox//acquaniebla//dia_"+str(time.strftime("%Y%m%d%H%M%S",moment))+".txt","w")
                        f.write(dato)
                        f.close()
                        f=open("base3.txt","w")
                        f.close()
                        print "cc"

def main():
    connect_to_database()
    
    while rules_allow_continuation():

        read_data_from_device()
        
        save_data_to_database()
        send_data_to_server()
        write_to_dropbox()
                
        
        

main()