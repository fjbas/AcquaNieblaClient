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
import time    #Librería para obtener la hora
import urllib  # librería para acondicionar la información que se va a a mandar por internet. 
from urllib2 import Request,urlopen


def log(message):#  Función para imprimir el mensaje 
    moment = time.gmtime()  # obtengo la hora GMT  
    print time.strftime("[%Y-%m-%d %H:%M:%S ]",moment) + " " + message# imprimo en pantalla lo que le doy a la función y con la hora en que le dije que lo imprimiera 
    
def connect_to_database():# función para establecer la conexión con la base de datos 
    global db
    if db is not None: ############Esto hace que se comporte como singleton!
        return db
    
    import sqlite3
    db = sqlite3.connect('./measures.db')#Ocupo librería par importar la base de datos
    db.row_factory = sqlite3.Row #########3# toma los datos como tupla no como ?#########3# toma los datos como tupla no como ?
    db.isolation_level = None    # Implementa un modo auto commit, para evitar hacer commit después de cada transacción 
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
        """)#Crea la tabla si no existe 
    db.execute("""
        CREATE TABLE IF NOT EXISTS
        CONFIGURATION
        (
            key text primary key,
            value text
        )
    """)########################primary key parecido a autoincrement
    return db

def set_token(): 
# función que establece la conexión con el servidor y este le entrega un nombre de usuario para empezar a enviar datos en caso que ya tenga uno no lo pide
    
    db = connect_to_database()
    cursor = db.cursor()
    cursor.execute("Select value from CONFIGURATION where key = ?",["token"])############para que sirve el []
    
    result = cursor.fetchone()## Busca la fila siguiente de los resultados en la base de datos
    global token
    if result is not None:
        
        token = result[0]
        print "Token is " + token
        return 
    else:
        try:
            print "No token exists"
            #No tengo token asi que se lo pido a la web
            url = "http://1.androidtravellog.appspot.com/getvalue" ##Dirección del servidor 
            request = Request(url,urllib.urlencode({'tag':'token'}))########### guardo los datos como una tupla y el comando urllib.urlencode permite dejar en un formato estandar para enviar los datos a travez de internet. 

            f = urlopen(request)## conecto con el servidor
            response = f.read()
            token = response.split(',')[-1].replace('"','').replace(']','').strip()#### 
            db.execute("INSERT INTO CONFIGURATION VALUES (?,?)",("token",token))
        except:
            log("Could not get token")
            token = "NO-TOKEN"
            
def connect_to_device():# funcion que conecta el programa con el dispositivo de adquisición de datos 
    import serial
    global device
    
    if device is not None:
        return device
    log("Connecting to device...")    
    device = serial.Serial("/dev/ttyUSB0",9600,timeout=1,writeTimeout=1)#tty se refiere que es terminal
    log("Connected")  
    device.write("r")
    a=device.readline()#con esto me de medir una vez antes de empezar a ocupar los datos. Estos datos son desechados 
    b=device.readline()
    return device

def disconnect_device():#desconecto dispositivo
    global device
    if device is not None:
        device.close()
    device = None
    

def read_data_from_device():# funcion para leer  la información del dispositivo que esta conectado a los sensores. 
    device = connect_to_device() 
    device.write("r")
    
    a=device.readline()#read value of device
    b=device.readline()
    
    log ("a:" + str(a) + " b:" + str(b))
    global read_data
    read_data ={1:a,2:b}# guardo los datos comp tupla
    

def save_data_to_database():# funcion que guarda los datos en la base de dato local 
    db = connect_to_database()
    for index in read_data:#index posicion del arreglo
        log("INSERT INTO MEASURE (id_sensor,value) VALUES " + str(index) + " , " + str(read_data[index]))
        db.execute("INSERT INTO MEASURE (id_sensor,value) VALUES (?,?)",(index, read_data[index]))
        #Grabar en un archivo de texto

def send_data_to_server():#funcion encargada de pasar los datos de la base de dato local a la del servidor y registrar esta transacción en la base de dato local,
    
    url = "http://1.androidtravellog.appspot.com/storeavalue"    
    query = "select * from measure where sent = 0"
    db = connect_to_database()
    cursor = db.cursor()
    cursor.execute(query)
    for row in cursor:
        output_data = {}
        for key in row.keys():
            output_data[key] = row[key]
        output_data['token'] = token
        data_to_server = {'tag' : "anm_"+str(token)+ "_" + str(row['id']), 'value':output_data}      
        try:
            request = Request(url,urllib.urlencode(data_to_server))
            f = urlopen(request)
            print f.read()
            db.execute("UPDATE MEASURE SET sent = 1 where id = ?",[row['id']])
            #log ("UPDATE MEASURE SET sent = 1 where id = " + str(row['id']))
        except Exception as exc:
            log(str(exc))



def rules_allow_continuation():# funcion encargada de hacer que el programa corra bajo las condiciones especificada.
    global counter    
    counter = counter  +1
    return counter < 3
    

def main():
    connect_to_database()
    set_token()
    while rules_allow_continuation():
        read_data_from_device()
        save_data_to_database()
        
    send_data_to_server()             
        
        

main()