import numpy as np
import matplotlib.pyplot as plt

# Setup
fs = 100000
t = np.linspace(0, 0.003, int(fs*0.003), endpoint=False) # 3ms duration
freq = 1000

# 1. The Ingredients
wave_1k = 1.0 * np.sin(2 * np.pi * 1000 * t)             # Fundamental
wave_2k = 0.5 * np.sin(2 * np.pi * 2000 * t)             # Even (The "Bad" Ingredient)
wave_3k = (1/3) * np.sin(2 * np.pi * 3000 * t)           # 3rd Harmonic
wave_5k = (1/5) * np.sin(2 * np.pi * 5000 * t)           # 5th Harmonic

# 2. The Mixing Bowl
# Sum of Odds (The Square Recipe)
sum_odds = wave_1k + wave_3k + wave_5k 

# Sum with Even (The "Broken" Recipe)
sum_bad = wave_1k + wave_2k

# 3. Plotting
plt.figure(figsize=(10, 8))

# Plot 1: The Components
plt.subplot(3, 1, 1)
plt.plot(t, wave_1k, label="1 kHz (Main)")
plt.plot(t, wave_3k, label="3 kHz (Flattener)")
plt.title("The Ingredients")
plt.legend(loc='upper right')
plt.grid(True)

# Plot 2: What happens if you add 2kHz? (Broken Symmetry)
plt.subplot(3, 1, 2)
plt.plot(t, sum_bad, 'r')
plt.title("Why No 2kHz? (Notice it creates a Sawtooth/Lopsided shape!)")
plt.ylabel("Amplitude")
plt.grid(True)

# Plot 3: The Square Wave Construction (1k + 3k + 5k)
plt.subplot(3, 1, 3)
plt.plot(t, sum_odds, 'g')
plt.title("The Square Recipe: 1k + 3k + 5k (Getting Squarer!)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()