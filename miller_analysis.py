from pybaseball import statcast_pitcher

# 1. Fetch data for Mason Miller (ID: 695243)
# We pull the full 2025 season
miller_data = statcast_pitcher('2025-04-01', '2025-10-01', 695243)

# 2. Analyze his arsenal usage
# value_count() counts how many times each unique value appears.
# normalize=True turns those counts into percentages (decimals)
usage = miller_data['pitch_type'].value_counts(normalize=True)

# 3. Display
print("Pitch Usage (%):")
print(usage)