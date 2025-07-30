# 🧠 Titanic Survival Predictor

A machine learning web app to predict passenger survival on the Titanic using logistic regression. Built using `scikit-learn`, `pandas`, and `Streamlit`.

---
Live Demo - > https://dino-identifier.streamlit.app/
## 🚀 Features

- Predict survival based on passenger data
- Data preprocessing included
- Model evaluation with accuracy, confusion matrix, and classification report
- Streamlit-based user interface

---

## 📁 Project Structure

```
titanic-survival-predictor/
├── app.py                   # Streamlit app
├── model/
│   └── model.joblib         # Trained ML model
├── data/
│   └── cleaned_titanic.csv  # Processed dataset
├── notebooks/
│   └── titanic_exploration.ipynb  # Jupyter notebook (EDA + training)
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/titanic-survival-predictor.git
cd titanic-survival-predictor
```

### 2. Create a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

## 🧠 Train the Model

If needed, retrain the model:

```bash
# Inside a script or notebook
python -m notebooks.titanic_exploration.ipynb
```

Or extract the training logic to a `train.py` file and run:

```bash
python train.py
```

---

## 🌐 Run the Streamlit App

```bash
streamlit run app.py
```

Go to `http://localhost:8501` in your browser.

---

## 🧪 Dependencies

- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- streamlit
- joblib

Install with:

```bash
pip install -r requirements.txt
```

---

## 📄 License

MIT License