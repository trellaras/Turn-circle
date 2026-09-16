import math
import streamlit as st

st.set_page_config(page_title="Υπολογιστής Κύκλου Στροφής", page_icon="🔄")

st.title("🔄 Υπολογιστής Κύκλου Στροφής")

# Εισαγωγή δεδομένων σε στήλες
col1, col2 = st.columns(2)

with col1:
    speed = st.number_input("Ταχύτητα:", min_value=0.1, value=10.0, step=0.5)
    unit = st.selectbox("Μονάδα Ταχύτητας:", ["Knots", "km/h"])

with col2:
    rate = st.number_input("Ρυθμός Στροφής (°/sec):", min_value=0.1, value=3.0, step=0.1)

if st.button("🚀 Υπολογισμός", type="primary"):
    # Μετατροπή ταχύτητας σε m/s
    v_ms = speed * 0.514444 if unit == "Knots" else speed / 3.6
    
    # Μετατροπή ρυθμού στροφής σε rad/s
    omega = math.radians(rate)

    # Υπολογισμοί
    radius_m = v_ms / omega
    diameter_m = 2 * radius_m

    radius_nm = radius_m / 1852
    diameter_nm = diameter_m / 1852

    # Εμφάνιση αποτελεσμάτων
    st.success("### Αποτελέσματα")
    st.write(f"**Ακτίνα (R):** {radius_m:.2f} m (`{radius_nm:.3f} NM`)")
    st.write(f"**Διάμετρος (D):** {diameter_m:.2f} m (`{diameter_nm:.3f} NM`)")
