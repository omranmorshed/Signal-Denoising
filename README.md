# 🧠 Comparative Analysis of Digital Filtering Techniques for Multi-Type Noisy Signal Restoration

This project presents a **comprehensive comparative study** of several classical digital filtering techniques for denoising signals corrupted by various types of noise.  
It simulates realistic pulse signals (Gaussian core + exponential tail) contaminated with **Gaussian**, **Uniform**, **Poisson**, and **Salt & Pepper** noise, and applies multiple filters to evaluate their performance.

---

## 🎯 Objectives
- Generate synthetic noisy signals with different noise types and intensities.  
- Apply multiple digital filters and analyze their effectiveness in restoring the clean signal.  
- Compare filters based on **SNR (dB)**, **PSNR (dB)**, **MSE**, **correlation**, and **execution time**.  
- Visualize time-domain, frequency-domain, and spectrogram results for comprehensive understanding.  

---

## 🧩 Implemented Filters
1. **Moving Average Filter** – simple smoothing FIR filter using a sliding window.  
2. **FIR Bandpass Filter** – isolates frequency components of interest while suppressing unwanted ones.  
3. **Wiener Filter** – adaptive linear filter minimizing mean square error based on local statistics.  
4. **Wavelet Denoising** – removes noise in multi-resolution domain using thresholding.  
5. **Matched Filter** – optimally detects known signal shapes in noisy backgrounds.  

---

## ⚙️ Noise Models
The study considers four types of noise:
- **Gaussian noise:** random variations following normal distribution.  
- **Uniform noise:** constant probability density over a specific range.  
- **Poisson noise:** signal-dependent random noise, typical in photon/electron counting systems.  
- **Salt & Pepper noise:** sparse impulsive noise producing high/low spikes in the signal.  

---

## 🧠 Methodology
1. Generate clean synthetic pulse signals.  
2. Add selected noise type and control its variance or intensity.  
3. Apply all denoising filters sequentially.  
4. Compute quantitative metrics:  
   - Mean Squared Error (MSE)  
   - Peak Signal-to-Noise Ratio (PSNR)  
   - Signal-to-Noise Ratio (SNR)  
   - Correlation Coefficient  
   - Execution Time  
5. Plot and analyze results:
   - **Time-domain waveforms**  
   - **FFT amplitude spectra**  
   - **Power Spectral Density (PSD)**  
   - **Spectrogram (Time–Frequency plots)**  

---

## 📊 Results Overview
- Each filter exhibits unique strengths depending on noise characteristics.  
- **Wiener** and **Wavelet** filters generally achieve higher SNR for Gaussian and Uniform noise.  
- **Matched Filter** excels in detecting structured pulses under low-SNR conditions.  
- **FIR** and **Moving Average** filters offer good simplicity–performance trade-offs.  

---

## 📂 Project Structure
Signal-Denoising/
│
├── src/
│ ├── filters # All filtering algorithms
│ │ ├── fir_bandpass.py
│ │ ├── matched.py
│ │ ├── moving_average.py
│ │ ├── wavelet.py
│ │ ├── wiener.py
│ ├── noise.py # Noise generation functions
│ ├── pulse.py # generate pulse
│ ├── metrics.py # Evaluation metrics
│ ├── freq_analysis.py # FFT, PSD, and spectrogram plotting
│ ├── aplly_all_filters.py 
│ ├── plotting.py # time analysis, plotting
│ ├── main.py # Main demo pipeline
│
├── Comparative_Analysis_of_Digital_Filtering_Techniques_for_Multi-Type_Noisy_Signal_Restoration.pdf
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt

