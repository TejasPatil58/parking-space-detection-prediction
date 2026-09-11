import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

st.set_page_config(layout="wide")

st.title("🚗 Parking Space Detection")

uploaded_file = st.file_uploader(
    "Upload Parking Image",
    type=["jpg", "jpeg", "png"]
)

try:
    model = YOLO("models/best.pt")
except Exception as e:
    st.error(f"Model Loading Error: {e}")
    st.stop()

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    img_array = np.array(image)

    results = model(img_array)

    annotated_img = results[0].plot()

    st.image(
        annotated_img,
        caption="Detection Result",
        use_container_width=True
    )

    occupied = 0
    empty = 0
    confidences = []

    for box in results[0].boxes:

        cls = int(box.cls[0])

        label = model.names[cls].lower()

        confidences.append(float(box.conf[0]))

        if "occupied" in label:
            occupied += 1

        elif "empty" in label:
            empty += 1

    total = occupied + empty

    occupancy_percent = (
        occupied / total * 100
        if total > 0 else 0
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "🚗 Occupied Slots",
        occupied
    )

    col2.metric(
        "🅿️ Empty Slots",
        empty
    )

    col3.metric(
        "📊 Total Slots",
        total
    )

    st.progress(occupancy_percent / 100)

    st.info(
        f"Parking Occupancy: {occupancy_percent:.1f}%"
    )

    if occupancy_percent < 50:
        st.success("🟢 Plenty of Parking Available")

    elif occupancy_percent < 80:
        st.warning("🟡 Moderate Occupancy")

    else:
        st.error("🔴 Parking Nearly Full")

    if confidences:
        avg_conf = sum(confidences) / len(confidences)

        st.info(
            f"🎯 Average Detection Confidence: {avg_conf:.2f}"
        )