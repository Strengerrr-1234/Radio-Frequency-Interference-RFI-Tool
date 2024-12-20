import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

class RFIBlocker:
    def __init__(self, sample_rate, signal_band, interference_band):
        """
        Initialize the RFIBlocker.

        Parameters:
        - sample_rate: Sampling rate of the signal (Hz)
        - signal_band: Tuple specifying the frequency range of the desired signal (Hz)
        - interference_band: Tuple specifying the frequency range of the interference (Hz)
        """
        self.sample_rate = sample_rate
        self.signal_band = signal_band
        self.interference_band = interference_band

    def bandstop_filter(self, data):
        """
        Apply a bandstop filter to remove interference.

        Parameters:
        - data: Input signal (1D numpy array)

        Returns:
        - Filtered signal (1D numpy array)
        """
        nyquist = 0.5 * self.sample_rate
        low = self.interference_band[0] / nyquist
        high = self.interference_band[1] / nyquist

        # Design a bandstop filter
        b, a = signal.butter(4, [low, high], btype='bandstop')
        filtered_data = signal.filtfilt(b, a, data)

        return filtered_data

    def generate_test_signal(self, duration=1.0):
        """
        Generate a test signal with interference.

        Parameters:
        - duration: Duration of the signal (seconds)

        Returns:
        - Tuple of time array and signal array
        """
        t = np.linspace(0, duration, int(self.sample_rate * duration), endpoint=False)

        # Desired signal (e.g., sine wave in signal_band)
        signal_freq = np.mean(self.signal_band)
        desired_signal = np.sin(2 * np.pi * signal_freq * t)

        # Interference signal (e.g., sine wave in interference_band)
        interference_freq = np.mean(self.interference_band)
        interference_signal = 0.5 * np.sin(2 * np.pi * interference_freq * t)

        # Combined signal
        combined_signal = desired_signal + interference_signal

        return t, combined_signal

# Example usage
if __name__ == "__main__":
    # Parameters
    sample_rate = 1000  # Hz
    signal_band = (20, 50)  # Desired signal frequency range (Hz)
    interference_band = (100, 120)  # Interference frequency range (Hz)

    rfi_blocker = RFIBlocker(sample_rate, signal_band, interference_band)

    # Generate a test signal
    t, test_signal = rfi_blocker.generate_test_signal()

    # Apply RFI blocking
    filtered_signal = rfi_blocker.bandstop_filter(test_signal)

    # Plot results
    plt.figure(figsize=(10, 6))
    plt.subplot(3, 1, 1)
    plt.plot(t, test_signal, label="Original Signal with Interference")
    plt.legend()
    plt.subplot(3, 1, 2)
    plt.plot(t, filtered_signal, label="Filtered Signal")
    plt.legend()
    plt.subplot(3, 1, 3)
    plt.magnitude_spectrum(test_signal, Fs=sample_rate, scale='dB', label="Original")
    plt.magnitude_spectrum(filtered_signal, Fs=sample_rate, scale='dB', label="Filtered")
    plt.legend()
    plt.tight_layout()
    plt.show()