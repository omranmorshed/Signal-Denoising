from scipy.signal import wiener


def wiener_filter(signal, mysize=11, noise=None):
    """SciPy Wiener filter (local-adaptive)."""
    return wiener(signal, mysize=mysize, noise=noise)
