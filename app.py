import streamlit as st

st.set_page_config(
    page_title="Smart Parking System",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 Smart Parking System")

st.markdown("""
## Welcome

This Smart Parking System provides:

✅ Parking Space Detection using YOLOv8

✅ Parking Occupancy Analysis

✅ Future Parking Prediction using Machine Learning

Use the sidebar to navigate between pages.
""")

st.image(
    "https://images.unsplash.com/photo-1506521781263-d8422e82f27a",
    use_container_width=True
)