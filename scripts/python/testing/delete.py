from database import Database

# deletes all teams from a country
def deleteTeamsByCountry(db: Database, country: str):
    db.query(f"DELETE FROM Team WHERE country LIKE '%{country}%'")

# deletes all leagues 
def deleteLeagues(db: Database):
    db.query("DELETE FROM League")

# delete player-tema relations by player last name
def deletePlayersTeams(db: Database, last_name: str):
    db.query(f"DELETE FROM PlayerTeam pt WHERE player_id IN (SELECT player_id FROM Player WHERE last_name LIKE '%{last_name}%'")

if __name__ == "__main__":
    print(
        """
        1. Delete all teams from a country
        2. Delete all leagues 
        3. Delete all of a player's relations with a team
        """
    )
    method = input("Enter the function you want to do: ")

    # assures method is proper
    while method not in ['1', '2', '3']:
        method = input("Enter a number between 1 and 3: ")

    # creates database
    db = Database()

    if method == '1':
        country = input("Enter the country: ")
        deleteTeamsByCountry(db=db, country=country)
    elif method == '2':
        deleteLeagues(db=db)
    elif method == '3':
        last_name = input("Enter the player's last name: ")
        deletePlayersTeams(db=db, last_name=last_name)

    # commit and close
    db.end()