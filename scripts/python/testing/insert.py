from database import Database

def main():
    try:
        print(
            """
            1. Player
            2. Team
            3. League
            """
        )
        method = input("Enter what type of row you want to add: ")

        # connect to database
        db = Database()

        # makes sure input is correct
        while method not in ['1', '2', '3']:
            method = input("Enter between 1 and 3: ")

        if method == '1':
            # goes through each trait of the player
            trait_list = ["first_name", "last_name", "middle_initial", "id", "position"]
            traits = {}

            # fill dict
            for trait in trait_list:
                traits[trait] = input(f"{trait}: ")

            # generates the player
            insert_player(
                database=db,
                first_name=traits["first_name"],
                last_name=traits["last_name"],
                middle_initial=traits["middle_initial"],
                id=traits["id"],
                position=traits["position"]
            )

        elif method == '2':
            # each trait of a team
            trait_list = ["name", "id", "year_founded", "country"]
            traits = {}

            # fill dict
            for trait in trait_list:
                traits[trait] = input(f"{trait}: ")

            # generate the team
            insert_team(
                database=db,
                name=traits["name"],
                id=traits["id"],
                year=traits["year_founded"],
                country=traits["country"]
            )

        elif method == '3':
            # each trait of a league
            trait_list = ["name", "id", "number_of_teams", "years_between_seasons", "year_founded"]
            traits = {}

            # fill dict
            for trait in trait_list:
                traits[trait] = input(f"{trait}: ")

            insert_league(
                database=db,
                name=traits["name"],
                id=traits["id"],
                year=traits["year_founded"],
                recurrence=traits["years_between_seasons"],
                num_teams=traits["number_of_teams"]
            )

    finally:
        # commit and close connection
        if db:
            db.end()

def format_insert(database: Database, query: str):

    # convert nonetypes to NULL and run query
    query = query.replace("'None'", "NULL")
    database.query(query)


def insert_player(database: Database, first_name=None, last_name = None, middle_initial=None, id=None, position=None):

    # generates sql insert
    query = (
        "INSERT INTO Player(first_name, last_name, middle_initial, player_id, field_position)" 
        f"VALUES ('{first_name}', '{last_name}', '{middle_initial}', '{id}', '{position}');"
    )
    
    # execute
    format_insert(database, query)

def insert_team(database: Database, id=None, name=None, year=None, country=None):
    
    # generates a sql insert
    query = (
        "INSERT INTO Team(team_id, team_name, year_founded, country)"
        f"VALUES ('{id}', '{name}', '{year}', '{country}');"
    )

    # execute
    format_insert(database, query)

def insert_league(database: Database, name=None, id=None, num_teams=None, recurrence=None, year=None):

    # generate sql insert
    query = (
        "INSERT INTO League(league_id, league_name, year_founded, recurrence, num_teams)"
        f"VALUES ('{id}', '{name}', '{year}', '{recurrence}', '{num_teams}');"
    )

    # execute
    format_insert(database, query)

if __name__ == "__main__":
    main()