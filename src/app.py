from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load model
model = joblib.load("model.pkl")

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