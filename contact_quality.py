from pybaseball import statcast

# Pull Data
data = statcast(start_dt='2025-03-27', end_dt='2025-03-27')

# Filter for balls put into play
in_play = data.dropna(subset=['launch_speed', 'launch_angle'])

# Finding the "Hard Hit" Leaderboard
hard_hits = in_play[in_play['launch_speed'] >= 95]
leaders = hard_hits.groupby('batter')['launch_speed'].agg(['max', 'min', 'count']).sort_values('max', ascending=False)

print("Opening Day Hard Hit Leaders:")
print(leaders.head(10))