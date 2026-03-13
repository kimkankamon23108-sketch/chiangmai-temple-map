import streamlit as st

st.title("แผนที่วัดในจังหวัดเชียงใหม่")

st.write("เว็บแสดงแผนที่วัด")
from streamlit_folium import st_folium
import folium

m = folium.Map(location=[18.7883,98.9853], zoom_start=12)

st_folium(m)
