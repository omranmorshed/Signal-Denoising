from scipy.signal import convolve
import numpy as np


def moving_average_filter(signal, window_size=11):
    """Simple moving average (FIR) with 'same' output length."""
    window = np.ones(window_size) / window_size
    return convolve(signal, window, mode='same')
