import numpy as np
import joblib

from tensorflow.keras.models import load_model

model = load_model("models/lstm_model.h5")

scaler = joblib.load("models/scaler.pkl")

encoder = joblib.load("models/label_encoder.pkl")


def predict_disaster(
    temperature,
    rainfall,
    humidity,
    wind_speed
):

    data = np.array([
        [
            temperature,
            rainfall,
            humidity,
            wind_speed
        ]
    ])

    data = scaler.transform(data)

    data = data.reshape(
        1,
        1,
        4
    )

    prediction = model.predict(
        data,
        verbose=0
    )

    class_id = np.argmax(prediction)

    disaster = encoder.inverse_transform(
        [class_id]
    )[0]

    return disaster