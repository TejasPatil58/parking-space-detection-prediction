import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

st.set_page_config(layout="wide")

st.title("📈 Smart Parking Prediction")

model = joblib.load("models/parking_model.pkl")

st.markdown(
"""
Predict future parking occupancy using
date and time.
"""
)

selected_date = st.date_input(
    "📅 Select Date"
)

selected_time = st.time_input(
    "⏰ Select Time"
)

if st.button("Predict Parking Availability"):

    hour = selected_time.hour

    day = selected_date.day

    month = selected_date.month

    weekday = selected_date.weekday()

    future_data = pd.DataFrame(
        [[hour, day, month, weekday]],
        columns=[
            "hour",
            "day",
            "month",
            "weekday"
        ]
    )

    prediction = model.predict(
        future_data
    )

    occupied = max(
        0,
        int(prediction[0])
    )

    total_slots = 100

    available = max(
        0,
        total_slots - occupied
    )

    col1, col2 = st.columns(2)

    col1.metric(
        "🚗 Predicted Occupied Slots",
        occupied
    )

    col2.metric(
        "🅿️ Predicted Available Slots",
        available
    )

    occupancy = occupied / total_slots * 100

    st.progress(
        occupancy / 100
    )

    st.info(
        f"Expected Occupancy: {occupancy:.1f}%"
    )

    if occupancy < 30:
        st.success(
            "🟢 Low Traffic Expected"
        )

    elif occupancy < 70:
        st.warning(
            "🟡 Moderate Traffic Expected"
        )

    else:
        st.error(
            "🔴 Heavy Traffic Expected"
        )