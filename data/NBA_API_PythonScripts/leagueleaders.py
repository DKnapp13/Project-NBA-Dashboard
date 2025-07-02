from nba_api.stats.endpoints import leagueleaders
import pandas as pd
import time

leaders = leagueleaders.LeagueLeaders(season="2024-25", season_type_all_star= "Regular Season")

df = leaders.get_data_frames()[0]
df.to_csv('leagueleaders.csv', index = False)
