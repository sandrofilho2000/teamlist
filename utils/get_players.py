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



players_link = []
teams_link_error = ""
players_link_error = ""


def get_player_img(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        div = soup.find("div", class_="data-header__profile-container")
        img = div.find("img").get("src")
        
        if img:
            return img
        
        else:
            return ""
        
    else:
        return ""

def get_players(url, slug, team_id = 0):
    global teams_link_error, players_link_error
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            soup = BeautifulSoup(response.content, "html.parser")
            team = {}
            header = soup.find("header", "data-header")
            header_li = header.find("div", "data-header__details").find_all("ul", "data-header__items")[1].find_all("li", "data-header__label")[1]
            stadium = {}
            
            try:
                stadium['name'] = header_li.find("a").text.strip()
                stadium['link'] = "https://www.transfermarkt.com.br"+header_li.find("a").get("href")
                stadium_id = select_rows("MAX(id)", "stadiums_stadium")[0][0]
                
                if stadium["link"]:
                    if not stadium_id:
                        stadium_id = 0
                        
                    insert_rows("stadiums_stadium", "(id, name, link)", f"""
                                    (
                                        "{stadium_id + 1}",
                                        "{stadium['name']}",
                                        "{stadium['link']}"
                                    )""")
                    
                    
                    update_rows("teams_team", f"id_stadium_id = '{stadium_id}'", f"id = {team_id}")
                    
            except: pass
            
            
            div = soup.find("div", class_="data-header__profile-container")
            main = soup.find("main")
            team["img"] = div.find("img").get("src")

            download_image(team["img"], f"{slug}{team_id}.png")

            
            try:
                table = main.find("div", class_="responsive-table")
                trs = table.find_all("tr")
                
                for tr in trs:
                    tr_table = tr.find("table")
                    if tr_table:
                        try:
                            player = {}
                            player["name"] = tr_table.find("td", "hauptlink").text.strip()
                            player["link"] = tr_table.find("a").get("href")
                            player["img"] = get_player_img("https://www.transfermarkt.com.br"+player["link"])
                            player["pos"] = tr_table.find_all('tr')[1].text.strip()
                            player["id_team_id"] = team_id
                            player["slug"] = slugify(player["name"])
                            player["num"] = tr.find_all("td", "zentriert")[0].text.strip()
                            player["birth"] = tr.find_all("td", "zentriert")[1].text.strip()
                            player["country_flag"] = tr.find_all("td", "zentriert")[2].find("img").get("src")
                            player["country_name"] = tr.find_all("td", "zentriert")[2].find("img").get("title")
                            player["value_market"] = pass_to_float(tr.find("td", "rechts").text.strip())
                            
                            
                            insert_rows("players_player", "(name, slug, img, link, pos, id_team_id, num, birth, country_flag, country_name, value_market)", f"""
                            (
                                "{player['name']}",
                                "{player['slug']}",
                                "{player['img']}",
                                "{player['link']}",
                                "{player['pos']}",
                                "{player['id_team_id']}",
                                "{player['num']}",
                                "{player['birth']}",
                                "{player['country_flag']}",
                                "{player['country_name']}",
                                "{player['value_market']}"
                            )""")
                            
                        except Exception as e:
                            players_link_error += """
                                {link}
                            """
                        
                            print(e)
            except Exception as e:
                # Handling the exception
                print("An error occurred:", e)
                traceback.print_exc()
                teams_link_error += """
                    {link}
                """
        except Exception as e:
            # Handling the exception
            print("An error occurred:", e)
            traceback.print_exc()
      
    





    

def get_stadium(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        







def get_players_a_letter():
    teams = select_rows("teams_team.id, teams_team.slug, teams_team.link ,teams_team.name", """teams_team
    LEFT JOIN players_player ON teams_team.id = players_player.id_team_id
    WHERE teams_team.name LIKE 'a%' 
    GROUP BY teams_team.id, teams_team.name
    HAVING COUNT(players_player.id) = 0""")


        
    for team in teams:
        id = team[0]
        slug = team[1]
        link = team[2]
        link = link.replace("br//", "/")
        link = link.replace("saison_id/2023", "")
        name = team[3]
        print(f"Adicionando jogadores do { name } ")
        get_players(link, slug, id)
        print(f"Jogadores do { name } adicionados")
    

    
    

def get_players_b_letter():
    teams = select_rows("teams_team.id, teams_team.slug, teams_team.link ,teams_team.name", """teams_team
    LEFT JOIN players_player ON teams_team.id = players_player.id_team_id
    WHERE teams_team.name LIKE 'b%' 
    GROUP BY teams_team.id, teams_team.name
    HAVING COUNT(players_player.id) = 0""")


        
    for team in teams:
        id = team[0]
        slug = team[1]
        link = team[2]
        link = link.replace("br//", "/")
        link = link.replace("saison_id/2023", "")
        name = team[3]
        print(f"Adicionando jogadores do { name } ")
        get_players(link, slug, id)
        print(f"Jogadores do { name } adicionados")
    
    
    

def get_players_c_letter():
    teams = select_rows("teams_team.id, teams_team.slug, teams_team.link ,teams_team.name", """teams_team
    LEFT JOIN players_player ON teams_team.id = players_player.id_team_id
    WHERE teams_team.name LIKE 'c%' 
    GROUP BY teams_team.id, teams_team.name
    HAVING COUNT(players_player.id) = 0""")


        
    for team in teams:
        id = team[0]
        slug = team[1]
        link = team[2]
        link = link.replace("br//", "/")
        link = link.replace("saison_id/2023", "")
        name = team[3]
        print(f"Adicionando jogadores do { name } ")
        get_players(link, slug, id)
        print(f"Jogadores do { name } adicionados")
    
    
    

def get_players_d_letter():
    teams = select_rows("teams_team.id, teams_team.slug, teams_team.link ,teams_team.name", """teams_team
    LEFT JOIN players_player ON teams_team.id = players_player.id_team_id
    WHERE teams_team.name LIKE 'd%' 
    GROUP BY teams_team.id, teams_team.name
    HAVING COUNT(players_player.id) = 0""")


        
    for team in teams:
        id = team[0]
        slug = team[1]
        link = team[2]
        link = link.replace("br//", "/")
        link = link.replace("saison_id/2023", "")
        name = team[3]
        print(f"Adicionando jogadores do { name } ")
        get_players(link, slug, id)
        print(f"Jogadores do { name } adicionados")
 
    

def get_players_e_letter():
    teams = select_rows("teams_team.id, teams_team.slug, teams_team.link ,teams_team.name", """teams_team
    LEFT JOIN players_player ON teams_team.id = players_player.id_team_id
    WHERE teams_team.name LIKE 'e%' 
    GROUP BY teams_team.id, teams_team.name
    HAVING COUNT(players_player.id) = 0""")


        
    for team in teams:
        id = team[0]
        slug = team[1]
        link = team[2]
        link = link.replace("br//", "/")
        link = link.replace("saison_id/2023", "")
        name = team[3]
        print(f"Adicionando jogadores do { name } ")
        get_players(link, slug, id)
        print(f"Jogadores do { name } adicionados")
 
    

def get_players_f_letter():
    teams = select_rows("teams_team.id, teams_team.slug, teams_team.link ,teams_team.name", """teams_team
    LEFT JOIN players_player ON teams_team.id = players_player.id_team_id
    WHERE teams_team.name LIKE 'f%' 
    GROUP BY teams_team.id, teams_team.name
    HAVING COUNT(players_player.id) = 0""")


        
    for team in teams:
        id = team[0]
        slug = team[1]
        link = team[2]
        link = link.replace("br//", "/")
        link = link.replace("saison_id/2023", "")
        name = team[3]
        print(f"Adicionando jogadores do { name } ")
        get_players(link, slug, id)
        print(f"Jogadores do { name } adicionados")
 
    

def get_players_g_letter():
    teams = select_rows("teams_team.id, teams_team.slug, teams_team.link ,teams_team.name", """teams_team
    LEFT JOIN players_player ON teams_team.id = players_player.id_team_id
    WHERE teams_team.name LIKE 'g%' 
    GROUP BY teams_team.id, teams_team.name
    HAVING COUNT(players_player.id) = 0""")


        
    for team in teams:
        id = team[0]
        slug = team[1]
        link = team[2]
        link = link.replace("br//", "/")
        link = link.replace("saison_id/2023", "")
        name = team[3]
        print(f"Adicionando jogadores do { name } ")
        get_players(link, slug, id)
        print(f"Jogadores do { name } adicionados")
 
    

def get_players_h_letter():
    teams = select_rows("teams_team.id, teams_team.slug, teams_team.link ,teams_team.name", """teams_team
    LEFT JOIN players_player ON teams_team.id = players_player.id_team_id
    WHERE teams_team.name LIKE 'h%' 
    GROUP BY teams_team.id, teams_team.name
    HAVING COUNT(players_player.id) = 0""")


        
    for team in teams:
        id = team[0]
        slug = team[1]
        link = team[2]
        link = link.replace("br//", "/")
        link = link.replace("saison_id/2023", "")
        name = team[3]
        print(f"Adicionando jogadores do { name } ")
        get_players(link, slug, id)
        print(f"Jogadores do { name } adicionados")
 
    

def get_players_i_letter():
    teams = select_rows("teams_team.id, teams_team.slug, teams_team.link ,teams_team.name", """teams_team
    LEFT JOIN players_player ON teams_team.id = players_player.id_team_id
    WHERE teams_team.name LIKE 'i%' 
    GROUP BY teams_team.id, teams_team.name
    HAVING COUNT(players_player.id) = 0""")


        
    for team in teams:
        id = team[0]
        slug = team[1]
        link = team[2]
        link = link.replace("br//", "/")
        link = link.replace("saison_id/2023", "")
        name = team[3]
        print(f"Adicionando jogadores do { name } ")
        get_players(link, slug, id)
        print(f"Jogadores do { name } adicionados")
 
    

def get_players_j_letter():
    teams = select_rows("teams_team.id, teams_team.slug, teams_team.link ,teams_team.name", """teams_team
    LEFT JOIN players_player ON teams_team.id = players_player.id_team_id
    WHERE teams_team.name LIKE 'j%' 
    GROUP BY teams_team.id, teams_team.name
    HAVING COUNT(players_player.id) = 0""")


        
    for team in teams:
        id = team[0]
        slug = team[1]
        link = team[2]
        link = link.replace("br//", "/")
        link = link.replace("saison_id/2023", "")
        name = team[3]
        print(f"Adicionando jogadores do { name } ")
        get_players(link, slug, id)
        print(f"Jogadores do { name } adicionados")
 
    

def get_players_k_letter():
    teams = select_rows("teams_team.id, teams_team.slug, teams_team.link ,teams_team.name", """teams_team
    LEFT JOIN players_player ON teams_team.id = players_player.id_team_id
    WHERE teams_team.name LIKE 'k%' 
    GROUP BY teams_team.id, teams_team.name
    HAVING COUNT(players_player.id) = 0""")


        
    for team in teams:
        id = team[0]
        slug = team[1]
        link = team[2]
        link = link.replace("br//", "/")
        link = link.replace("saison_id/2023", "")
        name = team[3]
        print(f"Adicionando jogadores do { name } ")
        get_players(link, slug, id)
        print(f"Jogadores do { name } adicionados")
 
    

def get_players_l_letter():
    teams = select_rows("teams_team.id, teams_team.slug, teams_team.link ,teams_team.name", """teams_team
    LEFT JOIN players_player ON teams_team.id = players_player.id_team_id
    WHERE teams_team.name LIKE 'l%' 
    GROUP BY teams_team.id, teams_team.name
    HAVING COUNT(players_player.id) = 0""")


        
    for team in teams:
        id = team[0]
        slug = team[1]
        link = team[2]
        link = link.replace("br//", "/")
        link = link.replace("saison_id/2023", "")
        name = team[3]
        print(f"Adicionando jogadores do { name } ")
        get_players(link, slug, id)
        print(f"Jogadores do { name } adicionados")
 
    

def get_players_m_letter():
    teams = select_rows("teams_team.id, teams_team.slug, teams_team.link ,teams_team.name", """teams_team
    LEFT JOIN players_player ON teams_team.id = players_player.id_team_id
    WHERE teams_team.name LIKE 'm%' 
    GROUP BY teams_team.id, teams_team.name
    HAVING COUNT(players_player.id) = 0""")


        
    for team in teams:
        id = team[0]
        slug = team[1]
        link = team[2]
        link = link.replace("br//", "/")
        link = link.replace("saison_id/2023", "")
        name = team[3]
        print(f"Adicionando jogadores do { name } ")
        get_players(link, slug, id)
        print(f"Jogadores do { name } adicionados")
 
    

def get_players_n_letter():
    teams = select_rows("teams_team.id, teams_team.slug, teams_team.link ,teams_team.name", """teams_team
    LEFT JOIN players_player ON teams_team.id = players_player.id_team_id
    WHERE teams_team.name LIKE 'n%' 
    GROUP BY teams_team.id, teams_team.name
    HAVING COUNT(players_player.id) = 0""")


        
    for team in teams:
        id = team[0]
        slug = team[1]
        link = team[2]
        link = link.replace("br//", "/")
        link = link.replace("saison_id/2023", "")
        name = team[3]
        print(f"Adicionando jogadores do { name } ")
        get_players(link, slug, id)
        print(f"Jogadores do { name } adicionados")
 
    

def get_players_o_letter():
    teams = select_rows("teams_team.id, teams_team.slug, teams_team.link ,teams_team.name", """teams_team
    LEFT JOIN players_player ON teams_team.id = players_player.id_team_id
    WHERE teams_team.name LIKE 'o%' 
    GROUP BY teams_team.id, teams_team.name
    HAVING COUNT(players_player.id) = 0""")


        
    for team in teams:
        id = team[0]
        slug = team[1]
        link = team[2]
        link = link.replace("br//", "/")
        link = link.replace("saison_id/2023", "")
        name = team[3]
        print(f"Adicionando jogadores do { name } ")
        get_players(link, slug, id)
        print(f"Jogadores do { name } adicionados")
 
    

def get_players_p_letter():
    teams = select_rows("teams_team.id, teams_team.slug, teams_team.link ,teams_team.name", """teams_team
    LEFT JOIN players_player ON teams_team.id = players_player.id_team_id
    WHERE teams_team.name LIKE 'p%' 
    GROUP BY teams_team.id, teams_team.name
    HAVING COUNT(players_player.id) = 0""")


        
    for team in teams:
        id = team[0]
        slug = team[1]
        link = team[2]
        link = link.replace("br//", "/")
        link = link.replace("saison_id/2023", "")
        name = team[3]
        print(f"Adicionando jogadores do { name } ")
        get_players(link, slug, id)
        print(f"Jogadores do { name } adicionados")
 
    

def get_players_q_letter():
    teams = select_rows("teams_team.id, teams_team.slug, teams_team.link ,teams_team.name", """teams_team
    LEFT JOIN players_player ON teams_team.id = players_player.id_team_id
    WHERE teams_team.name LIKE 'q%' 
    GROUP BY teams_team.id, teams_team.name
    HAVING COUNT(players_player.id) = 0""")


        
    for team in teams:
        id = team[0]
        slug = team[1]
        link = team[2]
        link = link.replace("br//", "/")
        link = link.replace("saison_id/2023", "")
        name = team[3]
        print(f"Adicionando jogadores do { name } ")
        get_players(link, slug, id)
        print(f"Jogadores do { name } adicionados")
 
    

def get_players_r_letter():
    teams = select_rows("teams_team.id, teams_team.slug, teams_team.link ,teams_team.name", """teams_team
    LEFT JOIN players_player ON teams_team.id = players_player.id_team_id
    WHERE teams_team.name LIKE 'r%' 
    GROUP BY teams_team.id, teams_team.name
    HAVING COUNT(players_player.id) = 0""")


        
    for team in teams:
        id = team[0]
        slug = team[1]
        link = team[2]
        link = link.replace("br//", "/")
        link = link.replace("saison_id/2023", "")
        name = team[3]
        print(f"Adicionando jogadores do { name } ")
        get_players(link, slug, id)
        print(f"Jogadores do { name } adicionados")
 
    

def get_players_s_letter():
    teams = select_rows("teams_team.id, teams_team.slug, teams_team.link ,teams_team.name", """teams_team
    LEFT JOIN players_player ON teams_team.id = players_player.id_team_id
    WHERE teams_team.name LIKE 's%' 
    GROUP BY teams_team.id, teams_team.name
    HAVING COUNT(players_player.id) = 0""")


        
    for team in teams:
        id = team[0]
        slug = team[1]
        link = team[2]
        link = link.replace("br//", "/")
        link = link.replace("saison_id/2023", "")
        name = team[3]
        print(f"Adicionando jogadores do { name } ")
        get_players(link, slug, id)
        print(f"Jogadores do { name } adicionados")
 
    

def get_players_t_letter():
    teams = select_rows("teams_team.id, teams_team.slug, teams_team.link ,teams_team.name", """teams_team
    LEFT JOIN players_player ON teams_team.id = players_player.id_team_id
    WHERE teams_team.name LIKE 't%' 
    GROUP BY teams_team.id, teams_team.name
    HAVING COUNT(players_player.id) = 0""")


        
    for team in teams:
        id = team[0]
        slug = team[1]
        link = team[2]
        link = link.replace("br//", "/")
        link = link.replace("saison_id/2023", "")
        name = team[3]
        print(f"Adicionando jogadores do { name } ")
        get_players(link, slug, id)
        print(f"Jogadores do { name } adicionados")
 
    

def get_players_u_letter():
    teams = select_rows("teams_team.id, teams_team.slug, teams_team.link ,teams_team.name", """teams_team
    LEFT JOIN players_player ON teams_team.id = players_player.id_team_id
    WHERE teams_team.name LIKE 'u%' 
    GROUP BY teams_team.id, teams_team.name
    HAVING COUNT(players_player.id) = 0""")


        
    for team in teams:
        id = team[0]
        slug = team[1]
        link = team[2]
        link = link.replace("br//", "/")
        link = link.replace("saison_id/2023", "")
        name = team[3]
        print(f"Adicionando jogadores do { name } ")
        get_players(link, slug, id)
        print(f"Jogadores do { name } adicionados")
 
    

def get_players_v_letter():
    teams = select_rows("teams_team.id, teams_team.slug, teams_team.link ,teams_team.name", """teams_team
    LEFT JOIN players_player ON teams_team.id = players_player.id_team_id
    WHERE teams_team.name LIKE 'v%' 
    GROUP BY teams_team.id, teams_team.name
    HAVING COUNT(players_player.id) = 0""")


        
    for team in teams:
        id = team[0]
        slug = team[1]
        link = team[2]
        link = link.replace("br//", "/")
        link = link.replace("saison_id/2023", "")
        name = team[3]
        print(f"Adicionando jogadores do { name } ")
        get_players(link, slug, id)
        print(f"Jogadores do { name } adicionados")
 
    
def get_players_w_letter():
    teams = select_rows("teams_team.id, teams_team.slug, teams_team.link ,teams_team.name", """teams_team
    LEFT JOIN players_player ON teams_team.id = players_player.id_team_id
    WHERE teams_team.name LIKE 'w%' 
    GROUP BY teams_team.id, teams_team.name
    HAVING COUNT(players_player.id) = 0""")


    for team in teams:
        id = team[0]
        slug = team[1]
        link = team[2]
        link = link.replace("br//", "/")
        link = link.replace("saison_id/2023", "")
        name = team[3]
        print(f"Adicionando jogadores do { name } ")
        get_players(link, slug, id)
        print(f"Jogadores do { name } adicionados")
    
    
def get_players_x_letter():
    teams = select_rows("teams_team.id, teams_team.slug, teams_team.link ,teams_team.name", """teams_team
    LEFT JOIN players_player ON teams_team.id = players_player.id_team_id
    WHERE teams_team.name LIKE 'x%' 
    GROUP BY teams_team.id, teams_team.name
    HAVING COUNT(players_player.id) = 0""")


    for team in teams:
        id = team[0]
        slug = team[1]
        link = team[2]
        link = link.replace("br//", "/")
        link = link.replace("saison_id/2023", "")
        name = team[3]
        print(f"Adicionando jogadores do { name } ")
        get_players(link, slug, id)
        print(f"Jogadores do { name } adicionados")
    
    
def get_players_y_letter():
    teams = select_rows("teams_team.id, teams_team.slug, teams_team.link ,teams_team.name", """teams_team
    LEFT JOIN players_player ON teams_team.id = players_player.id_team_id
    WHERE teams_team.name LIKE 'y%' 
    GROUP BY teams_team.id, teams_team.name
    HAVING COUNT(players_player.id) = 0""")


    for team in teams:
        id = team[0]
        slug = team[1]
        link = team[2]
        link = link.replace("br//", "/")
        link = link.replace("saison_id/2023", "")
        name = team[3]
        print(f"Adicionando jogadores do { name } ")
        get_players(link, slug, id)
        print(f"Jogadores do { name } adicionados")
    
    
def get_players_z_letter():
    teams = select_rows("teams_team.id, teams_team.slug, teams_team.link ,teams_team.name", """teams_team
    LEFT JOIN players_player ON teams_team.id = players_player.id_team_id
    WHERE teams_team.name LIKE 'z%' 
    GROUP BY teams_team.id, teams_team.name
    HAVING COUNT(players_player.id) = 0""")
 
 
functions_to_run = [
    ('a', get_players_a_letter),
    ('b', get_players_b_letter),
    ('c', get_players_c_letter),
    ('d', get_players_d_letter),
    ('e', get_players_e_letter),
    ('f', get_players_f_letter),
    ('g', get_players_g_letter),
    ('h', get_players_h_letter),
    ('i', get_players_i_letter),
    ('j', get_players_j_letter),
    ('k', get_players_k_letter),
    ('l', get_players_l_letter),
    ('m', get_players_m_letter),
    ('n', get_players_n_letter),
    ('o', get_players_o_letter),
    ('p', get_players_p_letter),
    ('q', get_players_q_letter),
    ('r', get_players_r_letter),
    ('s', get_players_s_letter),
    ('t', get_players_t_letter),
    ('u', get_players_u_letter),
    ('v', get_players_v_letter),
    ('w', get_players_w_letter),
    ('x', get_players_x_letter),
    ('y', get_players_y_letter),
    ('z', get_players_z_letter),
]  
    
    
with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    # Submit each function to the executor
    futures = [executor.submit(func) for letter, func in functions_to_run]

    # Wait for all functions to complete
    concurrent.futures.wait(futures)

    # Optionally, retrieve the results if the functions return anything
    results = [future.result() for future in futures]

# Output the results
for result in results:
    print(result)