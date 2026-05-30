import pandas as pd
import numpy as np
import joblib

from tensorflow.keras.models import load_model

# Load model
model = load_model(
    "models/lstm_model.h5"
)

# Load scaler
scaler = joblib.load(
    "models/scaler.pkl"
)

# Load encoder
encoder = joblib.load(
    "models/label_encoder.pkl"
)

# Sample input

temperature = 45
rainfall = 10
humidity = 20
wind_speed = 15

sample = np.array([
    [
        temperature,
        rainfall,
        humidity,
        wind_speed
    ]
])

sample = scaler.transform(sample)

sample = sample.reshape(
    1,
    1,
    4
)

prediction = model.predict(sample)

class_id = np.argmax(prediction)

disaster = encoder.inverse_transform(
    [class_id]
)

print("\nPrediction:")
print(disaster[0])