import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
from multiprocessing import Pool
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome('/path/to/your/chromedriver', options=options)

HEADERS = {'User-Agent': 
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

def get_player_info(id):

    try:

        dates = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

        def process_date(date):
            if date == "":
                return date
            month, day, year = re.split("[, ]+", date)
            month = dates.index(month)
            return f"{year}-{month}-{day}"
        
        SEARCH = "data-header__label"
        NAME = "data-header__headline-wrapper"
        url = f"https://www.transfermarkt.co.uk/lionel-messi/profil/spieler/{id}"

        page = driver.get(url)
        #page = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(page.page_source, features="lxml")

        qualities = soup.find_all('li', {'class': SEARCH})

        date_str = ''
        country = ''
        position = ''
        
        for quality in qualities:
            text = quality.text
            if "Date of birth" in text:     # get date of birth
                for word in text.split("\n"):
                    if "," in word.strip():
                        date_str = re.sub('\(..\)', '', word).strip()
            elif "Citizenship" in text:
                country = text.replace("Citizenship:", '').strip()
            elif "Position" in text:
                position = text.replace("Position:", '').strip().replace("Centre", "Center")

        name = soup.find_all('h1', {'class': NAME})[0].text.strip()
        names = name.split()

        first_name = ''
        last_name = ''
        middle_initial = ''
        
        if len(names) == 2:
            last_name = names[1]
            first_name = names[0]
        elif len(names) == 3:
            last_name = names[2]
            first_name = names[0]
            middle_initial = names[1][0].upper()
        elif len(names) == 1:
            last_name = names[0]
        else:
            first_name = names[0]
            middle_initial = names[1][0].upper()
            last_name = " ".join(names[2::])

        return {
            "id": id,
            "first_name": first_name,
            "last_name": last_name,
            "middle_initial": middle_initial,
            "country": country,
            "date_of_birth": process_date(date_str),
            "position": position
        } | _get_player_stats(id)

    except:

        return None


def _get_player_stats(id):

    GOALS_COL = "Unnamed: 6"
    GAMES_COL = "Unnamed: 5"
    ASSISTS_COL = "Unnamed: 7"
    CARDS_COL = "/ /"

    url = f"https://www.transfermarkt.co.uk/lionel-messi/leistungsdatendetails/spieler/{id}"
    

    # find table with information
    page = driver.get(url)
    # page = requests.get(url, headers=HEADERS)

    print("Response Received.")

    main_table = None

    # find the table 
    tables = pd.read_html(page.page_source)
    print("Table read.")
    for table in tables:
        if "Season" in table:
            main_table = table
    if main_table is None:
        return {
            "games": '',
            "goals": '',
            "assists": '',
            "cards": ''
        }

    # fetch information from dataframe
    try:
        total_games = main_table[GAMES_COL].values[-1].replace("-", "")
    except:
        total_games = ''
    try:
        total_goals = main_table[GOALS_COL].values[-1].replace("-", "")
    except:
        total_goals = ''
    try:
        total_assists = main_table[ASSISTS_COL].values[-1].replace("-", "")
    except:
        total_assists = ''
    try:
        cards_str = main_table[CARDS_COL].values[-1]
    except:
        cards_str = ''
    try:
        total_cards = sum(map(int, re.split("[\s\xa0/-]+", cards_str)))
    except:
        total_cards = ''

    print("Data processed.")

    return {
        "games": total_games,
        "goals": total_goals,
        "assists": total_assists,
        "cards": total_cards
    }

if __name__ == "__main__":
    fieldnames = [ "id", "first_name", "middle_initial", "last_name", "position", "date_of_birth", "country", "games", "goals", "assists", "cards"]
    with open("data/players.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        for id in range(110_000):
            with Pool(10) as p:
                print("Process started.")
                d = p.map(get_player_info, list(range(id*10, (id+1)*10)))
            for thing in d:
                if thing == None:
                    continue
                else:
                    writer.writerow(thing)