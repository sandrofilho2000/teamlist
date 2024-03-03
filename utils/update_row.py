import os
import sys

from slugify import slugify

# Add the root directory of your Django project to the Python path
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)

from leagues.utils.sql_commands import *




leagues = select_rows("id, name", "leagues_league")


for league in leagues:
    id = league[0]
    slug = slugify(league[1])

    print("SLUG: ", slug)
    print(f"leagues_league", f"slug = {slug}" ,f"id = {id}")
    update_rows(f"leagues_league", f"slug = '{slug}'" ,f"id = {id}")    
