import numpy as np
import matplotlib.pyplot as plt

# 1. Setup
fs = 100000          # 100 kHz Sampling Rate
duration = 0.01      # 10ms Duration
t = np.linspace(0, duration, int(fs*duration), endpoint=False)

# 2. Generate the Signal (The Challenge: Square Wave)
freq = 1000          # 1 kHz Fundamental
# np.sign converts sine wave to square (+1/-1)
signal = np.sign(np.sin(2 * np.pi * freq * t)) 

# 3. The Math (FFT)
fft_spectrum = np.fft.fft(signal)
fft_freqs = np.fft.fftfreq(len(signal), 1/fs)

# Positive half only
n_half = len(signal) // 2
fft_freqs = fft_freqs[:n_half]
fft_spectrum = np.abs(fft_spectrum)[:n_half] / n_half

# 4. Plotting
plt.figure(figsize=(10, 6))

# Time Domain
plt.subplot(2, 1, 1)
plt.plot(t[:1000], signal[:1000]) # First 1ms
plt.title(f"Time Domain: {freq}Hz Square Wave")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.grid(True)

# Frequency Domain
plt.subplot(2, 1, 2)
plt.plot(fft_freqs, fft_spectrum, 'r') 
plt.xlim(0, 20000) # Show 0 to 20 kHz
plt.title("Frequency Domain: The Harmonics")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)

plt.tight_layout()
plt.show()