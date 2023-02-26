-------------------------------------------------
-- Sams Teach Yourself SQL in 10 Minutes
-- http://www.forta.com/books/0672325675/
-- Example table creation scripts for PostgreSQL.
-------------------------------------------------


-------------------------
-- Create TeamStanding table
-------------------------
CREATE TABLE TeamStanding
(
  standing_id	int	NOT NULL UNIQUE ,
  team_id    	int  	NOT NULL ,
  league_id  	char(5) 	NOT NULL ,
  season_year	int  	NULL ,
  season_id	int	NULL ,	
  games_played	int	NULL ,
  stat_id	int 	NULL 
);

--------------------------
-- Create TeamStat table
--------------------------
CREATE TABLE TeamStat
(
  stat_id 	int	NOT NULL UNIQUE ,
  games_played	int	NULL ,
  wins    	int  	NULL ,
  draws   	int   	NULL ,
  losses     	int  	NULL ,
  goals_scored 	int	NULL ,
  goals_lost 	int  	NULL ,
  goal_diff   	int	NULL 
);

--------------------------
-- Create LeagueHistory table
--------------------------
CREATE TABLE LeagueHistory
(
  season_id	int	NOT NULL UNIQUE,
  league_id	char(5)	NOT NULL ,
  winning_id	int	NOT NULL ,
  season_year	int	NOT NULL ,
  league_mvp_id	int	NULL  
);

--------------------------
-- Create League table
--------------------------
CREATE TABLE League
(
  year_founded  	int          	NULL ,
  league_name 	char(50)    	NOT NULL ,
  league_id    	char(5) 		NOT NULL UNIQUE ,
  num_teams   	int          	NULL ,
  recurrence 	char(50) 	NULL 
);


----------------------
-- Create Match table
----------------------
CREATE TABLE Match
(
  match_id	int	NOT NULL UNIQUE ,
  date_played	date	NULL ,
  league_id	char(5)	NULL ,
  home_team_id  	int     	NULL ,
  away_team_id 	int    	NULL ,
  goals_home    	int 	NULL ,
  goals_away	int	NULL ,
  winning_id	int 	NULL	
);

------------------------
-- Create Player table
------------------------
CREATE TABLE Player
(
  first_name   	char(10)      	NULL ,
  last_name	char(20)		NOT NULL ,
  middle_initial char(1)		NULL ,
  player_id    	int      	NOT NULL UNIQUE ,
  year_salary  	decimal(12,2)    NULL ,
  field_position	char(20)		NULL ,
  team_id 	int	  	NULL ,
  award_ids	int		NULL ,
  stat_id 	int 		NULL 
);

-----------------------
-- Create PlayerStat table
-----------------------
CREATE TABLE PlayerStat
(
  stat_id	int 		NOT NULL UNIQUE ,
  games_played	int		NULL ,
  goals  	int	 	NULL ,
  assists	int		NULL ,
  hat_tricks	int		NULL 	
);

-----------------------
-- Create Team table
-----------------------
CREATE TABLE Team
(
  team_id      	int 		NOT NULL UNIQUE ,
  team_name    	char(50) 	NOT NULL ,
  year_founded 	int	 	NULL ,
  league_id    	char(5) 		NOT NULL ,
  games_played  	int	  	NULL ,
  wins    	int	 	NULL ,
  country 	char(50) 	NULL 
);

----------------------
-- Create Award table
----------------------
CREATE TABLE Award
(
  award_id	int		NOT NULL UNIQUE ,
  award_name	char(50)		NOT NULL ,
  year_created	int		NULL ,
  times_given	int		NULL ,
  award_desc	varchar(500)	NULL 
);

----------------------
-- Define primary keys
----------------------
ALTER TABLE Player ADD PRIMARY KEY (player_id);
ALTER TABLE LeagueHistory ADD PRIMARY KEY (season_id);
ALTER TABLE League ADD PRIMARY KEY (league_id);
ALTER TABLE TeamStanding ADD PRIMARY KEY (standing_id);
ALTER TABLE Award ADD PRIMARY KEY (award_id);
ALTER TABLE Team ADD PRIMARY KEY (team_id);
ALTER TABLE Match ADD PRIMARY KEY (match_id);
ALTER TABLE TeamStat ADD PRIMARY KEY (stat_id);
ALTER TABLE PlayerStat ADD PRIMARY KEY (stat_id);

----------------------
-- Define foreign keys
----------------------
ALTER TABLE LeagueHistory ADD CONSTRAINT FK_LeagueHistory_League FOREIGN KEY (league_id) REFERENCES League (league_id);
ALTER TABLE LeagueHistory ADD CONSTRAINT FK_LeagueHistory_Team FOREIGN KEY (winning_id) REFERENCES Team (team_id);
ALTER TABLE LeagueHistory ADD CONSTRAINT FK_LeagueHistory_Player FOREIGN KEY (league_mvp_id) REFERENCES Player (player_id);
ALTER TABLE TeamStanding ADD CONSTRAINT FK_TeamStanding_LeagueHistory FOREIGN KEY (season_id) REFERENCES LeagueHistory (season_id);
ALTER TABLE TeamStanding ADD CONSTRAINT FK_TeamStanding_Team FOREIGN KEY (team_id) REFERENCES Team (team_id);
ALTER TABLE TeamStanding ADD CONSTRAINT FK_TeamStanding_League FOREIGN KEY (league_id) REFERENCES League (league_id);
ALTER TABLE TeamStanding ADD CONSTRAINT FK_TeamStanding_TeamStat FOREIGN KEY (stat_id) REFERENCES TeamStat (stat_id);
ALTER TABLE Player ADD CONSTRAINT FK_Player_Award FOREIGN KEY (award_ids) REFERENCES Award (award_id);
ALTER TABLE Player ADD CONSTRAINT FK_Player_PlayerStat FOREIGN KEY (stat_id) REFERENCES PlayerStat (stat_id);
ALTER TABLE Team ADD CONSTRAINT FK_Team_League FOREIGN KEY (league_id) REFERENCES League (league_id);
ALTER TABLE Player ADD CONSTRAINT FK_Player_Team FOREIGN KEY (team_id) REFERENCES Team (team_id);
ALTER TABLE Match ADD CONSTRAINT FK_Matches_HomeTeam FOREIGN KEY (home_team_id) REFERENCES Team (team_id);
ALTER TABLE Match ADD CONSTRAINT FK_Match_AwayTeam FOREIGN KEY (away_team_id) REFERENCES Team (team_id);
ALTER TABLE Match ADD CONSTRAINT FK_Match_WinningTeam FOREIGN KEY (winning_id) REFERENCES Team (team_id);
ALTER TABLE Match ADD CONSTRAINT FK_Match_League FOREIGN KEY (league_id) REFERENCES League (league_id);