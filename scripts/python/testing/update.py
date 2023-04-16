from database import Database

def main():

    try:
        print(
            """
            1. Change player's position
            2. Change team's country
            """
        )
        method = input("Enter which function you would like to execute: ")

        # makes sure method is valid
        while method not in ['1', '2']:
            method = input("Enter either 1 or 2: ")

        # connects to database
        db = Database()
            
        # for player position
        if method == '1':

            last_name = input("Enter the player's last name: ")
            position = input("Enter the new position: ")

            # perform switch
            switch_player_position(
                db=db,
                last_name=last_name,
                new_pos=position
            )
            
        # for team country
        elif method == '2':

            name = input("Enter the team's name: ")
            country = input("Enter the new country: ")

            # perform switch
            switch_team_country(
                db=db,
                team_name=name,
                country=country
            )

    finally:
        # close connection and commit
        if db:
            db.end()

# sets position of any player containing given last name to new_pos
def switch_player_position(db: Database, last_name: str, new_pos: str):
    db.query(f"UPDATE Player SET field_position = '{new_pos}' WHERE last_name LIKE '%{last_name}%'")

# changes the country of team 
def switch_team_country(db: Database, team_name: str, country: str):
    db.query(f"UPDATE Team SET country = '{country}' WHERE team_name LIKE '%{team_name}%'") 

if __name__ == "__main__":
    main()