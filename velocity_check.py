from pybaseball import statcast

# 1. Get Data
data = statcast(start_dt='2025-08-15', end_dt='2025-08-15')

# 2. Filter & Sort
# sort_values() does exactly what it says.
# ascending=False means "Give me the big numbers first."
high_velo = data[data['release_speed'] >= 100].sort_values('release_speed', ascending=False)

# 3. Select Columns
final_view = high_velo[['player_name', 'pitch_type', 'release_speed', 'batter']]

# 4. Display
print(final_view.head(10))