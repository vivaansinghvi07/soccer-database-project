# soccer-database-project
This will database will store information all about soccer, such as leagues, teams, players, matches played, and much more.

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

**League** - this table keeps information of each league that I am looking at - such as when the Premier League was founded, how often it occurs, etc.
  - year_founded  
  - league_name 
  - league_id  
  - num_teams   
  - recurrence 

**Match** - this table is the largest and keeps information on every match for every league that I am looking at - you will be able to find the data of every soccer game that happened - currently, the table is about 5000-7000 rows long, just with the premier league alone.
  - match_id
  - date_played
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
- Finding out how many teams scored over 5 goals in the Premier League season 2019-2020
- Finding out the highest paid player
- Counting the number of teams which have won in their league
- Finding the team with the highest-performing player by awards, goals, assists, etc