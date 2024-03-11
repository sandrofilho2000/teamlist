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

def insert_rows(table, fields, values, show_query=False):
    conn = create_connection()    
    cur = conn.cursor()
    
 
    query = f"""
    INSERT INTO {table}
    {fields}
    VALUES
    {values}
    """
    
    if show_query:
        print(query)
    
    cur.execute(query)
    conn.commit()
    conn.close()
    
    
  
 
def select_rows(fields = "*", table = "", show_query = False):
    conn = create_connection()    
    cur = conn.cursor()
    query = f"SELECT {fields} FROM {table}"
    if show_query:
        print(query)
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    return rows
  
 
def update_rows(table = "", set = "", where = "", show_query = False):
    conn = create_connection()    
    cur = conn.cursor()
    
    table = table.lower().replace("table", "")
    set = set.lower().replace("set", "")
    where = where.replace("where", "").replace("WHERE", "")
    query = f"""
    UPDATE {table}
    SET {set}
    WHERE {where}
    """
    
    if show_query:
        print(query)
    
    cur.execute(query)
    conn.commit()
    conn.close()




