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
    print(query)
    rows = cur.fetchall()
    conn.close()
    return rows
     
  
 
def get_links():
    conn = create_connection()    
    cur = conn.cursor()
    query = f"""SELECT l.link, l.id, l.country_name, l.country_img, COUNT(t.id) AS num_teams
FROM leagues_league l
LEFT JOIN leagues_teams lt ON l.id = lt.id_league_id
LEFT JOIN teams_team t ON lt.id_team_id = t.id
GROUP BY l.id HAVING num_teams = 0;"""
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
    
    cur.execute(query)
    conn.commit()
    conn.close()




def insert_rows(table, fields, values):
    conn = create_connection()    
    cur = conn.cursor()
    
 
    query = f"""
    INSERT INTO {table} {fields}
    VALUES
    
    {values}


    """
    cur.execute(query)
    conn.commit()
    conn.close()
    
    

