import joblib

model = joblib.load("models/parking_model.pkl")

print(model.feature_names_in_)