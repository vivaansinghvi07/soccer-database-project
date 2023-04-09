-- stores templates for editing tables

INSERT INTO League(year_founded, league_name, league_id, num_teams, recurrence) 
    VALUES ('', '', '', '', '');
INSERT INTO Team(team_id, team_name, year_founded, country) 
    VALUES ('', '', '', '');
INSERT INTO Player(first_name, last_name, middle_initial, player_id, field_position)
    VALUES ('', '', '', '', '');
INSERT INTO Award(award_id, award_name, year_created, times_given, award_desc)
    VALUES ('', '', '', '', '');
INSERT INTO PlayerStat(stat_id, player_id, games_played, goals, assists, hat_tricks)
    VALUES('', '', '', '', '', '');
INSERT INTO PlayerAward(playeraward_id, date_awarded, player_id, award_id)
    VALUES('', '', '', '');
INSERT INTO PlayerTeam(playerteam_id, date_joined, earnings, player_id, team_id)
    VALUES('', '', '', '', '');
INSERT INTO LeagueHistory(season_id, league_id, winning_team_id, season_year, revenue, viewership, mvp_id)
    VALUES ('', '', '', '', '', '', '');
INSERT INTO TeamStanding(standing_id, team_id, league_id, season_id)
    VALUES('', '', '', '');
INSERT INTO TeamStandingStat(stat_id, standing_id, games_played, wins, draws, losses, goals_scored, goals_lost, goal_diff)
    VALUES('', '', '', '', '', '', '', '', '');
INSERT INTO Match(match_id, date_played, league_id, team1_id, team2_id, goals_team1, goals_team2, outcome)
    VALUES('', '', '', '', '', '', '', '');