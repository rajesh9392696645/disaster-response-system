# disaster-response-system
Input → Prediction → Emergency Response → Result on Same Page
1. Create the Project Folder

Create the folders exactly like this:

disaster-response-system/
│
├── app.py
│
├── models/
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── utils/
│   ├── predictor.py
│   └── emergency.py
│
└── requirements.txt
2. Install Python

Check if Python is installed:

python --version

or

python3 --version

Expected output:

Python 3.10.x

If not installed, download Python from:

Python Official Website

3. Create Virtual Environment (Recommended)

Open terminal inside the project folder:

cd disaster-response-system

Create virtual environment:

Windows
python -m venv venv
venv\Scripts\activate
Linux/Mac
python3 -m venv venv
source venv/bin/activate
4. Create requirements.txt

Add:

Flask==3.0.3

Install dependencies:

pip install -r requirements.txt

Or directly:

pip install flask
5. Run the Application

From the project root:

python app.py

You should see:

* Running on http://127.0.0.1:5000
* Debug mode: on
6. Open Browser

Open:

http://127.0.0.1:5000

You should see:

Real-Time Disaster Prediction System

[Temperature]
[Rainfall]
[Humidity]
[Wind Speed]

[Predict]
7. Test Different Inputs
Test Case 1: Flood

Input:

Temperature = 30
Rainfall = 250
Humidity = 85
Wind = 20

Expected Result:

Disaster: Flood
Probability: 92%

Move to higher ground
Avoid river areas
Contact rescue services
Test Case 2: Wildfire

Input:

Temperature = 45
Rainfall = 10
Humidity = 20
Wind = 15

Expected Result:

Disaster: Wildfire
Probability: 85%
Test Case 3: Cyclone

Input:

Temperature = 30
Rainfall = 50
Humidity = 75
Wind = 90

Expected Result:

Disaster: Cyclone
Probability: 88%
Test Case 4: Normal

Input:

Temperature = 28
Rainfall = 20
Humidity = 50
Wind = 15

Expected Result:

Disaster: Normal
Probability: 20%
8. Common Errors
Error
ModuleNotFoundError: No module named 'flask'

Fix:

pip install flask
Error
TemplateNotFound: index.html

Fix:

Make sure:

templates/
└── index.html

The folder name must be exactly templates.

Error
No module named utils

Fix:

Create an empty file:

utils/__init__.py

Structure:

utils/
├── __init__.py
├── predictor.py
└── emergency.py
9. Demo Flow for Project Presentation
Open browser.
Enter environmental values.
Click Predict.
Flask sends data to backend.
Predictor identifies disaster type.
Emergency module generates actions.
Result appears on the same page
