from pybaseball import statcast_batter
from pybaseball import playerid_lookup
from pybaseball import spraychart
import pandas as pd
import matplotlib.pyplot as plt

# 1. The ID Lookup 
player_info = playerid_lookup('judge', 'aaron')
player_id = player_info['key_mlbam'].values[0]

# 2. Pull the specific batter's data for 2025
data = statcast_batter('2025-03-27', '2025-09-28', player_id)

# 3. Filter for 'Balls In Play' (BIP)
bip = data.dropna(subset=['hc_x', 'hc_y']).copy()

# 4. THE VISUALIZATION: Plotting the Spray Chart
print("Generating Spray Chart...")

# We use the 'generic' stadium for a standardized view, color-coding by 'events'
chart = spraychart(bip, 'generic', title='Aaron Judge: 2025 Spray Chart', colorby='events')

# Display the plot
plt.show()