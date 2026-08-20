import streamlit as st

THEME = {
    "primary": "#00A6A6",        
    "primary_dark": "#00796B",   
    "primary_light": "#E6F7F6",  
    "secondary": "#2563EB",      
    "background": "#F8FAFC",     
    "surface": "#FFFFFF",        
    "text_primary": "#0F172A",   
    "text_secondary": "#64748B", 
    "border": "#E2E8F0",         
    "success": "#16A34A",        
    "warning": "#F59E0B",        
    "danger": "#DC2626",         
    "info": "#2563EB",       
}


def apply_theme():
    st.markdown("""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <style>
        header[data-testid="stHeader"], 
        .stAppHeader, 
        [data-testid="stHeader"] {{
            background-color: transparent !important;
            background: transparent !important;
        }}

        div[data-testid="stToolbar"] {{
            color: {THEME['text_primary']} !important;
        }}

        html, body, [class*="css"], .stApp {{
            font-family: 'Inter', system-ui, -apple-system, sans-serif !important;
            background-color: {THEME['background']} !important;
            color: {THEME['text_primary']} !important;
        }}

        .block-container {{
            max-width: 1200px !important;
            padding-top: 1.5rem !important;
            padding-bottom: 3rem !important;
        }}

        .app-header {{
            background-color: {THEME['surface']};
            border-bottom: 1px solid {THEME['border']};
            padding: 12px 24px;
            margin: -1.5rem -1rem 1.5rem -1rem;
            border-bottom-left-radius: 12px;
            border-bottom-right-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }}

        .brand-badge {{
            background-color: {THEME['primary_light']};
            color: {THEME['primary_dark']};
            border: 1px solid rgba(0, 166, 166, 0.2);
            padding: 4px 12px;
            border-radius: 9999px;
            font-size: 12px;
            font-weight: 600;
        }}

        .hero-card {{
            background-color: {THEME['surface']};
            border: 1px solid {THEME['border']};
            border-radius: 16px;
            padding: 20px 24px;
            margin-bottom: 24px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.03);
        }}

        .pill-tag {{
            display: inline-block;
            background-color: {THEME['primary_light']};
            color: {THEME['primary_dark']};
            font-size: 11px;
            font-weight: 600;
            padding: 4px 10px;
            border-radius: 6px;
            margin-bottom: 8px;
        }}

        .card-container {{
            background-color: {THEME['surface']};
            border: 1px solid {THEME['border']};
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 24px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.03);
        }}

        .card-header {{
            border-bottom: 1px solid {THEME['border']};
            padding-bottom: 12px;
            margin-bottom: 16px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        label, p, .stWidgetLabel, div[data-testid="stMarkdownContainer"] p {{
            color: {THEME['text_primary']} !important;
            font-weight: 600 !important;
        }}

        div[data-baseweb="input"], 
        div[data-baseweb="base-input"],
        div[data-baseweb="input"] > div,
        input[type="number"],
        input[type="text"],
        textarea {{
            background-color: #FFFFFF !important;
            color: {THEME['text_primary']} !important;
            -webkit-text-fill-color: {THEME['text_primary']} !important;
            border-radius: 10px !important;
        }}

        ::placeholder, textarea::placeholder, input::placeholder {{
            color: {THEME['text_secondary']} !important;
            opacity: 0.7 !important;
            -webkit-text-fill-color: {THEME['text_secondary']} !important;
        }}

        div[role="radiogroup"] label {{
            color: {THEME['text_primary']} !important;
            background-color: #FFFFFF !important;
            border: 1px solid {THEME['border']} !important;
            padding: 6px 14px !important;
            border-radius: 8px !important;
            font-size: 13px !important;
        }}

        div[data-testid="stNumberInputContainer"] button {{
            background-color: {THEME['primary_light']} !important;
            color: {THEME['primary_dark']} !important;
            border: 1px solid {THEME['border']} !important;
            border-radius: 8px !important;
        }}

        div[data-testid="stNumberInputContainer"] button:hover {{
            background-color: {THEME['primary']} !important;
            color: #FFFFFF !important;
        }}

        .stButton > button, div[data-testid="stFormSubmitButton"] > button {{
            background-color: {THEME['primary']} !important;
            color: #FFFFFF !important;
            font-weight: 600 !important;
            font-size: 15px !important;
            border-radius: 10px !important;
            border: none !important;
            height: 48px !important;
            width: 100% !important;
            transition: all 0.2s ease !important;
            box-shadow: 0 2px 4px rgba(0, 166, 166, 0.2) !important;
        }}

        .stButton > button:hover, div[data-testid="stFormSubmitButton"] > button:hover {{
            background-color: {THEME['primary_dark']} !important;
        }}

        .result-box {{
            background-color: {THEME['background']};
            border: 1px solid {THEME['border']};
            border-radius: 10px;
            padding: 12px 16px;
            margin-bottom: 10px;
            font-size: 14px;
            color: {THEME['text_primary']};
        }}

        /* BADGES STATUS */
        .badge-stunted {{
            background-color: #FEF2F2;
            color: {THEME['danger']};
            border: 1px solid #FCA5A5;
            padding: 4px 12px;
            border-radius: 9999px;
            font-weight: 600;
            font-size: 12px;
            display: inline-block;
        }}

        .badge-normal {{
            background-color: #F0FDF4;
            color: {THEME['success']};
            border: 1px solid #86EFAC;
            padding: 4px 12px;
            border-radius: 9999px;
            font-weight: 600;
            font-size: 12px;
            display: inline-block;
        }}

        .disclaimer-card {{
            background-color: #EFF6FF;
            border: 1px solid #BFDBFE;
            border-radius: 12px;
            padding: 14px 18px;
            margin-top: 24px;
            font-size: 12px;
            color: #1E40AF;
            display: flex;
            gap: 12px;
            align-items: flex-start;
        }}

        #MainMenu, footer {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)


def render_header():
    st.markdown(f"""
        <div class="app-header">
            <div style="display: flex; align-items: center; gap: 12px;">
                <div style="width: 38px; height: 38px; background-color: {THEME['primary_light']}; border-radius: 10px; display: flex; align-items: center; justify-content: center; color: {THEME['primary']}; font-size: 18px;">
                    <i class="fa-solid fa-stethoscope"></i>
                </div>
                <div>
                    <h2 style="margin: 0; font-size: 18px; font-weight: 700; color: {THEME['text_primary']}; line-height: 1.2;">AIDE-Stunt</h2>
                    <p style="margin: 0; font-size: 12px; color: {THEME['text_secondary']};">Pedoman Tumbuh Kembang Anak</p>
                </div>
            </div>
            <div>
                <span class="brand-badge">
                    <i class="fa-solid fa-circle" style="font-size: 8px; color: {THEME['primary']}; margin-right: 4px;"></i> AI Screening Mode
                </span>
            </div>
        </div>
    """, unsafe_allow_html=True)


def render_hero():
    st.markdown(f"""
        <div class="hero-card">
            <span class="pill-tag"><i class="fa-solid fa-ribbon"></i> Standar Permenkes RI No. 2/2020</span>
            <h2 style="margin: 4px 0 8px 0; font-size: 20px; font-weight: 700; color: {THEME['text_primary']};">Deteksi Dini Tumbuh Kembang Anak</h2>
            <p style="margin: 0; font-size: 13px; color: {THEME['text_secondary']}; line-height: 1.5;">
                Pantau pertumbuhan anak secara presisi dengan kalkulasi Z-Score antropometri dan rekomendasi nutrisi berbasis AI yang aman serta terpercaya.
            </p>
        </div>
    """, unsafe_allow_html=True)


def render_form():
    st.markdown(f"""
        <div class="card-container">
            <div class="card-header">
                <div>
                    <h3 style="margin: 0; font-size: 16px; font-weight: 700; color: {THEME['text_primary']};">
                        <i class="fa-solid fa-clipboard-user" style="color: {THEME['primary']}; margin-right: 6px;"></i>
                        Data Antropometri Anak
                    </h3>
                    <p style="margin: 2px 0 0 0; font-size: 12px; color: {THEME['text_secondary']};">Lengkapi parameter di bawah untuk memulai analisis screening.</p>
                </div>
                <span style="font-size: 11px; background-color: {THEME['background']}; padding: 4px 8px; border-radius: 6px; color: {THEME['text_secondary']}; font-weight: 600;">Langkah 1/2</span>
            </div>
    """, unsafe_allow_html=True)

    with st.form("stunting_form"):
        st.markdown(f'<label style="font-size: 13px; font-weight: 600; color: {THEME["text_primary"]}; margin-bottom: 6px; display: block;">Jenis Kelamin</label>', unsafe_allow_html=True)
        gender = st.radio(
            "Jenis Kelamin", 
            options=["👦 Laki-laki", "👧 Perempuan"], 
            horizontal=True,
            label_visibility="collapsed"
        )
        gender_clean = "Laki-laki" if "Laki-laki" in gender else "Perempuan"

        usia = st.number_input(
            "Umur (Bulan)", 
            min_value=0, 
            max_value=60, 
            value=12, 
            step=1,
            help="Masukkan umur anak dalam rentang 0 hingga 60 bulan."
        )

        col_bb, col_tb = st.columns(2)
        with col_bb:
            bb = st.number_input(
                "Berat Badan (kg)", 
                min_value=1.0, 
                max_value=40.0, 
                value=9.2, 
                step=0.1, 
                format="%.1f"
            )
        with col_tb:
            tb = st.number_input(
                "Tinggi Badan (cm)", 
                min_value=40.0, 
                max_value=130.0, 
                value=75.7, 
                step=0.1, 
                format="%.1f"
            )

        catatan = st.text_area(
            "Catatan Nutrisi & Gejala Klinis",
            placeholder="Contoh: Anak jarang makan protein hewani, sering batuk pilek, aktif bergerak...",
            height=90,
            help="Informasi tambahan memberikan konteks lebih mendalam bagi analisis AI."
        )

        st.markdown('<div style="margin-top: 16px;"></div>', unsafe_allow_html=True)
        submit_btn = st.form_submit_button("⚡ Analisis Pertumbuhan Anak", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)
    return submit_btn, usia, gender_clean, bb, tb, catatan


def render_result_dashboard(z_score, status, data_json):
    st.markdown(f"""
        <div class="card-container">
            <div class="card-header">
                <div>
                    <h3 style="margin: 0; font-size: 16px; font-weight: 700; color: {THEME['text_primary']};">
                        <i class="fa-solid fa-square-poll-vertical" style="color: {THEME['primary']}; margin-right: 6px;"></i>
                        Hasil Screening Antropometri
                    </h3>
                    <p style="margin: 2px 0 0 0; font-size: 12px; color: {THEME['text_secondary']};">Laporan diagnostik hasil kalkulasi Z-Score dan AI Engine.</p>
                </div>
                <span class="badge-normal"><i class="fa-solid fa-check" style="margin-right: 4px;"></i>Selesai</span>
            </div>
    """, unsafe_allow_html=True)

    res_col1, res_col2 = st.columns(2)
    with res_col1:
        st.metric("Nilai Z-Score (TB/U)", f"{z_score} SD")
    with res_col2:
        st.write("**Status Antropometri:**")
        if "Pendek" in status or "Stunted" in status:
            badge_html = f'<span class="badge-stunted"><i class="fa-solid fa-triangle-exclamation" style="margin-right: 4px;"></i>{status}</span>'
        else:
            badge_html = f'<span class="badge-normal"><i class="fa-solid fa-circle-check" style="margin-right: 4px;"></i>{status}</span>'
        st.markdown(badge_html, unsafe_allow_html=True)

    st.markdown(f'<div style="border-top: 1px solid {THEME["border"]}; margin: 16px 0;"></div>', unsafe_allow_html=True)

    # 1. Ringkasan
    st.markdown(f"""
        <div style="background-color: {THEME['primary_light']}; border: 1px solid rgba(0, 166, 166, 0.2); border-radius: 10px; padding: 14px; margin-bottom: 16px;">
            <div style="font-weight: 600; font-size: 13px; color: {THEME['primary_dark']}; margin-bottom: 4px;">
                <i class="fa-solid fa-lightbulb" style="margin-right: 6px;"></i>Ringkasan Kondisi Anak
            </div>
            <p style="margin: 0; font-size: 13px; color: {THEME['text_primary']}; line-height: 1.5;">
                {data_json.get("ringkasan_kondisi", "-")}
            </p>
        </div>
    """, unsafe_allow_html=True)

    # 2. Rekomendasi Nutrisi
    st.markdown(f'<h4 style="font-size: 13px; font-weight: 700; color: {THEME["text_primary"]}; margin-bottom: 8px;"><i class="fa-solid fa-apple-whole" style="color: {THEME["success"]}; margin-right: 6px;"></i>Rekomendasi Nutrisi AI</h4>', unsafe_allow_html=True)
    for item in data_json.get("rekomendasi_nutrisi", []):
        st.markdown(f'<div class="result-box"><i class="fa-solid fa-check" style="color: {THEME["success"]}; margin-right: 8px;"></i>{item}</div>', unsafe_allow_html=True)

    # 3. Tindak Lanjut
    st.markdown(f'<h4 style="font-size: 13px; font-weight: 700; color: {THEME["text_primary"]}; margin-top: 16px; margin-bottom: 8px;"><i class="fa-solid fa-user-doctor" style="color: {THEME["info"]}; margin-right: 6px;"></i>Langkah Tindak Lanjut</h4>', unsafe_allow_html=True)
    for index, langkah in enumerate(data_json.get("tindak_lanjut", []), start=1):
        st.markdown(f'<div class="result-box"><span style="font-weight: 700; color: {THEME["primary"]}; margin-right: 8px;">0{index}.</span>{langkah}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


def render_empty_state():
    st.markdown(f"""
        <div class="card-container" style="text-align: center; padding: 40px 20px;">
            <div style="width: 48px; height: 48px; background-color: {THEME['background']}; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 12px auto; color: {THEME['text_secondary']}; font-size: 20px;">
                <i class="fa-solid fa-chart-simple"></i>
            </div>
            <h4 style="margin: 0 0 6px 0; font-size: 15px; font-weight: 700; color: {THEME['text_primary']};">Hasil Screening Belum Tersedia</h4>
            <p style="margin: 0; font-size: 13px; color: {THEME['text_secondary']}; line-height: 1.5;">
                Silakan isi data antropometri buah hati Anda pada formulir di samping, lalu klik <b>Analisis Pertumbuhan Anak</b>.
            </p>
        </div>
    """, unsafe_allow_html=True)


def render_medical_disclaimer():
    st.markdown(f"""
        <div class="disclaimer-card">
            <i class="fa-solid fa-circle-info" style="font-size: 16px; margin-top: 2px;"></i>
            <div>
                <b>Disclaimer Medis:</b> Aplikasi ini dirancang sebagai sarana deteksi dini (screening) awal dan bukan pengganti diagnosis medis resmi. Konsultasikan tumbuh kembang anak secara berkala dengan Dokter Spesialis Anak atau Tenaga Kesehatan di Puskesmas/Posyandu.
            </div>
        </div>
    """, unsafe_allow_html=True)


def render_footer():
    render_medical_disclaimer()