from pybaseball import statcast, playerid_reverse_lookup
import pandas as pd

# 1. Pull data from the first week of 2025
data = statcast(start_dt='2025-03-27', end_dt='2025-04-03') 

# 2. Filter
data = data.dropna(subset=['estimated_ba_using_speedangle']).copy()

# 3. Calculate 
data['is_hit'] = data['events'].isin(['single', 'double', 'triple', 'home_run']).astype(int)

analysis = data.groupby('batter').agg({
    'is_hit': 'mean',
    'estimated_ba_using_speedangle': 'mean'
})

analysis.columns = ['Actual_BA', 'Expected_BA']
analysis['Luck_Gap'] = analysis['Actual_BA'] - analysis['Expected_BA']

# ---------------------------------------------------------
# 4. THE RELATIONAL JOIN
# ---------------------------------------------------------

# Extract the numeric IDs from analysis table
batter_ids = analysis.index.tolist()

# Pull the master lookup table from MLBAM for these specific IDs
lookup_table = playerid_reverse_lookup(batter_ids, key_type='mlbam')

# "First Last" name column
lookup_table['player_name'] = lookup_table['name_first'].str.title() + " " + lookup_table['name_last'].str.title()

# Merge the names into analysis DataFrame based on the shared MLBAM ID
final_report = analysis.merge(lookup_table[['key_mlbam', 'player_name']], left_on='batter', right_on='key_mlbam')

# Clean up
final_report = final_report.set_index('player_name')[['Actual_BA', 'Expected_BA', 'Luck_Gap']]

print("The Most Unlucky Hitters (Underperforming their contact quality):")
print(final_report.sort_values('Luck_Gap').head(10))