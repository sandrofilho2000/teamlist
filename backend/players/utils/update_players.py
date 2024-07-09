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

players = select_rows("id, name, value_market", "players_player WHERE value_market LIKE '%-%'")

for player in players:
    try:
        new_value = pass_to_float(player[-1])
        
    except:
        print(player[-1])