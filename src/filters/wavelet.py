import pywt
import numpy as np


def wavelet_denoise(signal, wavelet='db4', level=None):
    """Wavelet denoising with universal threshold (Donoho)."""
    if level is None:
        level = pywt.dwt_max_level(len(signal), pywt.Wavelet(wavelet).dec_len)
    coeffs = pywt.wavedec(signal, wavelet, level=level)
    detail_coeffs = coeffs[-1]
    sigma = np.median(np.abs(detail_coeffs)) / 0.6745 + 1e-12
    uthresh = sigma * np.sqrt(2 * np.log(len(signal)))
    denoised = [coeffs[0]] + \
        [pywt.threshold(c, value=uthresh, mode='soft') for c in coeffs[1:]]
    rec = pywt.waverec(denoised, wavelet)
    return rec[:len(signal)]
