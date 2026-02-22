from pybaseball import statcast

# Pull the data
data = statcast(start_dt='2025-03-27', end_dt='2025-03-27')

# Isolate Luis Severino (MLBAM ID: 605483)
severino = data[data['player_name'].str.contains('Severino', na=False)]

# Calculate percentages
mix = severino['pitch_type'].value_counts(normalize=True) * 100

print("Luis Severino 2025 Opening Day Arsenal Mix:")
print(mix)