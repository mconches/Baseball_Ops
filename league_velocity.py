from pybaseball import statcast

# 1. Pull data for Opening Day 2025
data = statcast(start_dt='2025-03-27', end_dt='2025-03-27')

# 2. The Grouping Operation
# Group by player name and calculate mean (average) and count (volume)
leaderboard = data.groupby('player_name')['release_speed'].agg(['mean', 'count'])

# 3. Filtering for Sample Size
# Only look at guys with 50+ pitches
qualified = leaderboard[leaderboard['count'] >= 50].sort_values('mean', ascending=False)

print("Opening Day 2025 Velocity Leaders:")
print(qualified.head(10))