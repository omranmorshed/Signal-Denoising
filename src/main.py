import numpy as np
from src.pulse import generate_test_signal
from src.metrics import apply_all_filters_with_timing, mse, psnr, snr_db, correlation
from src.plotting import print_metrics_table, plot_results_grid, plot_fft_psd_spectrogram_grid
from src.noise import generate_test_signal


def main_demo(save_fig=True):
    # parameters
    np.random.seed(0)
    length = 2048
    peak_pos = 500
    fs = 1e6
    clean, noisy, baseline = generate_test_signal(length=length,
                                                  peak_pos=peak_pos,
                                                  pulse_amp=1.0,
                                                  sigma=20.0,
                                                  tail_tau=50.0,
                                                  baseline_freq=3.0,
                                                  baseline_amp=0.05,
                                                  add_sine=True,
                                                  noise_types=['gaussian'],
                                                  noise_levels=[0.15],
                                                  poisson_rate=0.0,
                                                  baseline_drift_amp=0.02,
                                                  seed=0)

    # compute noisy baseline metrics for reference (no filter)
    noisy_metrics = {
        'MSE': mse(clean, noisy),
        'PSNR(dB)': psnr(clean, noisy),
        'SNR(dB)': snr_db(clean, noisy),
        'Correlation': correlation(clean, noisy),
        'Time(s)': 0.0
    }

    # apply filters and measure
    results, metrics, exec_times = apply_all_filters_with_timing(
        clean, noisy, template=None)

    # print table
    print_metrics_table(metrics, noisy_metrics=noisy_metrics)

    # plot
    plot_results_grid(clean, noisy, results, save_fig=save_fig)

    # Run frequency analysis and show plots
    plot_fft_psd_spectrogram_grid(results, clean, noisy, fs=fs)

    return clean, noisy, results, metrics, exec_times


# ----------------------------
# Run demo
# ----------------------------
if __name__ == "__main__":
    clean, noisy, results, metrics, exec_times = main_demo(save_fig=True)
