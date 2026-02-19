from pybaseball import statcast_pitcher
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Get Data (Mason Miller, 2025)
data = statcast_pitcher('2025-04-01', '2025-10-01', 695243)

# 2. Data Engineering (Feet to Inches)
# We create new columns because 'pfx_x' comes in feet
data['horz_break'] = data['pfx_x'] * 12
data['vert_break'] = data['pfx_z'] * 12

# 3. Create the Plot
# sns.scatterplot handles the color-coding by pitch type automatically.
plt.figure(figsize=(10, 8))
sns.scatterplot(data=data, x='horz_break', y='vert_break', hue='pitch_type',  palette='deep')

# 4. Labeling (Critical for Ops)
plt.title('Mason Miller 2025 Pitch Movement')
plt.xlabel('Horizontal Break (Inches)')
plt.ylabel('Vertical Break (inches)')
plt.axhline(0, color='black', linewidth=1) # Zero line for reference
plt.axvline(0, color='black', linewidth=1) # Zero line for reference
plt.grid(True, linestyle='--', alpha=0.7)

# 5. Show it
plt.show()