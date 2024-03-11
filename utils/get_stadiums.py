from math import exp
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

from sql_commands import insert_rows, select_rows, update_rows

root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

def get_stadium(url, team_name = "", stadium_name = ""):
    global teams_link_error, players_link_error, headers

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        crowd_capacity="" 
        seats= 0 
        staterooms = 0
        build_year="" 
        build_value = ""
        grass_heat="" 
        grass_type="" 
        grass_size="" 
        address="" 
        country_name="" 
        tickets_link="" 
        has_track="" 
        imgs="" 
        oficial_site = ""
        tickets_link = ""
        phone = ""
        
        try:
            
            table = soup.find_all("table", "profilheader")[0]
            trs = table.find_all("tr")
            
            for tr in trs:
                if "Capacidade total:" in tr.find('th'):
                    crowd_capacity = str(tr.find("td")).replace("<td>", "").replace("</td>", "").strip()

                elif "Cadeiras:" in tr.find('th'):
                    seats = str(tr.find("td")).replace("<td>", "").replace("</td>", "").strip()

                elif "Camarotes:" in tr.find('th'):
                    staterooms = str(tr.find("td")).replace("<td>", "").replace("</td>", "").strip()

                elif "Ano de construção:" in tr.find('th'):
                    build_year = str(tr.find("td")).replace("<td>", "").replace("</td>", "").strip()

                elif "Valor de construção:" in tr.find('th'):
                    build_value = str(tr.find("td")).replace("<td>", "").replace("</td>", "").strip()

                elif "Aquecimento do gramado:" in tr.find('th'):
                    grass_heat = str(tr.find("td")).replace("<td>", "").replace("</td>", "").strip()

                elif "Pista" in tr.find('th'):
                    has_track = str(tr.find("td")).replace("<td>", "").replace("</td>", "").strip()

                elif "Medidas do gramado:" in tr.find('th'):
                    grass_size = str(tr.find("td")).replace("<td>", "").replace("</td>", "").strip()

                elif "Gramado:" in tr.find('th'):
                    grass_type = str(tr.find("td")).replace("<td>", "").replace("</td>", "").strip()
        
        
        except:
            print("Erro ao adicionar informações principais")

    
        try:
            main = soup.find("div", "datenfakten-wappen")
            imgs_html = main.find_all("img")
            
            if(imgs_html):
                for img_html in imgs_html:
                    imgs += img_html.get("src") + "%%"
        except:
            print("Erro ao adicionar imagens")
                
        
        try:
            infos = soup.find_all("div", "content zentriert")[0]
            trs = infos.find_all("tr", "")
            for tr in trs:
                if "Tel:" in tr.find('th'):
                    phone = str(tr.find("td")).replace("<td>", "").replace("</td>", "").strip()
                    print(phone)
                    
                elif "Site oficial:" in tr.find('th'):
                    oficial_site = tr.find("a").get("href")
                    
                elif "Bilheteria" in tr.find('th'):
                    tickets_link = tr.find("a").get("href")
        except Exception as e:
            print(str(e))
            print("Erro ao adicionar informações laterais")
            
        stadium = {
            "crowd_capacity": crowd_capacity, 
            "seats": seats, 
            "staterooms": staterooms,
            "build_year": build_year, 
            "build_value": build_value,
            "grass_heat": grass_heat, 
            "grass_type": grass_type, 
            "grass_size": grass_size, 
            "address": address, 
            "country_name": country_name, 
            "tickets_link": tickets_link, 
            "has_track": has_track, 
            "imgs": imgs, 
            "oficial_site": oficial_site,
            "tickets_link": tickets_link,
            "phone": phone,
            "team_name": team_name,
        }
        
        
        insert_rows("stadiums_stadium", """
                        (
                        name,
                        crowd_capacity,
                        seats,
                        link,
                        staterooms,
                        build_year,
                        build_value,
                        grass_heat,
                        grass_type,
                        grass_size,
                        address,
                        country_name,
                        tickets_link,
                        has_track,
                        imgs,
                        oficial_site,
                        tickets_link,
                        phone,
                        team_name)""",
                        
                        f"""(
                            "{stadium_name}",
                            "{crowd_capacity}",
                            "{seats}",
                            "{url}",
                            "{staterooms}",
                            "{build_year}",
                            "{build_value}",
                            "{grass_heat}",
                            "{grass_type}",
                            "{grass_size}",
                            "{address}",
                            "{country_name}",
                            "{tickets_link}",
                            "{has_track}",
                            "{imgs}",
                            "{oficial_site}",
                            "{tickets_link}",
                            "{phone}",
                            "{team_name}"
                        )
                        
                        """)
        
        
        print(f"Estádio {stadium_name} adicionado\n")
        
    
def get_stadiums(letter):
    teams = select_rows("id, link, name", f"teams_team where id_stadium_id is null and name like '{letter}%'")
    for team in teams:
        if teams:
            team_id = team[0]
            link = team[1].replace(".br//", ".br/")
            team_name = team[2]
            response = requests.get(link, headers=headers)
            soup = BeautifulSoup(response.content, "html.parser")
            div = soup.find("div", "data-header__details")
            lis = div.find_all("li", "data-header__label")
            
            stadium_link = ""
            for li in lis:
                if 'Estádio:' in li.text.strip():
                    if li.find("a"):
                        stadium_link = li.find("a").get("href")
                        stadium_name = li.find("a").text.strip()
                    
            if stadium_link:
                stadium_link = "https://www.transfermarkt.com.br"+stadium_link
                get_stadium(stadium_link, team_name, stadium_name)
                                
            else:
                update_rows("teams_team", f"id_stadium_id = ''", "id = '{max_id}'")


functions_to_run = []               
                
import string
for letter in string.ascii_lowercase:
    # Add tuple with get_players function and current letter as parameter to the list
    functions_to_run.append((get_stadiums, letter))


with concurrent.futures.ThreadPoolExecutor(max_workers=27) as executor:
    # Submit each function to the executor
    futures = [executor.submit(func, param) for func, param in functions_to_run]

    # Wait for all functions to complete
    concurrent.futures.wait(futures)

    # Optionally, retrieve the results if the functions return anything
    results = [future.result() for future in futures]