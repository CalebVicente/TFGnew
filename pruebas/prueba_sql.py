# -*- coding: utf-8 -*-
"""
Created on Sat May 30 17:36:11 2020

@author: cvicentm
"""



class Database:  
  
    
    def __init__(self):
        
        
        self.host = 'localhost'
        self.database = 'news_storage'
        self.user = 'root'
        self.password = 'tfg_project'
        
        

    def open(self):
        import mysql.connector
        self.connection = mysql.connector.connect(host= self.host,
                                                 database= self.database,
                                                 user=self.user,
                                                 password=self.password)
        
    def insert(self, value):
        from mysql.connector import Error
        
        try:
        
            sql_select_Query = "INSERT INTO prueba (name) VALUES ("+value+");"
            self.cursor = self.connection.cursor()
            self.cursor.execute(sql_select_Query)
            #without using commit function is imposible insert but it is not neccesary to do a select
            self.connection.commit()
        
        
        except Error as e:
            print("Error reading data from MySQL table", e)
            
    def selectAll(self):
        from mysql.connector import Error
        
        try:
        
            sql_select_Query = "SELECT * FROM prueba"
            self.cursor = self.connection.cursor()
            self.cursor.execute(sql_select_Query)
            
            return self.cursor.fetchall()
            #without using commit function is imposible insert but it is not neccesary to do a select        
        
        except Error as e:
            print("Error reading data from MySQL table", e)
    
    def close(self):
        
        if (self.connection.is_connected()):
            self.connection.close()
            self.cursor.close()
            print("MySQL connection is closed")



text = ["'david'", "'mama'", "'días'", "'que'"]


dbAdapter = Database()
dbAdapter.open() 
"""          
for value in text:
    dbAdapter.insert(value)
"""
result = dbAdapter.selectAll()
dbAdapter.close()