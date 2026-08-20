import pandas as pd
import numpy as np
import os

def load_who_standards():
    data = [
        {"gender": "Laki-laki", "month": 0, "L": 1, "M": 49.88, "S": 0.0379},
        {"gender": "Laki-laki", "month": 6, "L": 1, "M": 67.62, "S": 0.0348},
        {"gender": "Laki-laki", "month": 12, "L": 1, "M": 75.75, "S": 0.0343},
        {"gender": "Laki-laki", "month": 24, "L": 1, "M": 87.12, "S": 0.0350},
        {"gender": "Laki-laki", "month": 36, "L": 1, "M": 96.08, "S": 0.0360},
        {"gender": "Laki-laki", "month": 48, "L": 1, "M": 103.32, "S": 0.0372},
        {"gender": "Laki-laki", "month": 60, "L": 1, "M": 110.02, "S": 0.0384},
        {"gender": "Perempuan", "month": 0, "L": 1, "M": 49.14, "S": 0.0379},
        {"gender": "Perempuan", "month": 6, "L": 1, "M": 65.74, "S": 0.0354},
        {"gender": "Perempuan", "month": 12, "L": 1, "M": 74.02, "S": 0.0349},
        {"gender": "Perempuan", "month": 24, "L": 1, "M": 85.71, "S": 0.0357},
        {"gender": "Perempuan", "month": 36, "L": 1, "M": 95.12, "S": 0.0368},
        {"gender": "Perempuan", "month": 48, "L": 1, "M": 102.70, "S": 0.0380},
        {"gender": "Perempuan", "month": 60, "L": 1, "M": 109.43, "S": 0.0392},
    ]
    return pd.DataFrame(data)


def calculate_zscore(usia_bulan: int, gender: str, tinggi_cm: float) -> tuple[float, str]:
    """
    Rumus Z-Score:
    Z = (((y / M) ** L) - 1) / (L * S)
    
    Kategori Status Gizi (Permenkes No. 2/2020):
    - Z < -3.0 SD             : Sangat Pendek (Severely Stunted)
    - -3.0 SD <= Z < -2.0 SD  : Pendek (Stunted)
    - -2.0 SD <= Z <= +3.0 SD : Normal
    - Z > +3.0 SD             : Tinggi
    """
    df_who = load_who_standards()
    
    # Filter gender & bulan terdekat
    subset = df_who[df_who["gender"] == gender]
    if subset.empty:
        subset = df_who
        
    # Cari nilai bulan terdekat
    idx = (subset["month"] - usia_bulan).abs().idxmin()
    row = subset.loc[idx]
    
    L = row["L"]
    M = row["M"]
    S = row["S"]
    
    # Hitung Z-score standar LMS
    if L != 0:
        z_score = (((tinggi_cm / M) ** L) - 1) / (L * S)
    else:
        z_score = np.log(tinggi_cm / M) / S
        
    z_score_rounded = round(float(z_score), 2)
    
    # Klasifikasi Status Stunting
    if z_score_rounded < -3.0:
        status = "Sangat Pendek (Severely Stunted)"
    elif -3.0 <= z_score_rounded < -2.0:
        status = "Pendek (Stunted)"
    elif -2.0 <= z_score_rounded <= 3.0:
        status = "Normal"
    else:
        status = "Tinggi"
        
    return z_score_rounded, status