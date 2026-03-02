import pandas as pd
import matplotlib.pyplot as plt
import mplcursors


# Function to convert from degrees, minutes and seconds to decimal
def dms_to_degree(Degree, Minute, Arcsec):
    decimal = Degree + Minute/60 + Arcsec/3600
    return round(decimal, 4)


AZ_Data = "D:/POS Planet Observation Data/Azimuth Data.csv"
ALT_Data = "D:/POS Planet Observation Data/Altitude Data.csv"

df_az = pd.read_csv(AZ_Data)
df_alt = pd.read_csv(ALT_Data)


if "Decimal" not in df_az.columns:
    df_az["Decimal"] = df_az.apply(lambda row: dms_to_degree(row["Degree"], row['Minute'], row['Arcsec']), axis=1)

if "Decimal" not in df_alt.columns:
    df_alt["Decimal"] = df_alt.apply(lambda row: dms_to_degree(row["Degree"], row['Minute'], row['Arcsec']), axis=1)

az_decimal = df_az["Decimal"]
alt_decimal = df_alt["Decimal"]
dates = df_alt["Date"]


if len(az_decimal) != len(alt_decimal):
    raise ValueError("AZ and ALT data lengths do not match!")


# AZIMUTH vs ALTITUDE
plt.figure(figsize=(100, 100))
scatter = plt.scatter(alt_decimal, az_decimal, label='AZ vs ALT', marker= 'o', color='black')
plt.plot(alt_decimal, az_decimal, label='AZ vs ALT', color='black', linestyle='--', lw= 1, ms=1)


plt.title('Azimuth vs Altitude ')
plt.xlabel('Azimuth in Degrees')
plt.ylabel('Altitude in Degrees')
plt.legend()
plt.grid()
cursor = mplcursors.cursor(scatter, hover=True)

# Define what the annotation displays
@cursor.connect("add")
def on_add(sel):
    index = sel.index  
    sel.annotation.set_text(f"Date: {dates.iloc[index]}\nAZ: {az_decimal.iloc[index]}\nALT: {alt_decimal.iloc[index]}")


# AZ vs Date Graph
plt.figure(figsize=(100, 100))
plt.plot(az_decimal, dates, marker = '*', color = 'black', ls = '-', lw = 1, ms=2, label = 'AZ vs Date')
plt.title("Azimuth vs Date Graph")
plt.xlabel("Azimuth")
plt.ylabel("Date")
plt.legend()


# ALT vs Date
plt.figure(figsize=(100, 100))
plt.plot(alt_decimal, dates, marker = '*', color = 'black', ls = '-', lw = 1, ms=2, label ='ALT vs Date')
plt.title("Altitude vs Date Graph")
plt.xlabel('ALTITUDE')
plt.ylabel('Date')
plt.legend()


plt.show()