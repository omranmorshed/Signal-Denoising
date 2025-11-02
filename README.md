# Signal Denoising & Filter Performance Analysis

A complete DSP experiment that evaluates multiple filters on different noise types  
(Gaussian, Uniform, Poisson, Salt & Pepper) using metrics (SNR, PSNR, MSE, Correlation)  
and frequency-domain visualization (FFT, PSD, Spectrogram).

## Features
- Realistic synthetic pulse generator
- Multiple noise models
- Filters: Moving Average, FIR, Wiener, Wavelet, Matched Filter
- Time & Frequency analysis + spectrograms
- Ranked performance table + runtime benchmarking
- Modular & extensible DSP pipeline

## Tech Stack
- Python (NumPy, SciPy, Matplotlib, PyWavelets)
- Jupyter / Matplotlib for visualization

## Run
`bash
python main.py