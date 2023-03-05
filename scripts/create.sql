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
	standing_id		int			NOT NULL UNIQUE ,
	team_id			int			NOT NULL ,
	league_id		char(5)		NOT NULL ,
	season_id		int			NULL
);

--------------------------
-- Create TeamStandingStat table
--------------------------
CREATE TABLE TeamStandingStat
(
	stat_id           int         NOT NULL UNIQUE ,
	games_played      int         NULL ,
	wins              int         NULL ,
	draws             int         NULL ,
	losses            int         NULL ,
	goals_scored      int         NULL ,
	goals_lost        int         NULL ,
	goal_diff         int         NULL ,
	standing_id       int         NOT NULL
);

--------------------------
-- Create LeagueHistory table
--------------------------
CREATE TABLE LeagueHistory
(
	season_id             int                 NOT NULL UNIQUE,
	season_year           int                 NOT NULL ,
	revenue               decimal(12, 2)      NULL ,
	viewership            int                 NULL ,
	league_id             char(5)             NOT NULL ,
	winning_team_id       int                 NULL ,
	mvp_id                int                 NULL
);

--------------------------
-- Create League table
--------------------------
CREATE TABLE League
(
	league_id         char(5)         NOT NULL UNIQUE ,
	year_founded      int             NULL ,
	league_name       char(50)        NOT NULL ,
	num_teams         int             NULL ,
	recurrence        char(50)        NULL 
);


----------------------
-- Create Match table
----------------------
CREATE TABLE Match
(
	match_id          int         NOT NULL UNIQUE ,
	date_played       date        NULL ,
	goals_team1       int         NULL ,
	goals_team2       int         NULL ,
	outcome           int         NOT NULL, -- the outcome is a 1 when team 1 wins, a 2 when team 2 wins, and a 0 when it is a draw
	league_id         char(5)     NULL ,
	team1_id          int         NOT NULL ,
	team2_id          int         NOT NULL
);

------------------------
-- Create Player table
------------------------
CREATE TABLE Player
(
	player_id         int             NOT NULL UNIQUE ,
	first_name        char(10)        NULL ,
	last_name         char(20)        NOT NULL ,
	middle_initial    char(1)         NULL ,
	year_salary       decimal(12,2)   NULL ,
	field_position    char(20)        NULL ,
	team_id           int             NULL 
);

-----------------------
-- Create PlayerStat table
-----------------------
CREATE TABLE PlayerStat
(
	stat_id           int         NOT NULL UNIQUE ,
	games_played      int         NULL ,
	goals             int         NULL ,
	assists           int         NULL ,
	hat_tricks        int         NULL ,
	player_id         int         NOT NULL
);

-----------------------
-- Create Player Award Table
-----------------------
CREATE TABLE PlayerTeam
(
	playerteam_id	int         NOT NULL UNIQUE ,
	player_id       int         NOT NULL ,
	team_id        int         NOT NULL
);

-----------------------
-- Create Player Award Table
-----------------------
CREATE TABLE PlayerAward
(
	playeraward_id  int         NOT NULL UNIQUE ,
	date_awarded    date        NULL ,
	player_id       int         NOT NULL ,
	award_id        int         NOT NULL
);
-----------------------
-- Create Team table
-----------------------
CREATE TABLE Team
(
	team_id           int             NOT NULL UNIQUE ,
 	team_name         char(50)        NOT NULL ,
	year_founded      int             NULL ,
	games_played      int             NULL ,
	wins              int             NULL ,
	country           char(50)        NULL ,
	league_id         char(5)         NOT NULL
);

----------------------
-- Create Award table
----------------------
CREATE TABLE Award
(
	award_id          int             NOT NULL UNIQUE ,
	award_name        char(50)        NOT NULL ,
	year_created      int             NULL ,
	times_given       int             NULL ,
	award_desc        varchar(500)    NULL 
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
ALTER TABLE TeamStandingStat ADD PRIMARY KEY (stat_id);
ALTER TABLE PlayerStat ADD PRIMARY KEY (stat_id);
ALTER TABLE PlayerAward ADD PRIMARY KEY (playeraward_id);

----------------------
-- Define foreign keys
----------------------
ALTER TABLE LeagueHistory ADD CONSTRAINT FK_LeagueHistory_League FOREIGN KEY (league_id) REFERENCES League (league_id);
ALTER TABLE LeagueHistory ADD CONSTRAINT FK_LeagueHistory_WinningTeam FOREIGN KEY (winning_team_id) REFERENCES Team (team_id);
ALTER TABLE LeagueHistory ADD CONSTRAINT FK_LeagueHistory_MostValuablePlayer FOREIGN KEY (mvp_id) REFERENCES Player (player_id);
ALTER TABLE TeamStanding ADD CONSTRAINT FK_TeamStanding_LeagueHistory FOREIGN KEY (season_id) REFERENCES LeagueHistory (season_id);
ALTER TABLE TeamStanding ADD CONSTRAINT FK_TeamStanding_Team FOREIGN KEY (team_id) REFERENCES Team (team_id);
ALTER TABLE TeamStanding ADD CONSTRAINT FK_TeamStanding_League FOREIGN KEY (league_id) REFERENCES League (league_id);
ALTER TABLE TeamStandingStat ADD CONSTRAINT FK_TeamStandingStat_TeamStanding FOREIGN KEY (standing_id) REFERENCES TeamStanding (standing_id);
ALTER TABLE PlayerStat ADD CONSTRAINT FK_PlayerStat_Player FOREIGN KEY (player_id) REFERENCES Player (player_id);
ALTER TABLE PlayerAward ADD CONSTRAINT FK_PlayerAward_Player FOREIGN KEY (player_id) REFERENCES Player (player_id);
ALTER TABLE PlayerAward ADD CONSTRAINT FK_PlayerAward_Award FOREIGN KEY (award_id) REFERENCES Award (award_id);
ALTER TABLE Team ADD CONSTRAINT FK_Team_League FOREIGN KEY (league_id) REFERENCES League (league_id);
ALTER TABLE Player ADD CONSTRAINT FK_Player_Team FOREIGN KEY (team_id) REFERENCES Team (team_id);
ALTER TABLE Match ADD CONSTRAINT FK_Matches_Team1 FOREIGN KEY (team1_id) REFERENCES Team (team_id);
ALTER TABLE Match ADD CONSTRAINT FK_Match_Team2 FOREIGN KEY (team2_id) REFERENCES Team (team_id);
ALTER TABLE Match ADD CONSTRAINT FK_Match_League FOREIGN KEY (league_id) REFERENCES League (league_id);