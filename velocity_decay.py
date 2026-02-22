from pybaseball import statcast
import matplotlib.pyplot as plt

# Pull Data
data = statcast(start_dt='2025-03-27', end_dt='2025-03-27')

# Isolate Starter
starter = data[data['player_name'].str.contains('Severino', na=False)]

# Group by innings; calculating average velocity
decay = starter.groupby('inning')['release_speed'].mean()

print("Severino Veloctiy by Inning:")
print(decay)

# Visualization
plt.figure(figsize=(10,6))
decay.plot(kind='line', marker='o', color='red')
plt.title("Velocity Decay Analysis: Luis Severino (Opening Day 2025)")
plt.xlabel("Inning")
plt.ylabel("Avg Velocity (MPH)")
plt.grid(True, linestyle='--')
plt.show()