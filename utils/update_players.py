from sql_commands import select_rows, update_rows
from datetime import datetime
import concurrent.futures

from passToFloat import pass_to_float



stadiums = select_rows("id, name, build_value", f"stadiums_stadium where build_value like '%€%'")

for stadium in stadiums:
    build_value = pass_to_float(stadium[2])
    print(build_value)
    update_rows("stadiums_stadium", f"build_value = {build_value}", f"id = {stadium[0]}")


        
        
        
        
        
  