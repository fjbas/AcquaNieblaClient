# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 11:02:21 2012

@author: root
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 12:12:30 2011

@author: francisco
"""

db    =    None
counter  =0
device0 = None
device1 = None
device_name_0=None
device_name_1=None
read_data_0= None
read_data_1= None
token = None
sensor_startup = [[],[],[],[],[],[],[],[],[],[],[]] 
seconds_between_data_samples = 1
seconds_between_average_calculation = 60
seconds_between_watch_dog=30
keep_going0 = True
keep_going1 = True
ad_sensors_0=[[],[],[],[],[],[],[],[],[],[],[]] 
ad_sensors_1=[[],[],[],[],[],[],[],[],[],[],[]] 
ad_sensors_2=[[],[],[],[],[],[],[],[],[],[],[]] 
number_of_sensors_of_divice_0=6
number_of_sensors_of_divice_1=6


import time
import sys
import serial

from threading import Timer

def log(message):
    moment = time.gmtime()    
    print time.strftime("[%Y-%m-%d %H:%M:%S ]",moment) + " " + str(message)
    
def connect_to_database():
    global db
    keep_going0
    import sqlite3
    db = sqlite3.connect('/home/francisco/Escritorio/prueba_con_2_entradas_usb/measures.db')
    db.row_factory = sqlite3.Row
    db.isolation_level = None    
    db.execute("""
        CREATE TABLE IF NOT EXISTS
        MEASURE        
        (
            id_operation integer primary key autoincrement,
            id_device text,
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

def connect_to_device0():
    global device0
    global keep_going0
    if device0 is not None:
        return device0
    log("Connecting to device0...")    
    try:
        device0 = serial.Serial("/dev/ttyUSB0",9600,timeout=1,writeTimeout=1)#tty se refiere que es terminal
	time.sleep(4)
    except:
        log("Connection error")
        keep_going0 = False
        sys.exit(500)
    log("Connected divice0")  
    time.sleep(0.1)
    return device0

def connect_to_device1():
    
    global device1
    global keep_going1
    if device1 is not None:
        return device1
    log("Connecting to device1...")    
    try:
        device1 = serial.Serial("/dev/ttyUSB1",9600,timeout=1,writeTimeout=1)#tty se refiere que es terminal
	time.sleep(4)
    except:
        log("Connection error")
        keep_going1 = False
        sys.exit(500)
    log("Connected divice1")  
    time.sleep(0.1)
    return device1

def disconnect_device():
    global device0
    global device1
    if device0 is not None:
        device0.close()
    if device1 is not None:
        device1.close()
    device0 = None
    device1 = None
    
def disconnect_database():
    db.close()

def get_average_sensors():
    global ad_sensors_0, ad_sensors_1
    sensors_average_0 = []
    sensors_average_1 = []
    for index in ad_sensors_0:
        if(len(index) == 0): continue
        avg0 = sum(index) / len(index)
        log(index)
        sensors_average_0.append(avg0)
        
        
    for index in ad_sensors_1:
        if(len(index) == 0): continue
        avg1 = sum(index) / len(index)
        log(index)
        sensors_average_1.append(avg1)
    print ("average 0")
#    log(sensors_average_0)
#    log(sensors_average_1)

    save_data_to_database(sensors_average_0,sensors_average_1)
    
    ad_sensors_0=[[],[],[],[],[],[],[],[],[],[],[]]
    ad_sensors_1=[[],[],[],[],[],[],[],[],[],[],[]]

def read_data_from_devices():
    global device_name_0, read_data_0,ad_sensors_0, ad_count_0
   
    read_data_0 = []

    
    device0 = connect_to_device0()
    device1 = connect_to_device1()
    
    
           
    try:
        device0.write("readall")
        time.sleep(0.1)
        
    except:
        sys.exit("500")
    line0 = ""
    device_name_0=device0.readline().strip()
    number_input_0=int(device0.readline().strip())
    for index in range (0,number_input_0):
        line0 = device0.readline()
        value0 = float(line0)
        read_data_0.append(line0)
        ad_sensors_0[index].append(value0)
        print str(device_name_0) + "sensor" + str(index) + str(value0)
#        
    # print device

     
        
        #conexion device1        
    global device_name_1, read_data_1, ad_sensors_1, ad_count_1
    read_data_1 = []
    try:
        device1.write("readall")
        time.sleep(0.1)
    except:
        sys.exit("500")
    line1 = ""       
    device_name_1=device1.readline().strip()
    number_input_1=int(device1.readline().strip())
    # print device
    for index in range (0,number_input_1):
        line1 = device1.readline()
        value1 = float(line1)
        read_data_1.append(line1)
        ad_sensors_1[index].append(value1)
        print str(device_name_1) + "sensor" + str(index) +str(value1)  
#    except:
#        sys.exit("500")
   
#    log(ad_sensors_1)
#    log(ad_sensors_0)
#    log(ad_sensors_2)
	
    
#    while (line != "EOF" and len(line) > 0):
 #       value = float(line)
#	
 #       read_data.append(line) 
  #      index = len(read_data) - 1
   #     ad_sensors[index].append(value)
    #    line = device.readline().strip()
    

    #log(ad_sensors)
    
    

def save_data_to_database(data0,data1):
    db = connect_to_database()
    for index in range(len(data0)):#index posicion del arreglo
        log("INSERT INTO MEASURE (id_device,id_sensor,value) VALUES " +str(device_name_0)+ str(index) + " , " + str(data0[index]))
        db.execute("INSERT INTO MEASURE (id_device,id_sensor,value) VALUES (?,?,?)",(device_name_0,index, data0[index]))
        #Grabar en un archivo de texto
    for index in range(len(data1)):#index posicion del arreglo
        log("INSERT INTO MEASURE (id_device,id_sensor,value) VALUES " +str(device_name_1)+ str(index) + " , " + str(data1[index]))
        db.execute("INSERT INTO MEASURE (id_device,id_sensor,value) VALUES (?,?,?)",(device_name_1,index, data1[index]))
        #Grabar en un archivo de texto
    disconnect_database()


def data_capture():
    if keep_going0:
        Timer(seconds_between_data_samples,data_capture).start()
    log("data capture")    
    read_data_from_devices()

def get_average_and_save():
    if keep_going0:
        Timer(seconds_between_average_calculation,get_average_and_save).start()    
    log("average calculation")
    get_average_sensors()
    

def rules_allow_continuation():
    global counter    
    counter = counter  +1
    return counter < 5 and keep_going0
    
def watch_dog():
    if keep_going0:
        Timer(seconds_between_watch_dog,watch_dog).start() 
    log("Watchdog is writing the file...")
    f = open ("/acquaniebla/log/acquaniebla.watchdog", "w")
    f.close()
    
    
def main():
    watch_dog()
    time.sleep(90)
    connect_to_database()
    Timer(seconds_between_data_samples,data_capture).start()
    Timer(seconds_between_average_calculation,get_average_and_save).start()
    
                 
 
main()
