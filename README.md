# 🌟 A Comprehensive Measure of Well-Being

An end-to-end **Machine Learning Lifecycle** project that analyzes environmental and socioeconomic indicators using a housing market dataset to model and predict comprehensive well-being. The project demonstrates the complete ML workflow — from data collection and preprocessing to model training, evaluation, serialization, and deployment through a Flask web application.

---

## 📖 Table of Contents

- [Description](#description)
- [Epic 1: Environment Setup and Package Installation](#epic-1-environment-setup-and-package-installation)
- [Epic 2: Importing Required Libraries](#epic-2-importing-required-libraries)
- [Epic 3: Dataset Download and Understanding](#epic-3-dataset-download-and-understanding)
- [Epic 4: Data Preprocessing and Label Encoding](#epic-4-data-preprocessing-and-label-encoding)
- [Epic 5: Dividing the Dataset into Train and Test Data](#epic-5-dividing-the-dataset-into-train-and-test-data)
- [Epic 6: Fitting the Model](#epic-6-fitting-the-model)
- [Epic 7: Saving the Model](#epic-7-saving-the-model)
- [Epic 8: Building the Flask Web Application](#epic-8-building-the-flask-web-application)
- [Repository Structure](#-repository-structure)
- [Technologies Used](#-technologies-used)
- [Installation](#-installation)
- [Running the Project](#-running-the-project)
- [Future Enhancements](#-future-enhancements)
- [Author](#-author)

---

## Description

The project is developed through a structured workflow consisting of multiple epics, covering data collection, analysis, preprocessing, model development, and deployment. Each epic focuses on a specific stage of the machine learning lifecycle to ensure systematic and efficient project execution.

---

## Epic 1: Environment Setup and Package Installation

**Story 1:** Download and install all required Python packages, machine learning libraries, and Flask dependencies needed for the project (NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn, Pickle, Flask).

**Story 2:** Create and organize the project folder structure, including directories for datasets, models, templates, static files, and source code.

```
A-Comprehensive-Measure-of-Well-Being/
│
├── datasets/
│   └── house_price_dataset.csv
│
├── models/
│   └── model.pkl
│
├── src/
│   └── train.py
│
├── templates/
│   └── index.html
│
├── ER Diagram.png
├── app.py
├── requirements.txt
└── README.md
```

---

## Epic 2: Importing Required Libraries

**Story 1:** Import all necessary libraries and modules such as NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn, Pickle, and Flask to support data analysis, model development, and web application creation.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import pickle
from flask import Flask, request, render_template
```

---

## Epic 3: Dataset Download and Understanding

**Story 1:** Download the dataset from Kaggle and load it into the development environment. The dataset is stored in `datasets/house_price_dataset.csv`.

**Story 2:** Explore and understand the dataset structure, features, target variable, and data types using:

```python
df.head()
df.info()
df.describe()
df.shape
```

**Story 3:** Perform data visualization to identify patterns, trends, distributions, and relationships within the dataset — including histograms, scatter plots, correlation heatmaps, distribution plots, and pairwise relationships. These analyses help identify feature correlations, data distribution, outliers, and potential predictive variables.

---

## Epic 4: Data Preprocessing and Label Encoding

**Story 1:** Select dependent and independent variables required for model training, separating the feature set (X) from the target variable (Y).

**Story 2:** Check for missing values and handle null entries appropriately to improve data quality using:

```python
df.isnull().sum()
```

**Story 3:** Perform label encoding to convert categorical text values into numerical representations suitable for machine learning algorithms, since Linear Regression cannot process categorical text directly.

```
Urban    → 0
Suburban → 1
Rural    → 2
```

**Story 4:** Prepare the cleaned and transformed dataset for model development by removing inconsistencies, converting categorical values, and building the final training matrix.

---

## Epic 5: Dividing the Dataset into Train and Test Data

**Story 1:** Split the processed dataset into training and testing sets to enable model learning and performance evaluation on unseen data.

- **Training Data:** 80%
- **Testing Data:** 20%

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

---

## Epic 6: Fitting the Model

**Story 1:** Train the Linear Regression model using the prepared training dataset.

```python
model = LinearRegression()
model.fit(X_train, y_train)
```

**Story 2:** Generate predictions using the trained model and analyze the prediction results.

```python
y_pred = model.predict(X_test)
```

**Story 3:** Evaluate model performance using appropriate regression metrics and visualizations, including prediction comparison, residual analysis, and accuracy assessment.

---

## Epic 7: Saving the Model

**Story 1:** Save the trained Linear Regression model using serialization techniques such as Pickle so it can be reused without retraining.

```python
import pickle
pickle.dump(model, open("models/model.pkl", "wb"))
```

**Story 2:** Store the model file for deployment and future prediction purposes at `models/model.pkl`, enabling faster loading and easy integration into the Flask application.

---

## Epic 8: Building the Flask Web Application

**Story 1:** Develop the Flask backend to handle user requests, process inputs, load the trained model, and generate predictions.

```python
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open("models/model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    features = [float(x) for x in request.form.values()]
    prediction = model.predict([features])
    return render_template("index.html", prediction_text=f"Predicted Well-Being Score: {prediction[0]}")

if __name__ == "__main__":
    app.run(debug=True)
```

**Story 2:** Create HTML templates and integrate them with Flask to provide a user-friendly interface (`templates/index.html`) with a clean input form and dynamic prediction display.

**Story 3:** Run, test, and validate the complete web application to ensure accurate predictions and smooth functionality.

```
User Input → HTML Form → Flask Backend → Load model.pkl → Prediction → Display Result
```

---

## 📁 Repository Structure

```
A-Comprehensive-Measure-of-Well-Being/
│
├── datasets/
│   └── house_price_dataset.csv
│
├── models/
│   └── model.pkl
│
├── src/
│   └── train.py
│
├── templates/
│   └── index.html
│
├── ER Diagram.png
├── app.py
├── requirements.txt
└── README.md
```

---

## 🧰 Technologies Used

| Category              | Technologies         |
|------------------------|-----------------------|
| Programming Language  | Python                |
| Data Processing        | Pandas, NumPy         |
| Visualization          | Matplotlib, Seaborn   |
| Machine Learning       | Scikit-learn          |
| Model Serialization    | Pickle                |
| Backend                 | Flask                 |
| Frontend                | HTML5                 |
| Version Control        | Git & GitHub          |

---

## ⚡ Installation

Clone the repository:

```bash
git clone https://github.com/AsunthaPeyyala/A-Comprehensive-Measure-of-Well-Being.git
cd A-Comprehensive-Measure-of-Well-Being
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶ Running the Project

**Step 1 (optional):** Retrain the model:

```bash
python src/train.py
```

**Step 2:** Run the Flask application:

```bash
python app.py
```

**Step 3:** Open your browser at:

```
http://127.0.0.1:5000/
```

---

## 🔮 Future Enhancements

- Deploy on Render or Railway
- Docker containerization
- Cloud deployment on AWS or Azure
- Feature scaling and normalization
- Advanced regression algorithms
- Hyperparameter tuning
- Cross-validation
- REST API development
- Interactive dashboard integration
- Authentication and user management

---

## 👨‍💻 Author

Developed as a complete Machine Learning Lifecycle project demonstrating data preprocessing, feature engineering, model training, evaluation, serialization, and Flask deployment for real-world predictive analytics.

---

⭐ If you found this project useful, consider giving the repository a star on GitHub!
