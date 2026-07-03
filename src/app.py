from pathlib import Path

from flask import Flask, render_template, request
import joblib

BASE_DIR = Path(__file__).resolve().parents[1]
MODEL_PATH = BASE_DIR / "models" / "model.pkl"
TEMPLATES_DIR = BASE_DIR / "templates"

app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

# Load model
model = joblib.load(MODEL_PATH)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Prediction
@app.route('/predict', methods=['POST'])
def predict():

    size = float(request.form['size'])
    bedrooms = float(request.form['bedrooms'])

    result = model.predict([[size, bedrooms]])

    return render_template(
        'index.html',
        prediction_text=f'Predicted House Price: {result[0]:,.2f}'
    )

if __name__ == "__main__":
    app.run(debug=True)
