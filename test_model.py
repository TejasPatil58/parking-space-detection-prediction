import joblib

print("Loading model...")

model = joblib.load("models/parking_model.pkl")

print("Model Loaded Successfully")
print(type(model))