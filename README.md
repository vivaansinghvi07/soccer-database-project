# Soccer Database Project
This will database will store information all about soccer, such as leagues, teams, players, matches played, and much more. With this project, I aim to provide easily accessible information all about soccer. People will be able to analyze anything from details about matches from 20 years ago, to the salaries of the top 5 most well-paid players in the scene. 

The tables used in this project include those describing a(n):
  - **League**
  - **League History** - a recount of a particular season
  - **Team**
  - **Team Standing** - how a team performed in a season
  - **Team Standing Stat** - the team's statistics in a season
  - **Match**
  - **Player**
  - **Player Award** - keeps track of who won what
  - **Player Team** - keeps track of the teams that a player is in
  - **Player Stat** - a players in-game stats
  - **Award**

## Requirements: 
- PostGreSQL 15
- PGAdmin4
- Lucid Chart (For ERD)
- MacOS for implementation

## Tables: 

- **<i>Primary Key</i>**
- **Foregin Key**

**Team Standing** - this table helps keep track of how a team performed in a certain season - such as Arsenal’s performance in the Premier League in the 2018-19 season
  - **<i>standing_id</i>**
  - team_id  - relates to team_id in TEAM table
  - **league_id** - relates to league_id in LEAGUE table
  - **season_id** - relates to season_id in LEAGUEHISTORY table

**Team Standing Stat** - this table keeps track of the team's performance during a season, as a somewhat branch of the TEAMSTANDINGSTAT table
  - **<i>stat_id</i>**
  - games_played
  - wins
  - draws
  - losses
  - goals_scored
  - goals_lost
  - goal_difference
  - **standing_id** - relates to standing_id in TEAM STANDING table

**League History** - this table keeps track of who won each season in the league. Such as: who won the Premier league in the 2017-18 season
  - **<i>season_id</i>**	
  - season_year	
  - revenue
  - viewership
  - **league_id** - relates to league_id in LEAGUE table
  - **team_winning_id** - relates to team_id in TEAM table
  - **mvp_id** - relates to player_id in PLAYER table

**League** - this table keeps information of each league that I am looking at - such as when the Premier League was founded, how often it occurs, etc. Note: Recurrence represents the number of years between seasons of the league
  - **<i>league_id</i>** 
  - year_founded  
  - league_name 
  - num_teams   
  - recurrence 

**Match** - this table is the largest and keeps information on every match for every league that I am looking at - you will be able to find the data of every soccer game that happened
  - **<i>match_id</i>**
  - date_played
  - goals_team1   
  - goals_team2
  - outcome
  - **league_id** - relates to league_id in LEAGUE table
  - **team2_id** - relates to team_id in TEAM table
  - **team1_id** - relates to team_id in TEAM table

**Player** - this table keeps track of all the players in soccer and their various details - such as what Messi’s earnings are, what his awards are, what team(s) he plays for, and how many goals and assists he has made
  - **<i>player_id</i>**
  - first_name
  - last_name
  - middle_initial 
  - field_position
  - date_of_birth

**Player Stat** - this table keeps track of the player's in-game statistics, similar to how the TEAMSTAT table relates to TEAMSTANDINGSTAT
  - **<i>stat_id</i>**
  - games_played
  - goals  
  - assists
  - cards
  - **player_id** - relates to player_id in PLAYER table

**Player Team** - since players can be on multiple teams, this keeps track of what teams the player in question is in. Each row features one player-team relation. The addition of this table also has the feature where you can see what players are on a team
  - **<i>playerteam_id</i>**
  - date_joined
  - earnings
  - **team_id** - relates to team_id in TEAM table
  - **player_id** - relates to player_id in PLAYER table

**Player Award** - this table stores each award that was won by a player and also lists the player next to that award
  - **<i>playeraward_id</i>**
  - date_awarded
  - **award_id** - relates to award_id in AWARD table
  - **player_id** - relates to player_id in PLAYER table

**Teams** - this table keeps track of teams and information about them - such as when Manchester United was founded, and what league it plays in
  - **<i>team_id</i>** 
  - team_name 
  - year_founded
  - country  

**Award** - stores information about various awards in soccer - such as when the Ballon-D’or was started, a description of it, and how many times it was given
  - **<i>award_id</i>**
  - award_name
  - year_created	
  - times_given
  - award_desc

## ERD: 
![ERD](ERD.png)

## To Create The Database:
- Open PGAdmin4 and create a database
- Run the [create.sql](/scripts/create.sql) query to create the tables

