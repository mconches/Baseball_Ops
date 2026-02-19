from pybaseball import statcast

# Pull data for a specific date (Format: YYYY-MM-DD)
data = statcast(start_dt='2024-05-01', end_dt='2024-05-01')

# Display the first 5 rows
print(data.head())