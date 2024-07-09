import requests
from bs4 import BeautifulSoup


links = [
    "/transfers/transfersalden/statistik?ajax=yw1&amp;kontinent_id=0&amp;land_id=0&amp;nat=0&amp;page=2&amp;plus=1&amp;pos=&amp;sa=&amp;saison_id=2023&amp;saison_id_bis=2023&amp;w_s=w",
    "/transfers/transfersalden/statistik?ajax=yw1&%3Bkontinent_id=0&%3Bland_id=0&%3Bnat=0&%3Bpage=2&%3Bplus=1&%3Bpos=&%3Bsa=&%3Bsaison_id=2023&%3Bsaison_id_bis=2023&%3Bw_s=w&page=2",
    "/transfers/transfersalden/statistik?ajax=yw1&%3Bkontinent_id=0&%3Bland_id=0&%3Bnat=0&%3Bpage=2&%3Bplus=1&%3Bpos=&%3Bsa=&%3Bsaison_id=2023&%3Bsaison_id_bis=2023&%3Bw_s=w&page=3",
    "/transfers/transfersalden/statistik?ajax=yw1&%3Bkontinent_id=0&%3Bland_id=0&%3Bnat=0&%3Bpage=2&%3Bplus=1&%3Bpos=&%3Bsa=&%3Bsaison_id=2023&%3Bsaison_id_bis=2023&%3Bw_s=w&page=4",
    "/transfers/transfersalden/statistik?ajax=yw1&%3Bkontinent_id=0&%3Bland_id=0&%3Bnat=0&%3Bpage=2&%3Bplus=1&%3Bpos=&%3Bsa=&%3Bsaison_id=2023&%3Bsaison_id_bis=2023&%3Bw_s=w&page=5",
    "/transfers/transfersalden/statistik?ajax=yw1&%3Bkontinent_id=0&%3Bland_id=0&%3Bnat=0&%3Bpage=2&%3Bplus=1&%3Bpos=&%3Bsa=&%3Bsaison_id=2023&%3Bsaison_id_bis=2023&%3Bw_s=w&page=6",
    "/transfers/transfersalden/statistik?ajax=yw1&%3Bkontinent_id=0&%3Bland_id=0&%3Bnat=0&%3Bpage=2&%3Bplus=1&%3Bpos=&%3Bsa=&%3Bsaison_id=2023&%3Bsaison_id_bis=2023&%3Bw_s=w&page=7",
    "/transfers/transfersalden/statistik?ajax=yw1&%3Bkontinent_id=0&%3Bland_id=0&%3Bnat=0&%3Bpage=2&%3Bplus=1&%3Bpos=&%3Bsa=&%3Bsaison_id=2023&%3Bsaison_id_bis=2023&%3Bw_s=w&page=8",
    "/transfers/transfersalden/statistik?ajax=yw1&%3Bkontinent_id=0&%3Bland_id=0&%3Bnat=0&%3Bpage=2&%3Bplus=1&%3Bpos=&%3Bsa=&%3Bsaison_id=2023&%3Bsaison_id_bis=2023&%3Bw_s=w&page=9",
    "/transfers/transfersalden/statistik?ajax=yw1&%3Bkontinent_id=0&%3Bland_id=0&%3Bnat=0&%3Bpage=2&%3Bplus=1&%3Bpos=&%3Bsa=&%3Bsaison_id=2023&%3Bsaison_id_bis=2023&%3Bw_s=w&page=10"
]


def get_teams_img(url):
    leagues = []

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all divs with class "TeamLinks flex items-center"
        header = soup.find("div", "data-header__profile-container")
        img = header.find("img").get("src")

        return img


def get_leagues():
    leagues = []
    
    sql_command = """
    DROP TABLE leagues_league ;
    CREATE TABLE leagues_league (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(255) NOT NULL,
            link VARCHAR(255) NOT NULL,
            small_img VARCHAR(255) NOT NULL,
            img VARCHAR(255) NOT NULL, 
            outcomes REAL,
            incomes REAL,
            balance REAL,
            country_img VARCHAR(255) NOT NULL,
            country_name VARCHAR(255) NOT NULL
    );
    
    INSERT INTO leagues_league (name, link, small_img, img, outcomes, incomes, balance, country_img, country_name)
    VALUES 
    
"""

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    for link in links:
        response = requests.get(
            f"https://www.transfermarkt.com.br{link}",
            headers=headers,
        )

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.content, "html.parser")

            # Find all divs with class "TeamLinks flex items-center"
            table = soup.find("table", class_="items")
            trs = table.find_all("tr")
            for tr in trs:
                league = {}
                td = tr.find("td", "hauptlink no-border-links")
                td_image = tr.find("td", "no-border-rechts zentriert")

                try:
                    td_outcomes = tr.find_all("td", "rechts")[0]
                    td_incomes = tr.find_all("td", "rechts")[1]
                    td_balance = tr.find_all("td", "rechts")[2]
                except:
                    print("No elements found")

                if td_image and td and td_outcomes and td_incomes and td_balance:
                    league["small_img"] = td_image.find("img").get("src")
                    league["name"] = td.text.strip()
                    league["link"] = "https://www.transfermarkt.com.br" + td.find(
                        "a"
                    ).get("href")
                    league["link"] = league["link"].replace(
                        "transferrekorde", "startseite"
                    )
                    league["img"] = get_teams_img(league["link"])
                    league["outcomes"] = td_outcomes.text.strip()
                    league["incomes"] = td_incomes.text.strip()
                    league["balance"] = td_balance.text.strip()

                    if td.find("a", "hauptlink no-border-links"):
                        league["link"] = td.find("a", "hauptlink no-border-links").get(
                            "href"
                        )
                        response = requests.get(league["link"], headers=headers)

                    if td.find("img"):
                        league["country_img"] = td.find("img").get("src")
                        league["country_name"] = td.find("img").get("title")
                        
                        
                    if league["name"]:
                        sql_command += f"""
                            (
                            '{league["name"]}',
                            '{league["link"]}',
                            '{league["small_img"]}',
                            '{league["img"]}',
                            '{league["outcomes"]}',
                            '{league["incomes"]}',
                            '{league["balance"]}',
                            '{league["country_img"]}',
                            '{league["country_name"]}'
                            ) ,               
                        """

                        print(f'Liga {league["name"]} Adicionada!') 

               
                

        else:
            print("Failed to retrieve webpage.")

    # Define o nome do arquivo
    file_name = "leagues.sql"

    # Escreve o valor de sql_command no arquivo usando UTF-8
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(sql_command)
        
    print("Script Finalizado!")
    return leagues


get_leagues()
