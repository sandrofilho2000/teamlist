import sqlite3
from sqlite3 import Error


def create_connection():
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(r"C:\xampp\htdocs\Not legacy\Python\Futeapp\db.sqlite3")

    except Error as e:
        print(e)
        
      
    return conn  
     
     
     
  
 
def select_rows(fields = "*", table = ""):
    conn = create_connection()    
    cur = conn.cursor()
    query = f"SELECT {fields} FROM {table}"
    cur.execute(query)

    rows = cur.fetchall()
    conn.close()
    return rows
  
 
def update_rows(table = "", set = "", where = ""):
    conn = create_connection()    
    cur = conn.cursor()
    
 
    query = f"""
    UPDATE {table}
    SET {set}
    WHERE {where}
    """
    
    print(query)
    cur.execute(query)
    conn.commit()
    conn.close()




