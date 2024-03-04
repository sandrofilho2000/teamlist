import os
import sys
import traceback
from turtle import update
from numpy import save
import requests
import re
from bs4 import BeautifulSoup
import concurrent.futures
from slugify import slugify

root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)

from utils.passToFloat import pass_to_float
from utils.sql_commands import select_rows, update_rows

teams = select_rows("id, name, total_market_value", "teams_team WHERE total_market_value LIKE '%-%'")

for team in teams:
    try:
        new_value = pass_to_float(team[-1])
        
    except:
        print(team[-1])