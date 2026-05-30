import pandas as pd
import numpy as np
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.utils import to_categorical

# Load dataset
df = pd.read_csv("dataset/disaster_data.csv")

# Features
X = df[[
    "temperature",
    "rainfall",
    "humidity",
    "wind_speed"
]]

# Target
y = df["disaster"]

# Encode labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Save label encoder
joblib.dump(
    label_encoder,
    "models/label_encoder.pkl"
)

# Scale data
scaler = MinMaxScaler()

X_scaled = scaler.fit_transform(X)

# Save scaler
joblib.dump(
    scaler,
    "models/scaler.pkl"
)

# Convert to sequence shape
X_scaled = X_scaled.reshape(
    X_scaled.shape[0],
    1,
    X_scaled.shape[1]
)

# One hot encode
y_cat = to_categorical(y_encoded)

# Build LSTM
model = Sequential()

model.add(
    LSTM(
        64,
        input_shape=(1,4)
    )
)

model.add(
    Dense(
        32,
        activation="relu"
    )
)

model.add(
    Dense(
        y_cat.shape[1],
        activation="softmax"
    )
)

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

model.fit(
    X_scaled,
    y_cat,
    epochs=30,
    batch_size=8
)

model.save(
    "models/lstm_model.h5"
)

print("LSTM Model Saved")