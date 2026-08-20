import os
import json
import re
import streamlit as st
import google.generativeai as genai


def get_gemini_api_key() -> str:
    api_key = ""
    
    # Cek Gemini API dari Streamlit Secrets
    try:
        if "GEMINI_API_KEY" in st.secrets:
            api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        pass

    # Clean whitespace & quotes jika ada
    api_key = api_key.strip().strip("'").strip('"')
    return api_key


def configure_genai():
    api_key = get_gemini_api_key()
    if not api_key:
        raise ValueError(
            "API Key Gemini tidak valid atau tidak ditemukan. "
        )
    genai.configure(api_key=api_key)


# PROMPT & ENGINE GENERATE ANALISIS STUNTING
def generate_stunting_analysis(usia: int, gender: str, bb: float, tb: float, z_score: float, status: str, catatan: str) -> dict:
    configure_genai()
    
    model = genai.GenerativeModel('gemini-3.6-flash')

    prompt = f"""
Anda adalah pakar nutrisi anak dan spesialis tumbuh kembang anak (Dokter Spesialis Anak).
Analisis data antropometri anak berikut berdasarkan standar Permenkes RI No. 2 Tahun 2020:

Data Pasien:
- Usia: {usia} bulan
- Jenis Kelamin: {gender}
- Berat Badan: {bb} kg
- Tinggi/Panjang Badan: {tb} cm
- Kalkulasi Z-Score (TB/U): {z_score} SD
- Status Antropometri: {status}
- Catatan Orang Tua/Gejala: {catatan if catatan else "Tidak ada catatan tambahan."}

Tugas:
Berikan rekomendasi medis dan nutrisi dalam format JSON MURNI tanpa format markdown lain (seperti ```json).
Struktur JSON yang WAJIB dipenuhi:
{{
  "ringkasan_kondisi": "Ringkasan kondisi tumbuh kembang anak secara profesional dalam 2-3 kalimat ringkas.",
  "rekomendasi_nutrisi": [
    "Poin rekomendasi makanan/nutrisi spesifik 1",
    "Poin rekomendasi makanan/nutrisi spesifik 2",
    "Poin rekomendasi makanan/nutrisi spesifik 3"
  ],
  "tindak_lanjut": [
    "Langkah tindakan medis/praktis 1",
    "Langkah tindakan medis/praktis 2",
    "Langkah tindakan medis/praktis 3"
  ]
}}
"""

    try:
        response = model.generate_content(
            prompt,
            generation_config={"temperature": 0.3}
        )
        
        raw_text = response.text.strip()
        cleaned_text = re.sub(r"^```(?:json)?\s*", "", raw_text, flags=re.MULTILINE)
        cleaned_text = re.sub(r"\s*```$", "", cleaned_text, flags=re.MULTILINE).strip()
        
        result = json.loads(cleaned_text)
        return result

    except json.JSONDecodeError:
        # Fallback jika parsing JSON gagal
        return {
            "ringkasan_kondisi": f"Anak berusia {usia} bulan dengan status {status} (Z-Score: {z_score} SD). Perlu pemantauan rutin terhadap pola makan dan pertumbuhan bulanan.",
            "rekomendasi_nutrisi": [
                "Tingkatkan asupan protein hewani tinggi kualitas seperti telur, ikan, daging ayam, atau daging sapi.",
                "Berikan makanan kaya zat besi dan zink untuk mendukung kurva pertumbuhan linier.",
                "Pastikan porsi dan frekuensi Makanan Pendamping ASI (MPASI) sesuai dengan usia anak."
            ],
            "tindak_lanjut": [
                "Lakukan penimbangan dan pengukuran tinggi badan rutin setiap bulan di Posyandu/Puskesmas.",
                "Konsultasikan hasil analisis ini dengan Dokter Spesialis Anak atau Petugas Gizi Puskesmas.",
                "Evaluasi riwayat penyakit infeksi berulang yang dapat menghambat penyerapan nutrisi."
            ]
        }
    except Exception as e:
        raise RuntimeError(f"Gagal menghubungkan ke Gemini API: {str(e)}")