## Use Cases:
- **League**:  
  - Finding the league/competition that happens the least frequently
    - `SELECT league_name, MAX(recurrence) AS years_per_season FROM League`
    - `SELECT league_name FROM League WHERE recurrence IN (SELECT MAX(recurrence) FROM League)`
  - Finding the oldest league
    - `SELECT league_name, MIN(year_founded) AS oldest_year FROM League`
    - `SELECT league_name FROM League WHERE year_founded IN (SELECT MIN(year_founded) FROM League)`
  - Finding the number of teams playing in the world cup
    - `SELECT league_name, num_teams FROM League WHERE league_name LIKE '%world%'`
- **Team**
  - Sorting teams by win count
    - `SELECT team_name, wins FROM Team ORDER BY wins DESC`
  - Finding all the teams that are based in England
    - `SELECT team_name FROM Team WHERE country LIKE '%england%'`
  - Getting the league (if any) of the oldest team in the database
    - `SELECT t.team_name, t.year_founded, l.league_name FROM Team t LEFT JOIN League l ON t.league_id = l.league_id WHERE t.year_founded IN (SELECT MAX(year_founded) FROM Team)`
- **Award**
  - Selecting the rarest award
    - `SELECT award_name, MIN(times_given) AS fewest_times_given FROM Award`
  - Finding the description of the ballon d'or
    - `SELECT award_desc FROM Award WHERE award_name LIKE '%ballon d'or%'`
  - Finding the most recently created award
    - `SELECT award_name, award_desc, MIN(year_created) AS year_created FROM Award`
- **Player** and **PlayerStat**
  - Arranging players by salary
    - `SELECT first_name, last_name, year_salary FROM Player ORDER BY year_salary DESC`
  - Finding the stats of a player (ex: Messi)
    - `SELECT p.first_name, p.last_name, ps.* FROM Player p INNER JOIN PlayerStat ps ON p.player_id = ps.player_id WHERE p.last_name LIKE '%messi%'`
  - Finding the player with the highest goals scored
    - `SELECT p.first_name, p.last_name, MAX(ps.goals) AS goals_scored FROM Player p INNER JOIN PlayerStat ps ON p.player_id = ps.player_id`
  - Finding the highest number of games played
    - `SELECT MAX(games_played) AS highest_games_played FROM Player Stat`
  - Finding the players with less than 100 matches
    - `SELECT p.first_name, p.last_name, ps.games_played FROM Player p INNER JOIN PlayerStat ps ON p.player_id = ps.player_id WHERE ps.games_played < 100`
- **Match**
  - Finding the number of matches that have had more than 8 goals
    - `SELECT COUNT(*) AS count FROM Match WHERE goals_team1 > 8 OR goals_team2 > 8`
  - Finding the matches that happened between specific dates (01-01-2001 and 02-01-2001)
    - `SELECT * FROM Match WHERE date_played BETWEEN '2001-01-01' AND '2001-02-01'`
  - Finding the highest scoring home teams that played in the 2018 season of the premier league
    - `SELECT TOP 5 * FROM Match WHERE season_id IN (SELECT season_id FROM LeagueHistory WHERE league_id = 'PRM' AND season_year = 2018) ORDER BY goals_home DESC`
- **TeamStat** and **TeamStandingStat**
  - Finding the team with the best goal difference in their 2020 season
    - `SELECT t.team_name, MAX(tst.goal_difference) as best_goal_difference FROM Team t INNER JOIN TeamStandingStat ts ON t.team_id = ts.team_id INNER JOIN TeamStat tst ON ts.stat_id = tst.stat_id WHERE ts.season_year = 2020`
  - Finding the highest goals scored by any team
    - `SELECT MAX(goals_scored) AS highest_goals_scored FROM TeamStat`
  - Finding a team's (Manchester City) stats in a certain season
    - `SELECT tst.* FROM TeamStandingStat ts INNER JOIN TeamStat tst ON ts.standing_id = tst.standing_id WHERE ts.team_id IN (SELECT team_id FROM Team WHERE team_name LIKE '%manchester city%')`
- **LeagueHistory**
  - Finding the mvp in a certain season of a certain league (premier league)
    - `SELECT first_name FROM Player WHERE player_id IN (SELECT mvp_id FROM LeagueHistory WHERE season_year = 2017 AND league_id = 'PRM')`
  - Finding the teams that have win in a certain league (world cup)
    - `SELECT t.team_name FROM Team t INNER JOIN LeagueHistory lh ON t.team_id = lh.team_winning_id WHERE lh.league_id = 'WRLD'`
