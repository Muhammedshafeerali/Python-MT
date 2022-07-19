
"""This is the  dbsaveer module.

This module does Saving Prducts in to Database.
"""

import sqlite3

def save_to_db(records):
    try:
        
        sqliteConnection = sqlite3.connect('PRODDB.db') #connecting DATABASE
        cursor = sqliteConnection.cursor() #creating cursor object to execute SQLite command
        # print("Successfully Connected to SQLite")
        for each_record in records:
            sqlite_insert_query = """INSERT INTO PRODUCTS
                                (category, product) 
                                VALUES
                                {}
                                """.format(each_record)

            
            
            count = cursor.execute(sqlite_insert_query)
            sqliteConnection.commit()
            

        print("Records inserted successfully into PRODUCTS table ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")