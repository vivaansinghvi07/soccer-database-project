import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
from multiprocessing import Pool

def get_player_info(id):
    pass

def get_player_stats(id):

    GOALS_COL = "Unnamed: 6"
    GAMES_COL = "Unnamed: 5"
    ASSISTS_COL = "Unnamed: 7"
    CARDS_COL = "/ /"

    url = f"https://www.transfermarkt.co.uk/lionel-messi/leistungsdatendetails/spieler/{id}"
    headers = {'User-Agent': 
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

    # find table with information
    page = requests.get(url, headers=headers)

    print("Response Received.")

    main_table = None

    # find the table 
    tables = pd.read_html(page.text)
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
    with open("data/players.csv", "w") as f:
        for id in range(110_000):
            with Pool(10) as p:
                print("Process started.")
                print(p.map(get_player_stats, list(range(id*10, (id+1)*10))))