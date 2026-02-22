from pybaseball import statcast

# 1. Pull the data
data = statcast(start_dt='2025-03-27', end_dt='2025-03-27')

# 2. Isolate the ATH game
ath_game = data[(data['home_team'] == 'ATH') | (data['away_team'] == 'ATH')]

# 3. Define the labels
swing_labels = ['foul', 'hit_into_play', 'swinging_strike', 'foul_tip', 'swinging_strike_blocked']
whiff_labels = ['swinging_strike', 'swinging_strike_blocked']

# 4. Filter for only pitches where a swing occurred
swings = ath_game[ath_game['description'].isin(swing_labels)].copy()

# 5. Calculate Whiff Rate per pitcher
whiff_rates = swings.groupby('player_name')['description'].apply(
    lambda x: x.isin(whiff_labels).mean() * 100
).sort_values(ascending=False)

print("A's vs Mariners Whiff Rate Leaders (Min. 5 Swings):")
print(whiff_rates)