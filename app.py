import math
import streamlit as st

st.set_page_config(page_title="Υπολογιστής Στροφής & G-Force", page_icon="✈️")

st.title("✈️ Υπολογιστής Στροφής & G-Force")

col1, col2 = st.columns(2)

with col1:
    speed = st.number_input("Ταχύτητα:", min_value=0.1, value=300.0, step=10.0)
    unit = st.selectbox("Μονάδα Ταχύτητας:", ["Knots", "km/h"])

with col2:
    rate = st.number_input("Ρυθμός Στροφής (°/sec):", min_value=0.1, value=12.0, step=0.5)

if st.button("🚀 Υπολογισμός", type="primary"):
    # Μετατροπές
    v_ms = speed * 0.514444 if unit == "Knots" else speed / 3.6
    omega = math.radians(rate)

    # Βασικοί υπολογισμοί
    radius_m = v_ms / omega
    diameter_m = 2 * radius_m
    radius_nm = radius_m / 1852
    diameter_nm = diameter_m / 1852

    # Υπολογισμός G-Force
    g_turn = (v_ms * omega) / 9.80665
    g_total = math.sqrt(1 + g_turn**2)

    # Υπολογισμός γωνίας κλίσης (Bank Angle) για οριζόντια στροφή
    bank_angle_deg = math.degrees(math.atan(g_turn))

    # Αποτελέσματα
    st.success("### Αποτελέσματα")
    
    col_res1, col_res2 = st.columns(2)
    with col_res1:
        st.write(f"**Ακτίνα (R):** {radius_m:.2f} m (`{radius_nm:.3f} NM`)")
        st.write(f"**Διάμετρος (D):** {diameter_m:.2f} m (`{diameter_nm:.3f} NM`)")
    
    with col_res2:
        st.write(f"**Φορτίο G (Στροφής):** `{g_turn:.2f} G`")
        st.write(f"**Συνολικό Φορτίο G:** `{g_total:.2f} G`")
        st.write(f"**Απαιτούμενη Κλίση (Bank Angle):** `{bank_angle_deg:.1f}°`")
