# 🦖 Dino-Identifier: A Paleontological Classifier

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.x-orange?style=for-the-badge&logo=scikit-learn)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

An immersive web application that uses machine learning to classify dinosaurs as either **Carnivores** or **Herbivores** based on their fossil measurements. This project showcases an end-to-end ML workflow, from data exploration to a fully interactive and thematically designed deployment.

 Live Demo -> https://dino-identifier.streamlit.app/

---

## ✨ Core Features

- **Immersive & Thematic UI:** A custom-styled interface with a background image that transports the user to a paleontological setting, providing a unique and engaging experience.
- **Real-time Classification:** Leverages a trained `RandomForestClassifier` to provide instant predictions on dinosaur diet.
- **Interactive Fossil Analysis Panel:** A clean sidebar allows users to input fossil data (length, geological age) using intuitive sliders.
- **Detailed & Visual Results:** The application presents the prediction, confidence level, and input summary in a clear, professional dashboard format, complete with high-quality imagery.
- **Reproducible Workflow:** The entire process—from data cleaning and exploratory analysis in a Jupyter Notebook to model training in a Python script—is documented and easy to reproduce.


---

## ✨ Features

- Train a classifier using sample data
- Interactive web UI for predictions
- Easy local deployment with Streamlit

---

## 🛠️ Tech Stack

- **Python 3.9+**
- **Pandas, NumPy**
- **Scikit-learn**
- **Streamlit**

---

## 📁 Project Structure

```
ml-streamlit-app/
├── app.py                  # Streamlit app script
├── model.pkl               # Trained model file (optional)
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation (you are here!)
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ml-streamlit-app.git
cd ml-streamlit-app
```

### 2. Create and activate virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

Then open the app in your browser.

---

## 📜 License

This project is licensed under the MIT License.