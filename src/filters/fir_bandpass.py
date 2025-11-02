from scipy.signal import firwin, lfilter


def fir_bandpass_filter(signal, numtaps=101, lowcut=0.001, highcut=0.05):
    """
    FIR bandpass using normalized freq (fractions of Nyquist).
    lowcut/highcut are fractions of Nyquist (0..1). For real Hz, use firwin's fs parameter.
    """
    taps = firwin(numtaps, [lowcut, highcut], pass_zero=False)
    return lfilter(taps, 1.0, signal)
