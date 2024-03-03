


import os
import sys
import traceback
from turtle import update
from numpy import insert, save
import requests
import re
from bs4 import BeautifulSoup
import concurrent.futures

from slugify import slugify

root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)

from teams.utils.get_imgs import download_image
from teams.utils.passToFloat import pass_to_float
from teams.utils.slugfy import *
from teams.utils.sql_commands import *
from googletrans import Translator

def translate_country_name_to_english(portuguese_country_name):
    # Create a Translator object
    translator = Translator()

    # Translate the country name from Portuguese to English
    translation = translator.translate(portuguese_country_name, src='pt', dest='en')

    # Return the translated text
    return translation.text

def select_rows(fields = "*", table = ""):
    conn = create_connection()    
    cur = conn.cursor()
    query = f"SELECT {fields} FROM {table}"
    print(query)
    cur.execute(query)

    rows = cur.fetchall()
    conn.close()
    return rows

countries = select_rows("""country_name, country_img, id""", """
leagues_league
""")


for country in countries:
    country_name = country[0]
    country_img = country[1]
    id = country[2]
    
    country_img = country_img.replace("tiny", "medium")
    
    update_rows("leagues_league", f"country_img = '{country_img}'", f"id = '{id}'")
    






