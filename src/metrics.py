import numpy as np


def mse(a, b):
    return np.mean((a - b) ** 2)


def psnr(a, b):
    """Peak signal-to-noise ratio (dB)."""
    max_val = np.max(np.abs(a)) + 1e-12
    return 10 * np.log10(max_val ** 2 / (mse(a, b) + 1e-15))


def snr_db(clean, noisy):
    """Simple SNR (dB) estimator using clean signal power vs (noisy-clean) power."""
    sig_pow = np.mean(clean ** 2) + 1e-15
    noise_pow = np.mean((noisy - clean) ** 2) + 1e-15
    return 10.0 * np.log10(sig_pow / noise_pow)


def correlation(a, b):
    """Normalized correlation coefficient between two signals."""
    a_norm = a - np.mean(a)
    b_norm = b - np.mean(b)
    denom = (np.sqrt(np.sum(a_norm ** 2) * np.sum(b_norm ** 2)) + 1e-15)
    return np.sum(a_norm * b_norm) / denom
