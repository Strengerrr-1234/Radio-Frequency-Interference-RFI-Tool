# Radio-Frequency-Interference-RFI-Tool

Python code for detecting and blocking Radio Frequency Interference (RFI). This code is a simplified simulation and uses signal processing techniques like bandpass filtering to identify and mitigate interference.


## 1. Libraries Used
* `numpy`: Used for numerical computations, such as creating arrays and performing mathematical operations.
* `scipy.signal`: Provides signal processing functions, such as designing filters.
* `matplotlib.pyplot`: Used for plotting and visualizing data.


## 2. Class Definition: `RFIBlocker`
   The `RFIBlocker` class is designed to handle Radio Frequency Interference (RFI) in signals by applying a bandstop filter.


## 3. `__init__` Method
* Initializes the instance with:
    * `sample_rate`: Sampling rate of the signal in Hz.
    * `signal_band`: Frequency range of the desired signal, given as a tuple (e.g., `(20, 50)` Hz).
    * `interference_band`: Frequency range of the interference, given as a tuple (e.g., `(100, 120)` Hz).

This sets up the basic parameters needed for signal processing.


## 4. `bandstop_filter` Method
* ### Purpose:
     Removes interference by applying a bandstop filter, which suppresses frequencies in the interference range.
* ### Steps:
     1. ### Normalize Frequencies:
          Convert the interference band frequencies to a range of 0–1 relative to the Nyquist frequency (Nyquist=sample rate2Nyquist=2sample rate​).
     2. ### Design the Filter:
          Use `scipy.signal.butter` to design a 4th-order Butterworth bandstop filter.
     3. ### Filter the Data:
          Use `scipy.signal.filtfilt` to apply the filter. This method ensures zero-phase distortion.

The result is a filtered signal where the interference has been removed.


## 5. `generate_test_signal` Method
* ### Purpose:
     Creates a synthetic signal containing both the desired signal and interference.
* ### Parameters:
    `duration`: Duration of the generated signal in seconds (default is 1 second).
* Steps:
    1. ### Create a Time Array:
        Use `np.linspace` to create a uniformly spaced time array.
    2. ### Generate Desired Signal:
         A sine wave with a frequency in the `signal_band` range.
    3. ### Generate Interference Signal:
         A sine wave with a frequency in the `interference_band` range.
    4. ### Combine Signals:
         Add the desired signal and interference to create a test signal.


## 6. Example Usage
### Setup
  * ### Parameters:
      * `sample_rate = 1000`: Sampling rate in Hz.
      * `signal_band = (20, 50)`: Frequency range of the desired signal in Hz.
      * `interference_band = (100, 120)`: Frequency range of interference in Hz.
### Steps
  1. ### Instantiate `RFIBlocker`: 
      Create an object with the given parameters.
  2. ### Generate Test Signal: 
      Use `generate_test_signal` to simulate a signal with interference.
  3. ### Apply Bandstop Filter: 
      Use `bandstop_filter` to remove interference.


## 7. Visualization
* ### Plot the Results:
    * ### Original Signal with Interference:
         Time-domain signal before filtering.
    * ### Filtered Signal:
         Time-domain signal after filtering.
    * ### Magnitude Spectrum:
         Frequency-domain representation of both signals, showing the suppression of interference.

The plots visually demonstrate how the bandstop filter effectively removes interference from the signal.


## 8. Expected Output
The script generates three subplots:

  1. ### Original Signal with Interference:
        A time-domain waveform with visible interference.
  3. ### Filtered Signal:
        A cleaner time-domain waveform after interference removal.
  5. ### Frequency Spectrum:
        * ### Before Filtering:
             Shows peaks in both the signal and interference frequency ranges.
        * ### After Filtering:
             Shows suppression in the interference frequency range.
