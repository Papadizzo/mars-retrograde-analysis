# Mars Retrograde Motion Analysis

Tracked Mars' position over 3 months using Stellarium to observe its apparent retrograde motion.

## 📊 Data
- Daily altitude measurements (Sept 30 - Dec 31)
- Daily azimuth measurements (Sept 30 - Dec 31)
- 90+ days of observations

## 🐍 Code
Python script that:
- Converts DMS (Degrees, Minutes, Seconds) to decimal degrees
- Creates three visualizations:
  - Azimuth vs Altitude (with interactive hover)
  - Azimuth vs Date
  - Altitude vs Date

## 📈 Results
The graphs clearly show Mars' apparent retrograde motion - when the planet appears to move backward in the sky relative to background stars.

## 🛠️ Technologies
- Python
- Pandas (data processing)
- Matplotlib (visualizations)
- mplcursors (interactive graphs)

## 🚀 How to Run
1. Install requirements: `pip install pandas matplotlib mplcursors`
2. Run: `python POS_Assignment_Clean.py`
