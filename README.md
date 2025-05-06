# 🧠 Malnutrition Risk Predictor

This is a simple AI project that helps predict **malnutrition risk** (Normal, MAM, or SAM) in children based on a few basic health indicators — like age, weight, and arm size.  
It uses machine learning (Random Forest) and is built with beginner-friendly tools like **Streamlit**, **pandas**, and **scikit-learn**.

---

## ✨ What This Project Does

- ✅ Takes a CSV file of child data (age, weight, MUAC, growth history)
- ✅ Predicts if each child is at risk of **malnutrition**
- ✅ Shows results instantly on a clean, interactive web page

Perfect for health workers, NGOs, or anyone learning AI for social good.

---

## 🧾 Files Inside

```bash
Malnutrition-Risk-Predictor/
├── main.py                  # Script to train and save the AI model
├── malnutrition_model.pkl   # Your trained model (auto-created after training)
├── malnutrition_app.py      # The Streamlit web app
├── sample_children_data.csv # Example input file
├── README.md                # You're reading this
└── .venv/                   # (Optional) Python virtual environment

---


```
---

## 🚀 How to Get Started

### 1. Download or Clone This Project

```bash
git clone https://github.com/yadavlakshya743/Malnutrition-Risk-Predictor.git

cd Malnutrition-Risk-Predictor
```
### 2. Create and Activate a Python Environment
```bash python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install the Required Libraries
If you have a requirements.txt file:

```bash
pip install -r requirements.txt
```
#### Or install manually:
 ``` bash
pip install pandas scikit-learn streamlit joblib numpy==1.23 scipy
```

## 🧠 Train Your Model
This step builds the AI brain.

```bash
python3 main.py
```
#### After running, you’ll get a new file:

```bash
malnutrition_model.pkl
```
#### That's your trained model!

🌐 Run the Web App
Open the app in your browser:

```bash

streamlit run malnutrition_app.py
```
#### Visit the URL shown (usually http://localhost:8501) to interact with the app.

## 📄 Sample Data Format
Use a CSV file that looks like this:


## 🧰 Tools Used
🐍 Python 3

📊 pandas

🔍 scikit-learn

🌐 Streamlit (for the frontend)

💾 joblib (to save/load the model)

## 💡 Why I Built This
This was made as a quick demo for using AI in public health — especially for tracking malnutrition risk in children.
It's simple enough to build in under 2 hours, even with little coding experience, thanks to Streamlit and Python!
