from database import Database

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

# select 1 player
def selectPlayer(db):
    db.query("SELECT * FROM Player")
    print(db.cursor.fetchone())

# select all player-team relations
def selectPlayerTeams(db):
    db.query("SELECT p.first_name, p.last_name, t.team_name FROM Player p INNER JOIN PlayerTeam pt ON pt.player_id = p.player_id INNER JOIN Team t on t.team_id = pt.team_id")
    print(format(db.cursor.fetchall()))

# select all leagues
def selectLeagues(db):
    db.query("SELECT * FROM League")
    print(format(db.cursor.fetchall()))

def main():

    # creates database
    db = Database()

    # get type of function to run
    print(
        """
        1. Select 5 teams
        2. Select 1 player
        3. Select all player-team relations
        4. Select all leagues
        """
    )
    num = input("What function do you want to execute? ")

    if not num in ["1", "2", "3", "4"]:
        print("Invalid choice!")
    else:
        num = int(num)
        print()
        eval(["selectTeams", "selectPlayer", "selectPlayerTeams", "selectLeagues"][num-1] + "(db)")

    # closes connection
    db.end()

if __name__ == "__main__":
    main()