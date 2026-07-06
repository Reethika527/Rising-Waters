import joblib

model = joblib.load("floods.save")

joblib.dump(model, "model.pkl")

print("Model saved successfully")