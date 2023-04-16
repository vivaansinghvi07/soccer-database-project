from database import Database

def main():

    try:

        # creates database
        db = Database()

        # get type of function to run
        print(
            """
            1. Select 5 teams
            2. Select all player-team relations
            3. Select all leagues
            4. Select player by last name
            """
        )
        num = input("What function do you want to execute? ")

        if not num in ["1", "2", "3", "4"]:
            print("Invalid choice!")
        elif num == "4":
            selectPlayerByName(db, last_name=input("Enter the player's last name: "))
        else:
            num = int(num)
            print()
            eval(["selectTeams", "selectPlayerTeams", "selectLeagues"][num-1] + "(db)")

    finally:
        # closes connection
        if db:
            db.end()

# neatifies multiple rows
def format(ls):
    output = ""
    for row in ls:
        output += str(row) + "\n"
    return output     

# select 5 teams from the teams table
def selectTeams(db):
    db.query("SELECT * FROM Team")
    print(format(db.cursor.fetchmany(size=5)))

# select all player-team relations
def selectPlayerTeams(db):
    db.query("SELECT p.first_name, p.last_name, t.team_name FROM Player p INNER JOIN PlayerTeam pt ON pt.player_id = p.player_id INNER JOIN Team t on t.team_id = pt.team_id")
    print(format(db.cursor.fetchall()))

# select all leagues
def selectLeagues(db):
    db.query("SELECT * FROM League")
    print(format(db.cursor.fetchall()))

# select a player by their last name
def selectPlayerByName(db, last_name):
    db.query(f"SELECT * FROM Player WHERE last_name LIKE '%{last_name}%'")
    print(format(db.cursor.fetchall()))

if __name__ == "__main__":
    main()