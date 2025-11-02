from scipy.signal import correlate
import numpy as np


def matched_filter(signal, template):
    """
    Matched filter via cross-correlation. Returns correlation output (same length).
    Template should be similar length to expected pulse duration.
    """
    sigc = signal - np.mean(signal)
    tplc = template - np.mean(template)
    corr = correlate(sigc, tplc, mode='same')
    return corr
