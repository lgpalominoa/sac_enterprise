import folium
from streamlit_folium import st_folium
from sales.motor import MotorVentas

def render_sales(user):
    st_folium.header("📍 Radar de Empresas")

    col1, col2 = st.columns([3,1])
    search_type = col2.selectbox("Buscar por", ["Ciudad", "ZIP Code"])
    query = col1.text_input("Ubicación")

    if st_folium.button("Buscar"):
        motor = MotorVentas()
        coords = motor.geocode(query)

        if not coords:
            st_folium.error("Ubicación no encontrada")
            return

        lat, lon = coords
        companies = motor.search_business(lat, lon)

        m = folium.Map(location=[lat, lon], zoom_start=14)
        for c in companies:
            if c["Lat"] and c["Lon"]:
                folium.Marker(
                    [c["Lat"], c["Lon"]],
                    popup=c["Nombre"]
                ).add_to(m)

        st_folium(m, height=400)
        st.dataframe(companies, use_container_width=True)
