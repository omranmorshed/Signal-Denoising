import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from scipy.signal import welch, spectrogram, get_window
from src.metrics import snr_db


def compute_fft(signal, fs=1e6, nfft=None):
    """
    Compute single-sided FFT magnitude and frequency axis (Hz).
    Returns (freqs, mag) where mag is amplitude spectrum (not power).
    """
    N = len(signal)
    if nfft is None:
        nfft = int(2 ** np.ceil(np.log2(N)))
    # FFT
    S = np.fft.rfft(signal, n=nfft)
    freqs = np.fft.rfftfreq(nfft, d=1.0/fs)
    # magnitude (scale to amplitude)
    mag = np.abs(S) / N * 2.0  # multiply by 2 for single-sided amplitude
    return freqs, mag


def compute_psd_welch(signal, fs=1e6, nperseg=512, window='hann'):
    """
    Compute PSD (Welch). Returns (freqs, psd) where psd has units power/Hz.
    """
    win = get_window(window, nperseg)
    freqs, psd = welch(signal, fs=fs, window=win, nperseg=nperseg,
                       noverlap=nperseg//2, nfft=None, scaling='density')
    return freqs, psd


def plot_fft_psd_spectrogram_grid(signals_dict, clean, noisy, fs=1e6, nperseg=256, noverlap=None, cmap='viridis'):
    """
    Grid plot: Col1=FFT, Col2=PSD, Col3=Spectrogram
    Rows = noisy + filtered signals (sorted by SNR descending)
    """
    import matplotlib.pyplot as plt

    # signals dict: add noisy first
    signals = {'noisy': noisy}
    signals.update(signals_dict)

    # sort filters by SNR descending (optional, skip if not needed)
    snr_list = []
    for name, sig in signals_dict.items():
        snr_list.append((name, snr_db(clean, sig)))
    snr_sorted = sorted(snr_list, key=lambda x: x[1], reverse=True)
    sorted_names = ['noisy'] + [x[0] for x in snr_sorted]

    n_rows = len(sorted_names)
    fig, axes = plt.subplots(n_rows, 3, figsize=(15, 3*n_rows))

    for i, name in enumerate(sorted_names):
        sig = signals[name]
        # FFT
        f, mag = compute_fft(sig, fs=fs)
        ax_fft = axes[i, 0] if n_rows > 1 else axes[0]
        ax_fft.plot(f, mag, label=name)
        ax_fft.set_xlim(0, fs/2)
        if i == 0:
            ax_fft.set_title('FFT')
        ax_fft.set_ylabel('Amplitude')
        if i == n_rows-1:
            ax_fft.set_xlabel('Frequency [Hz]')
        ax_fft.grid(True)
        ax_fft.legend(fontsize=8)

        # PSD
        f_psd, psd = compute_psd_welch(sig, fs=fs)
        ax_psd = axes[i, 1] if n_rows > 1 else axes[1]
        ax_psd.semilogy(f_psd, psd, label=name)
        if i == 0:
            ax_psd.set_title('PSD (Welch, log)')
        if i == n_rows-1:
            ax_psd.set_xlabel('Frequency [Hz]')
        ax_psd.set_ylabel('Power/Hz')
        ax_psd.grid(True, which='both', ls='--', lw=0.5)
        ax_psd.legend(fontsize=8)

        # Spectrogram
        ax_spec = axes[i, 2] if n_rows > 1 else axes[2]
        f_s, t_s, Sxx = spectrogram(sig, fs=fs, window='hann', nperseg=nperseg,
                                    noverlap=(noverlap if noverlap is not None else nperseg//2), scaling='density', mode='psd')
        Sxx_db = 10*np.log10(Sxx + 1e-15)
        im = ax_spec.pcolormesh(t_s, f_s, Sxx_db, shading='gouraud', cmap=cmap)
        ax_spec.set_ylabel('Freq [Hz]')
        ax_spec.set_xlabel('Time [s]')
        if i == 0:
            ax_spec.set_title('Spectrogram')
        ax_spec.set_ylim(0, fs/2)
        plt.colorbar(im, ax=ax_spec, format='%+2.0f dB')

    plt.tight_layout()
    plt.show()
