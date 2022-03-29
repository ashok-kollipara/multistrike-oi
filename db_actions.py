#!/usr/bin/python3
import os
import sqlite3
import time
from json_handler import get_oi, get_OC_json

#standardize database file location

path = os.getcwd()
db_name = 'multistrike_oi.db'

#clear stdout and give correct separator
if os.name == 'nt':
    os.system('cls')
    file_path= os.getcwd() +'\\'+ db_name 

else:
    os.system('clear')
    file_path= os.getcwd() +'/'+ db_name 


def check_db():

    global file_path

    #check database available
    file_list = os.listdir(path)

    if db_name in file_list:

        #reset db table data and start populating new data
        print('Database exists \nResetting table data')
        reset_table_data()

    else:

        #create a new db and start the process

        print('Database doesnot exist\nCreating a new one..! in ' + path)

        connection = sqlite3.connect(file_path)

        cursor=connection.cursor()

        #create tables command
        command = "create table oi(time, strike1, strike2)"
        cursor.execute(command)

        returned = cursor.execute("select * from oi")

        print ("Refreshed just now..")
        for item in returned:
            print (item)

        connection.close()


def populate_db(index_name, expiry, contract1, contract2):

    global file_path
    connection = sqlite3.connect(file_path)

    cursor=connection.cursor()

    #add values to tables command
    cursor.execute(
            "insert into oi values (?,?,?)", 
                        (
                        time.strftime('%H:%M'),
                        get_oi(expiry, contract1),
                        get_oi(expiry, contract2),
                        )
                    )
    time.sleep(1)
        
    #commit data write in db and save it
    connection.commit()

    returned = cursor.execute("select * from oi")

    for item in returned:
        print (item)

    connection.close()

    get_OC_json(index_name)


def fetch_data():

    global file_path
    connection = sqlite3.connect(file_path)

    cursor=connection.cursor()

    returned = cursor.execute("select * from oi")

    time_data, strike1_oi, strike2_oi = [], [], []

    for item in returned:
        time_data.append(item[0])
        strike1_oi.append(item[1])
        strike2_oi.append(item[2])

    connection.close()

    return time_data, strike1_oi, strike2_oi


def reset_table_data():

    global file_path
    connection = sqlite3.connect(file_path)

    cursor=connection.cursor()

    cursor.execute("delete from oi")

    connection.commit()

    connection.close()


