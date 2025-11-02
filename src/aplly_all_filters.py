from src.filters.moving_average import moving_average_filter
from src.filters.fir_bandpass import fir_bandpass_filter
from src.filters.wiener import wiener_filter
from src.filters.wavelet import wavelet_denoise
from src.filters.matched import matched_filter
import time
import numpy as np
from src.metrics import apply_all_filters_with_timing, mse, psnr, snr_db, correlation


def apply_all_filters_with_timing(clean, noisy, template=None):
    """
    Apply filters, measure execution time and compute metrics.
    - Align & normalize matched filter output to the clean signal peak for fair comparison.
    Returns:
      results: dict of filtered signals (matched normalized & aligned included)
      metrics: dict of metric dictionaries per filter
      exec_times: dict of execution times per filter (seconds)
    """
    results = {}
    exec_times = {}
    metrics = {}

    # moving average
    t0 = time.time()
    results['moving_average'] = moving_average_filter(noisy, window_size=11)
    exec_times['moving_average'] = time.time() - t0

    # fir bandpass
    t0 = time.time()
    results['fir_bandpass'] = fir_bandpass_filter(
        noisy, numtaps=101, lowcut=0.002, highcut=0.05)
    exec_times['fir_bandpass'] = time.time() - t0

    # wiener
    t0 = time.time()
    results['wiener'] = wiener_filter(noisy, mysize=11)
    exec_times['wiener'] = time.time() - t0

    # wavelet
    t0 = time.time()
    results['wavelet'] = wavelet_denoise(noisy, wavelet='db4', level=4)
    exec_times['wavelet'] = time.time() - t0

    # matched filter (produce corr, then align & normalize)
    if template is None:
        L = len(noisy)
        center = L // 2
        # derive a template
        template = clean[center-60:center+60] if len(clean) >= 120 else clean
    t0 = time.time()
    corr = matched_filter(noisy, template)
    exec_times['matched_raw'] = time.time() - t0

    # normalize & align matched output:
    # - find peak index in clean and in corr
    clean_peak_idx = np.argmax(clean)
    corr_peak_idx = np.argmax(np.abs(corr))
    shift = corr_peak_idx - clean_peak_idx
    # normalize amplitude to match max of clean
    corr_norm = corr / (np.max(np.abs(corr)) + 1e-12) * np.max(np.abs(clean))
    # roll to align peaks (negative shift moves corr earlier)
    corr_aligned = np.roll(corr_norm, -shift)
    results['matched'] = corr_aligned
    # record matched total time under key 'matched'
    exec_times['matched'] = exec_times['matched_raw']

    # compute metrics for each result
    for name, arr in results.items():
        cur_mse = mse(clean, arr)
        cur_psnr = psnr(clean, arr)
        cur_snr = snr_db(clean, arr)
        cur_corr = correlation(clean, arr)
        metrics[name] = {
            'MSE': cur_mse,
            'PSNR(dB)': cur_psnr,
            'SNR(dB)': cur_snr,
            'Correlation': cur_corr,
            'Time(s)': exec_times.get(name, 0.0)
        }

    return results, metrics, exec_times
