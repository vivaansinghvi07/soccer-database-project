# soccer-database-project
This will database will store information all about soccer, such as leagues, teams, players, matches played, and much more. With this project, I aim to provide easily accessible information all about soccer. People will be able to analyze anything from details about matches from 20 years ago, to the salaries of the top 5 most well-paid players in the scene. 

The tables used in this project include those describing a(n):
  - League
  - League History - a recount of a particular season
  - Team
  - Team Standing - how a team performed in a season
  - Team Stat - the team's statistics in a season
  - Match
  - Player
  - Player Stat - a players in-game stats
  - Award

## Requirements: 
PostGreSQL 15

## Tables: 
**Team Standing** - this table helps keep track of how a team performed in a certain season - such as Arsenal’s performance in the Premier League in the 2018-19 season
  - standing_id
  - team_id  - relates to team_id in TEAM table
  - league_id - relates to league_id in LEAGUE table
  - season_year	
  - season_id - relates to season_id in LEAGUEHISTORY table
  - stat_id - relates to stat_id in TEAMSTAT table 

**Team Stat** - this table keeps track of the team's performance during a season, as a somewhat branch of the TEAMSTANDING table
  - stat_id
  - games_played
  - wins
  - draws
  - losses
  - goals_scored
  - goals_lost
  - goal_difference

**League History** - this table keeps track of who won each season in the league. Such as: who won the Premier league in the 2017-18 season
  - season_id	
  - league_id - relates to league_id in LEAGUE table
  - winning_id - relates to team_id in TEAM table
  - season_year	
  - league_mvp_id - relates to player_id in PLAYER table

**League** - this table keeps information of each league that I am looking at - such as when the Premier League was founded, how often it occurs, etc. Note: Recurrence represents the number of years between seasons of the league
  - year_founded  
  - league_name 
  - league_id  
  - num_teams   
  - recurrence 

**Match** - this table is the largest and keeps information on every match for every league that I am looking at - you will be able to find the data of every soccer game that happened - currently, the table is about 5000-7000 rows long, just with the premier league alone.
  - match_id
  - date_played
  - season_id - relates to season_id in LEAGUEHISTORY table
  - league_id - relates to league_id in LEAGUE table
  - home_team_id - relates to team_id in TEAM table
  - away_team_id - relates to team_id in TEAM table
  - goals_home   
  - goals_away
  - winning_id - relates to team_id in TEAM table

**Player** - this table keeps track of all the players in soccer and their various details - such as what Messi’s earnings are, what his awards are, what team(s) he plays for, and how many goals and assists he has made
  - player_name 
  - player_id 
  - year_salary 
  - position
  - team_id - relates to team_id in TEAM table
  - stat_id - relates to stat_id in PLAYERSTAT table
  - award_ids - relates to award_id in AWARD table

**Player Stat** - this table keeps track of the player's in-game statistics, similar to how the TEAMSTAT table relates to TEAMSTANDING
  - stat_id
  - player_id - relates to player_id in PLAYER table
  - games_played
  - goals  
  - assists
  - hat_tricks

**Teams** - this table keeps track of teams and information about them - such as when Manchester United was founded, and what league it plays in
  - team_id 
  - team_name 
  - year_founded 
  - league_id - relates to league_id in LEAGUES table
  - games_played 
  - wins 
  - country  

**Award** - stores information about various awards in soccer - such as when the Ballon-D’or was started, a description of it, and how many times it was given
  - award_id
  - award_name
  - year_created	
  - times_given
  - award_desc

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
    - `SELECT player_name, year_salary FROM Player ORDER BY year_salary DESC`
  - Finding the most decorated player
    - `SELECT TOP 1 player_name FROM Player ORDER BY len(award_ids) DESC`
  - Finding the stats of a player (ex: Messi)
    - `SELECT p.player_name, ps.* FROM Player p INNER JOIN PlayerStat ps ON p.stat_id = ps.stat_id WHERE p.player_name LIKE '%messi%'`
  - Finding the player with the highest goals scored
    - `SELECT p.player_name, MAX(ps.goals) AS goals_scored FROM Player p INNER JOIN PlayerStat ps ON p.stat_id = ps.stat_id`
  - Finding the highest number of games played
    - `SELECT MAX(games_played) AS highest_games_played FROM Player Stat`
  - Finding the players with less than 100 matches
    - `SELECT p.player_name, ps.games_played FROM Player p INNER JOIN PlayerStat ps ON p.stat_id = ps.stat_id WHERE ps.games_played < 100`
- **Match**
  - Finding the number of matches that have had more than 8 goals
    - `SELECT COUNT(*) AS count FROM Match WHERE goals_home > 8 OR goals_away > 8`
  - Finding the matches that happened between specific dates (01-01-2001 and 02-01-2001)
    - `SELECT * FROM Match WHERE date_played BETWEEN '2001-01-01' AND '2001-02-01'`
  - Finding the highest scoring home teams that played in the 2018 season of the premier league
    - `SELECT TOP 5 * FROM Match WHERE season_id IN (SELECT season_id FROM LeagueHistory WHERE league_id = 'PRM' AND season_year = 2018) ORDER BY goals_home DESC`
- **TeamStat** and **TeamStanding**
  - Finding the team with the best goal difference in their 2020 season
    - `SELECT t.team_name, MAX(tst.goal_difference) as best_goal_difference FROM Team t INNER JOIN TeamStanding ts ON t.team_id = ts.team_id INNER JOIN TeamStat tst ON ts.stat_id = tst.stat_id WHERE ts.season_year = 2020`
  - Finding the highest goals scored by any team
    - `SELECT MAX(goals_scored) AS highest_goals_scored FROM TeamStat`
  - Finding a team's (Manchester City) stats in a certain season
    - `SELECT tst.* FROM TeamStanding ts INNER JOIN TeamStat tst ON ts.stat_id = tst.stat_id WHERE ts.team_id IN (SELECT team_id FROM Team WHERE team_name LIKE '%manchester city%')`
  - Finding the seasons which a team (Barcelona) played in 
    - `SELECT season_year FROM TeamStanding ts INNER JOIN Team t ON t.team_id = ts.team_id WHERE t.team_name LIKE '%barcelona%'`
- **LeagueHistory**
  - Finding the mvp in a certain season of a certain league (premier league)
    - `SELECT player_name FROM Player WHERE player_id IN (SELECT league_mvp_id FROM LeagueHistory WHERE season_year = 2017 AND league_id = 'PRM')`
  - Finding the teams that have win in a certain league (world cup)
    - `SELECT t.team_name FROM Team t INNER JOIN LeagueHistory lh ON t.team_id = lh.winning_id WHERE lh.league_id = 'WRLD'`
