# 🚗 AI-Based Parking Space Detection & Prediction System

<p align="center">
  <img src="assets/banner.png" alt="AI Parking System Banner" width="100%">
</p>

![Python](https://img.shields.io/badge/Python-3.10-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![MongoDB](https://img.shields.io/badge/Database-MongoDB-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

# 📌 Project Overview

The **AI-Based Parking Space Detection & Prediction System** is a Final Year Major Project developed under the domain of Artificial Intelligence and Data Science.

This system automatically detects vacant and occupied parking slots using Computer Vision and Deep Learning techniques. It also predicts future parking availability using historical data trends. The solution integrates a real-time web dashboard for monitoring and visualization.

The objective is to reduce traffic congestion, minimize fuel wastage, and support smart city infrastructure through intelligent parking management.

---

# 🎯 Problem Statement

Urban areas face increasing parking challenges due to rising vehicle density. Drivers spend significant time searching for parking spaces, leading to:

* Traffic congestion
* Fuel wastage
* Environmental pollution
* Inefficient parking utilization

This project aims to develop a scalable AI-based system that automates parking detection and predicts availability in real time.

---

# 🏗️ System Architecture

## High-Level Architecture

```
CCTV Cameras
      ↓
Video Frame Capture
      ↓
Image Preprocessing (OpenCV)
      ↓
Parking Slot Detection
      ↓
CNN Classification Model
      ↓
Database Storage
      ↓
Prediction Engine
      ↓
Backend API (Flask/FastAPI)
      ↓
React Web Dashboard
```

---

# 🧠 Methodology

## 1. Image Acquisition

* Live video feed from CCTV cameras
* Frame extraction for processing

## 2. Image Preprocessing

* Image resizing
* Noise reduction
* Normalization
* Region of Interest (ROI) extraction

## 3. Parking Slot Detection

* Segmentation techniques
* Bounding box extraction

## 4. Deep Learning Classification

* Convolutional Neural Network (CNN)
* Binary classification:

  * 0 → Vacant
  * 1 → Occupied

## 5. Prediction Module

* Historical occupancy data analysis
* Time-series modeling
* Future slot availability prediction

---

# 📊 Model Details

### Model Type

Convolutional Neural Network (CNN)

### Training Dataset

* Labeled images of parking slots
* Categories: Vacant and Occupied
* Data augmentation applied

### Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

---

# 💻 Technology Stack

## Backend

* Python
* Flask / FastAPI
* TensorFlow / Keras
* OpenCV
* NumPy
* Pandas

## Frontend

* React.js
* HTML5
* CSS3

## Database

* MongoDB / MySQL

## Tools

* VS Code
* Jupyter Notebook
* Git & GitHub

---

# 📁 Project Structure

```
ai-parking-space-detection-prediction/
│
├── dataset/
│   ├── vacant/
│   └── occupied/
│
├── models/
│   ├── cnn_model.h5
│   └── training_script.py
│
├── backend/
│   ├── app.py
│   ├── routes.py
│   └── prediction.py
│
├── frontend/
│   ├── src/
│   └── public/
│
├── utils/
│
├── requirements.txt
├── LICENSE
└── README.md
```

---

# ⚙️ Installation & Setup

## Step 1: Clone Repository

```bash
git clone https://github.com/your-username/ai-parking-space-detection-prediction.git
cd ai-parking-space-detection-prediction
```

## Step 2: Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Run Backend

```bash
python app.py
```

## Step 5: Run Frontend

```bash
cd frontend
npm install
npm start
```

---

# 📤 Expected Output

* Number of vacant parking spaces
* Number of occupied parking spaces
* Slot-wise parking status
* Real-time dashboard visualization
* Future parking availability prediction

---

# 🌍 Applications

* Smart Cities
* Shopping Malls
* Airports
* Corporate Offices
* Railway Stations
* Event Parking Management

---

# 🔐 Challenges Addressed

* Variable lighting conditions
* Weather variations
* Camera angle differences
* Real-time performance optimization
* Large dataset handling

---

# 🚀 Future Scope

* Mobile application integration
* Online slot reservation system
* IoT sensor integration
* Cloud deployment
* Edge AI for real-time inference

---

# 👨‍💻 Team Members

* Krishna Chandrakant Patil (TY DS – 52)
* Borse Tejas Narendra (TY DS – 55)
* Kalpesh Rajendra Patil (TY DS – 31)

---

# 🎓 Academic Information

Final Year Major Project
Department of Computer Science & Engineering (Data Science)
Academic Year: 2025–2026

---

# 📜 License

This project is licensed under the MIT License.
