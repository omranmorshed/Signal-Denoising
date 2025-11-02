import numpy as np
from src.pulse import gaussian_exponential_pulse


def generate_test_signal(length=2048, peak_pos=300, pulse_amp=1.0,
                         sigma=20.0, tail_tau=50.0, baseline_freq=3.0,
                         baseline_amp=0.0, add_sine=False,
                         noise_types=['gaussian'], noise_levels=[0.15],
                         poisson_rate=0.0, baseline_drift_amp=0.0, seed=None):
    """
    Create a realistic test signal:
     - single pulse (Gaussian core + exponential tail)
     - optional sinusoidal baseline
     - additive noise of multiple types:
       'gaussian', 'uniform', 'poisson', 'salt_pepper'
    Parameters:
      noise_types: list of strings specifying noise types
      noise_levels: list of floats specifying noise amplitudes (same order as noise_types)
    Returns:
      clean, noisy, baseline_component
    """
    if seed is not None:
        np.random.seed(seed)
    # Clean pulse
    clean = gaussian_exponential_pulse(length=length, peak=peak_pos, amp=pulse_amp,
                                       sigma=sigma, tail_tau=tail_tau)
    t = np.arange(length)
    baseline = baseline_amp * \
        np.sin(2*np.pi*baseline_freq*t/length) if add_sine else np.zeros(length)

    noisy = clean + baseline

    # Add multiple noises
    for ntype, lvl in zip(noise_types, noise_levels):
        if ntype == 'gaussian':
            noisy += np.random.normal(0, lvl, size=length)
        elif ntype == 'uniform':
            noisy += np.random.uniform(-lvl, lvl, size=length)
        elif ntype == 'poisson':
            noisy += np.random.poisson(lvl, size=length) - lvl
        elif ntype == 'salt_pepper':
            num_sp = int(length*lvl)
            indices = np.random.choice(length, num_sp, replace=False)
            noisy[indices] = np.max(
                clean)*np.random.choice([0, 1], size=num_sp)

    # Optional slow baseline drift
    if baseline_drift_amp > 0.0:
        drift = baseline_drift_amp * np.sin(2 * np.pi * t / length * 3.0)
        noisy += drift

    return clean, noisy, baseline
