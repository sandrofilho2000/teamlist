from abc import update_abstractmethods
import os
import sys

from pytz import country_names

root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)

import traceback
from turtle import update
from numpy import save
import requests
import re
from bs4 import BeautifulSoup
import concurrent.futures

from slugify import slugify
from get_imgs import download_image
from passToFloat import pass_to_float

from sql_commands import insert_rows, select_rows, update_rows


def get_players(letter):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    players = select_rows("id, country_flag", f"players_player where country_flag like '%verysmall%' and name like '{letter}%'")
    
    for player in players:
        id = player[0]
        country_flag = player[1]
        country_flag = country_flag.replace("tiny", "verysmall")
        update_rows("players_player", f"country_flag='{country_flag}'", f"id={id}" )
        print("PAÍS ATUALIZADO")
                
functions_to_run = []               
                
import string
for letter in string.ascii_lowercase:
    # Add tuple with get_players function and current letter as parameter to the list
    functions_to_run.append((get_players, letter))


with concurrent.futures.ThreadPoolExecutor(max_workers=27) as executor:
    # Submit each function to the executor
    futures = [executor.submit(func, param) for func, param in functions_to_run]

    # Wait for all functions to complete
    concurrent.futures.wait(futures)

    # Optionally, retrieve the results if the functions return anything
    results = [future.result() for future in futures]