# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 12:12:30 2011

@author: francisco
"""
db    =    None
counter  =0
device = None
read_data = None
import time
import urllib
from urllib2 import Request,urlopen


def log(message):
    moment = time.gmtime()    
    print time.strftime("[%Y-%m-%d %H:%M:%S ]",moment) + " " + message
    
def connect_to_database():
    global db
    if db is not None:
        return db
    
    import sqlite3
    db = sqlite3.connect('./measures.db')
    db.row_factory = sqlite3.Row
    db.isolation_level = None    #¿para que sirve este comando?    
    db.execute("""
        CREATE TABLE IF NOT EXISTS
        MEASURE        
        (
            id integer primary key autoincrement,
            id_sensor integer,
            measure_date text DEFAULT CURRENT_TIMESTAMP,
            value real,
            sent integer DEFAULT 0
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
    log("Connected")  
    device.write("r")
    a=device.readline()#si no las pongo parte lellendo apartir del segundo momento
    b=device.readline()
    return device

def disconnect_device():
    global device
    if device is not None:
        device.close()
    device = None
    

def read_data_from_device():
    device = connect_to_device() 
    device.write("r")
    
    a=device.readline()#read value of device
    b=device.readline()
    
    log ("a:" + str(a) + " b:" + str(b))
    global read_data
    read_data ={1:a,2:b}
    

def save_data_to_database():
    db = connect_to_database()
    for index in read_data:#index posicion del arreglo
        log("INSERT INTO MEASURE (id_sensor,value) VALUES " + str(index) + " , " + str(read_data[index]))
        db.execute("INSERT INTO MEASURE (id_sensor,value) VALUES (?,?)",(index, read_data[index]))
        #Grabar en un archivo de texto

def send_data_to_server():
    
    url = "http://1.androidtravellog.appspot.com/storeavalue"    
    query = "select * from measure where sent = 0"
    db = connect_to_database()
    cursor = db.cursor()
    cursor.execute(query)
    for row in cursor:
        output_data = {}
        for key in row.keys():
            output_data[key] = row[key]

        data_to_server = {'tag' : "anm_" + str(row['id']), 'value':output_data}      
        try:
            request = Request(url,urllib.urlencode(data_to_server))
            f = urlopen(request)
            print f.read()
            db.execute("UPDATE MEASURE SET sent = 1 where id = ?",[row['id']])
            #log ("UPDATE MEASURE SET sent = 1 where id = " + str(row['id']))
        except Exception as exc:
            log(str(exc))



def rules_allow_continuation():
    global counter    
    counter = counter  +1
    return counter < 3
    

def main():
    connect_to_database()
    
    while rules_allow_continuation():
        read_data_from_device()
        save_data_to_database()
        
    send_data_to_server()             
        
        

main()