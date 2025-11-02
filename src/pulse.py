def gaussian_exponential_pulse(length=2048, peak=300, amp=1.0, sigma=20.0, tail_tau=50.0):
    """
    Create a single pulse: Gaussian core + exponential tail.
    Returns a 1D numpy array of `length` samples.
    """
    t = np.arange(length)
    core = amp * np.exp(-0.5 * ((t - peak) / sigma) ** 2)
    tail = np.zeros_like(t, dtype=float)
    mask = t >= peak
    tail[mask] = amp * np.exp(-(t[mask] - peak) / tail_tau)
    pulse = 0.85 * core + 0.15 * tail
    return pulse
