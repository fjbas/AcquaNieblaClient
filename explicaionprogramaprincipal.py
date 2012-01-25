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

ad_sensors=sensor_startup



import time


from threading import Timer

def log(message):					#imprime en pantalla lo que se le entregue, junto con la hora que en que se imprime
    moment = time.gmtime()    
    print time.strftime("[%Y-%m-%d %H:%M:%S ]",moment) + " " + str(message)
    
def connect_to_database():
    global db
    
    import sqlite3					#importo libreria
    db = sqlite3.connect('./measures.db')		#creo la conexion
    db.row_factory = sqlite3.Row			#permite trabjar los datos con cursor 
    db.isolation_level = None    			#permite realizar autocommit  
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
        """)						#crea tabla para medir los datos que de los censores SOLO si es que no existe la tabla
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
    import serial					#importa libreria serial
    global device
    
    if device is not None:				#conectar si no existe conexion
        return device
    log("Connecting to device...")    
    device = serial.Serial("/dev/ttyUSB0",9600,timeout=1,writeTimeout=1)#tty se refiere que es terminal
    log("Connected")  
    
    return device

def disconnect_device():				#desconecta el dispositivo
    global device
    if device is not None:
        device.close()
    device = None
    
def disconnect_database():
    db.close()

def get_average_sensors():				#obtiene promedios de la mediciones y lo guarda en a base de dato local
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
    device = connect_to_device() 				#inicia la conecion con el dispositivo
    line = ""       
    device.write("r")						#escribe r en el puerto serial para indicarle al dispositivo que lea e envie las mediciones

    line = device.readline().strip()				#remueve el salto de linea que probiene al final del valor de las mediciones
    
    while (line != "EOF" and len(line) > 0):			#lee cada una de las mediciones enviadas por el dispositivo
        value = float(line)
        read_data.append(line) 
        index = len(read_data) - 1
        ad_sensors[index].append(value)				#agrega al final de la linea el largo de la linea
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
    Timer(seconds_between_data_samples,data_capture).start()		#inicia arbol para llamar la funcion cada un segundo
    log("data capture")    						#imprime en pantalla que se inicio data capture
    read_data_from_device()						#lee datos del dispositivo

def get_average_and_save():
    Timer(seconds_between_average_calculation,get_average_and_save).start()    
    log("average calculation")
    get_average_sensors()
    

def rules_allow_continuation():
    global counter    
    counter = counter  +1
    return counter < 5
    

def main():
    time.sleep(120)
    connect_to_database()
    Timer(seconds_between_data_samples,data_capture).start()			#crea un arbol que llama a la funcion cada un segundo para recopilar datos
    Timer(seconds_between_average_calculation,get_average_and_save).start()	# llama a la funcion cada un minuto para guardar datos en la base
                 
        
        

main()
