from nba_api.stats.endpoints import teamgamelogs
import pandas as pd
import time


logs = teamgamelogs.TeamGameLogs(season_nullable="2024-25", season_type_nullable='Regular Season')
df = logs.get_data_frames()[0]
time.sleep(2)

df.to_csv('2025teamgamelogs.csv', index=False)