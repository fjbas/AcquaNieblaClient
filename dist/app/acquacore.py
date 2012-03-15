# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 12:12:30 2011

@author: francisco
"""

db    =    None
counter  =0
device = None
read_data = None
token = None
sensor_startup = [[],[],[],[],[],[],[],[],[],[],[]] 
seconds_between_data_samples = 1
seconds_between_average_calculation = 60
seconds_between_watch_dog=30
keep_going = True
ad_sensors=sensor_startup



import time
import sys

from threading import Timer

def log(message):
    moment = time.gmtime()    
    print time.strftime("[%Y-%m-%d %H:%M:%S ]",moment) + " " + str(message)
    
def connect_to_database():
    global db
    keep_going
    import sqlite3
    db = sqlite3.connect('/acquaniebla/db/measures.db')
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
    db.execute("""
        CREATE TABLE IF NOT EXISTS
        CONFIGURATION
        (
            key text primary key,
            value text
        )
    """)
    return db

def connect_to_device():
    import serial
    global device
    global keep_going
    if device is not None:
        return device
    log("Connecting to device...")    
    try:
        device = serial.Serial("/dev/ttyUSB0",9600,timeout=1,writeTimeout=1)#tty se refiere que es terminal
    except:
        log("Connection error")
        keep_going = False
        sys.exit(500)
    log("Connected")  
    
    return device

def disconnect_device():
    global device
    if device is not None:
        device.close()
    device = None
    
def disconnect_database():
    db.close()

def get_average_sensors():
    global ad_sensors
    sensors_average = []
    for index in ad_sensors:
        if(len(index) == 0): continue
        avg = sum(index) / len(index)

        sensors_average.append(avg)

    log(sensors_average)

    save_data_to_database(sensors_average)
    
    ad_sensors=[[],[],[],[],[],[],[],[],[],[],[]]
    

def read_data_from_device():
    global read_data
    global ad_sensors, ad_count
    read_data = []    
    device = connect_to_device() 
    line = ""       
    try:
        device.write("r")
    except:
        sys.exit("500")
    line = device.readline().strip()
    
    while (line != "EOF" and len(line) > 0):
        value = float(line)
        read_data.append(line) 
        index = len(read_data) - 1
        ad_sensors[index].append(value)
        line = device.readline().strip()
    

    log(ad_sensors)
    
    

def save_data_to_database(data):
    db = connect_to_database()
    for index in range(len(data)):#index posicion del arreglo
        log("INSERT INTO MEASURE (id_sensor,value) VALUES " + str(index) + " , " + str(data[index]))
        db.execute("INSERT INTO MEASURE (id_sensor,value) VALUES (?,?)",(index, data[index]))
        #Grabar en un archivo de texto
    disconnect_database()


def data_capture():
    if keep_going:
        Timer(seconds_between_data_samples,data_capture).start()
    log("data capture")    
    read_data_from_device()

def get_average_and_save():
    if keep_going:
        Timer(seconds_between_average_calculation,get_average_and_save).start()    
    log("average calculation")
    get_average_sensors()
    

def rules_allow_continuation():
    global counter    
    counter = counter  +1
    return counter < 5 and keep_going
    
def watch_dog():
    if keep_going:
        Timer(seconds_between_watch_dog,watch_dog).start() 
    log("Watchdog is writing the file...")
    f = open ("/acquaniebla/log/acquaniebla.watchdog", "w")
    f.close()
    
    
def main():
    watch_dog()
    time.sleep(60)
    connect_to_database()
    Timer(seconds_between_data_samples,data_capture).start()
    Timer(seconds_between_average_calculation,get_average_and_save).start()
    
                 
        
        

main()
