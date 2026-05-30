from flask import Flask, render_template, request
from utils.predictor import predict_disaster
from utils.emergency import generate_response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        temperature = float(request.form["temperature"])
        rainfall = float(request.form["rainfall"])
        humidity = float(request.form["humidity"])
        wind = float(request.form["wind"])

        disaster = predict_disaster(
            temperature,
            rainfall,
            humidity,
            wind
        )

        result = generate_response(disaster)

    return render_template(
        "index.html",
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)