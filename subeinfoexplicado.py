# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 11:40:37 2011

@author: francisco"""

dbmysqlu=None
ide=None
id_sensor=None
measure_date=None
value=None
dbmysql=None




import sqlite3
import time
import MySQLdb
from urllib2 import Request,urlopen
import urllib

db=None
def connect_to_database():
    global db
    
    db = sqlite3.connect('./measures.db')
    db.row_factory = sqlite3.Row
    db.isolation_level = None    		#inicia auto commite
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
    


def set_token():
    
    db = connect_to_database()
    cursor = db.cursor()
    cursor.execute("Select value from CONFIGURATION where key = ?",["token"])
    
    result = cursor.fetchone()
    global token
    if result is not None:
        
        token = result[0]
        print "Token is " + token
        return 
    else:
        try:
            print "No token exists"
            #No tengo token asi que se lo pido a la web
            url = "http://1.androidtravellog.appspot.com/getvalue"
            request = Request(url,urllib.urlencode({'tag':'token'}))
            f = urlopen(request)
            response = f.read()
            token = response.split(',')[-1].replace('"','').replace(']','').strip()
            db.execute("INSERT INTO CONFIGURATION VALUES (?,?)",("token",token))
        except:
            log("Could not get token")
            token = "NO-TOKEN"
                    


def conet_mysql_u():
    print ("conectando")
    
    global dbmysqlu
    if dbmysqlu is not None:
        return dbmysqlu
            
    dbmysql = MySQLdb.connect(host='icc.uandes.cl', user='fbas',passwd='DD2mqGRjFHSKdUXJ',db="rs_fbas")
    dbmysqlu=dbmysql.cursor()
    
    return dbmysqlu
    
    
def up_data_mysqlu(data):
    conet_mysql_u()    
    dbmysqlu.execute("""
            CREATE TABLE  if not exists MEASURE        
            (
                id integer ,
                token varchar(255),
                id_sensor integer,
                measure_date text(20),
                value real
            );
            """)

    #dbmysqlu.execute('INSERT INTO MEASURE (id,id_sensor,measure_date,value) VALUES (?,?,?,?)',(int(ide),int(id_sensor),(measure_date),int(value))          )
    dbmysqlu.execute("insert INTO MEASURE (id,id_sensor,measure_date,value,token) values (%s,%s,%s,%s,%s)",
                     (  str(data["id"]),
                        str(data["id_sensor"]),
                        str(data["measure_date"]),
                        str(data["value"]),
                        str(data["token"])))
    #dbmysqlu.commit()


def log(message):
    moment = time.gmtime()    
    print time.strftime("[%Y-%m-%d %H:%M:%S ]",moment) + " " + str(message)
    
      
def send_data_to_server():
    
   
    query = "select * from measure where sent = 0"	#se busca los datos que no han sido enviado, ya que tienen un 0
    db = connect_to_database()				#inicia conexion con base de dato local
    cursor = db.cursor()
    cursor.execute(query)
    for row in cursor:
        output_data = {}
        for key in row.keys():
            output_data[key] = row[key]
        output_data['token'] = token
        log(output_data)     
        try:
            
            #SEND TO MYSQL            
            up_data_mysqlu(output_data)
            
            
            db.execute("UPDATE MEASURE SET sent = 1 where id = ?",[row['id']])
            #log ("UPDATE MEASURE SET sent = 1 where id = " + str(row['id']))
        except Exception as exc:
            log(str(exc))
     
    log("All rows sent")      
 

set_token()           
send_data_to_server()
