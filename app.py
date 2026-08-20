import streamlit as st
from src.ui_components import (
    apply_theme, 
    render_header, 
    render_hero, 
    render_form, 
    render_result_dashboard, 
    render_empty_state, 
    render_medical_disclaimer
)
from src.zscore_calc import calculate_zscore
from src.ai_engine import generate_stunting_analysis

st.set_page_config(
    page_title="AIDE-Stunt - Deteksi Tumbuh Kembang Anak",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def main():
    apply_theme()
    render_header()
    render_hero()
    
    col_left, col_right = st.columns([1, 1.1], gap="large")
    
    with col_left:
        submit_btn, usia, gender, bb, tb, catatan = render_form()
        
    with col_right:
        if submit_btn:
            with st.spinner("⏳ Menghitung Z-Score & memproses analisis AI..."):
                # Hitung Z-Score
                z_score, status = calculate_zscore(usia_bulan=usia, gender=gender, tinggi_cm=tb)
                
                # Panggil AI Engine
                try:
                    ai_result = generate_stunting_analysis(
                        usia=usia,
                        gender=gender,
                        bb=bb,
                        tb=tb,
                        z_score=z_score,
                        status=status,
                        catatan=catatan
                    )
                    render_result_dashboard(z_score, status, ai_result)
                except Exception as e:
                    st.error(f"⚠️ Terjadi Kesalahan pada Analisis AI: {str(e)}")
                    render_empty_state()
        else:
            render_empty_state()
            
    # Footer
    render_medical_disclaimer()

if __name__ == "__main__":
    main()