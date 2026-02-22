from pybaseball import statcast

# 1. Pull data
data = statcast(start_dt='2025-03-27', end_dt='2025-03-27')

# 2. Sort by pitcher, game, and time to ensure the sequence is correct
data = data.sort_values(['player_name', 'game_date', 'at_bat_number', 'pitch_number'])

# 3. Create the "Previous Pitch" column
data['prev_pitch'] = data.groupby('player_name')['pitch_type'].shift(1)

# 4. Filter for the FF -> CH sequence
tunnel_sequence = data[(data['prev_pitch'] == 'FF') & (data['pitch_type'] == 'CH')]

print(f"Total FF -> CH sequences found: {len(tunnel_sequence)}")