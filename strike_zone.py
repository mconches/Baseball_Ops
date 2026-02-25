from pybaseball import statcast
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd

# 1. Pull Data & Clean (Same as Step 1)
print("Pulling Hawkeye pitch tracking data...")
data = statcast(start_dt='2025-03-27', end_dt='2025-03-27')
takes = data[data['description'].isin(['called_strike', 'ball'])].copy()
clean_takes = takes.dropna(subset=['plate_x', 'plate_z', 'sz_top', 'sz_bot']).copy()

# 2. Define Boundaries
inside_x = (clean_takes['plate_x'] >= -0.708) & (clean_takes['plate_x'] <= 0.708)
inside_z = (clean_takes['plate_z'] >= clean_takes['sz_bot']) & (clean_takes['plate_z'] <= clean_takes['sz_top'])

clean_takes['in_rulebook_zone'] = inside_x & inside_z

# 3. The Framing Logic
# It was called a strike, but it was NOT physically in the zone
clean_takes['stolen_strike'] = (clean_takes['description'] == 'called_strike') & (~clean_takes['in_rulebook_zone'])

# 4. Isolate the Stolen Strikes for Visualization
framed_pitches = clean_takes[clean_takes['stolen_strike'] == True]
print(f"\nTotal 'Stolen Strikes' on Opening Day 2025: {len(framed_pitches)}")

# 5. THE VISUALIZATION: Drawing the Front Office Heat Map
print("Rendering Strike Zone Map...")

fig, ax = plt.subplots(figsize=(6, 8))

# Coordinates for the rectangle
zone = patches.Rectangle((-0.708, 1.5), 1.416, 2.0, linewidth=2, edgecolor='black', facecolor='none', zorder=3)
ax.add_patch(zone)

# Draw Home Plate
plate_x = [-0.708, -0.708, 0, 0.708, 0.708]
plate_y = [0.2, 0, -0.25, 0, 0.2]
ax.plot(plate_x, plate_y, color='black', linewidth=2)

# Plot the Framed Pitches
ax.scatter(framed_pitches['plate_x'], framed_pitches['plate_z'], color='red', alpha=0.6, label='Stolen Strikes')

# Professional Formatting
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-0.5, 5.0)
ax.set_title("Catcher Framing: Stolen Strikes (Opening Day 2025)", fontsize=14, fontweight='bold')
ax.set_xlabel("Horizontal Location (Feet)", fontweight='bold')
ax.set_ylabel("Vertical Location (Feet)", fontweight='bold')
ax.axvline(0, color='gray', linestyle='--', linewidth=0.5) # Center line
ax.legend(loc='upper right')
ax.grid(True, linestyle=':', alpha=0.6)

plt.show()