from pybaseball import statcast

# 1. Pull Data (Opening Day 2025). As of 2025 team is abbr ATH instead of OAK
data = statcast(start_dt='2025-03-27', end_dt='2025-03-27')

# 2. Separate the A's
ath_data = data[(data['home_team'] == 'ATH') | (data['away_team'] == 'ATH')]

print(f"Total pitches in A's game: {len(ath_data)}")