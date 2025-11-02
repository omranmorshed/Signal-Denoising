import matplotlib.pyplot as plt


def print_metrics_table(metrics, noisy_metrics=None):
    """
    Print formatted table of metrics. If noisy_metrics is provided (metrics for raw noisy),
    it will be printed as the baseline row.
    """
    print("\nFilter Performance Metrics (sorted by SNR descending):")
    print("{:<16s} {:>12s} {:>12s} {:>10s} {:>12s} {:>10s}".format(
        "Filter", "MSE", "PSNR(dB)", "SNR(dB)", "Correlation", "Time(s)"))
    rows = []
    for name, m in metrics.items():
        rows.append((name, m['MSE'], m['PSNR(dB)'],
                    m['SNR(dB)'], m['Correlation'], m['Time(s)']))
    # sort by SNR descending
    rows_sorted = sorted(rows, key=lambda x: x[3], reverse=True)
    if noisy_metrics is not None:
        nm = noisy_metrics
        print("{:<16s} {:12.4e} {:12.3f} {:10.3f} {:12.3f} {:10.4f}".format(
            "noisy", nm['MSE'], nm['PSNR(dB)'], nm['SNR(dB)'], nm['Correlation'], nm['Time(s)']))
    for r in rows_sorted:
        print("{:<16s} {:12.4e} {:12.3f} {:10.3f} {:12.3f} {:10.4f}".format(
            r[0], r[1], r[2], r[3], r[4], r[5]))


def plot_results_grid(clean, noisy, results_dict, save_fig=False, fig_name='filters_comparison_fixed.png'):
    """
    Plot: top row = clean vs noisy, second row = all filters (subplots).
    """
    names = list(results_dict.keys())
    n_filters = len(names)

    plt.figure(figsize=(14, 9))
    # Top: clean vs noisy
    ax_top = plt.subplot(2, 1, 1)
    ax_top.plot(clean, label='Clean (truth)', color='black', linewidth=1.2)
    ax_top.plot(noisy, label='Noisy', color='tab:red', alpha=0.6)
    ax_top.set_title('Clean (truth) vs Noisy')
    ax_top.legend()
    ax_top.grid(True)

    plt.figure(figsize=(14, 9))
    # Bottom: filters (arrange as 2x3 grid if up to 5 filters)
    for i, name in enumerate(names):
        ax = plt.subplot(2, 3, i+1)
        ax.plot(clean, label='Clean (truth)', color='black', linewidth=0.9)
        ax.plot(results_dict[name], label=name, alpha=0.9)
        ax.set_title(name)
        ax.legend()
        ax.grid(True)

    plt.tight_layout()
    if save_fig:
        plt.savefig(fig_name, dpi=160)
        print(f"Saved figure to {fig_name}")
    plt.show()
