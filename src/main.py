import numpy as np
import matplotlib.pyplot as plt

# simple test signal
t = np.linspace(0, 1, 1000)
clean = np.sin(2*np.pi*10*t)
noise = np.random.normal(0, 0.3, t.shape)
noisy = clean + noise

plt.figure(figsize=(10, 4))
plt.plot(t, clean, label="Clean Signal")
plt.plot(t, noisy, label="Noisy Signal", alpha=0.6)
plt.legend()
plt.title("Test Signal Display")
plt.show()

print("✅ Script ran successfully")
