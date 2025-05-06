import streamlit as st
import pandas as pd
import joblib

@st.cache_data
def load_model():
    return joblib.load("malnutrition_model.pkl")

model = load_model()

st.title("Malnutrition Risk Predictor")
st.write("Upload a CSV file with child data:")

uploaded_file = st.file_uploader("Choose a CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Input Data:", df)

    preds = model.predict(df)
    label_map = {0: "Normal", 1: "MAM", 2: "SAM"}
    df["Malnutrition Risk"] = [label_map[p] for p in preds]

    st.write("Prediction Results:")
    st.write(df)
    st.download_button(
        label="Download Results",
        data=df.to_csv(index=False).encode('utf-8'),
        file_name='predictions.csv',
        mime='text/csv'
    )
else:
    st.write("Please upload a CSV file to see the predictions.")
# This is a simple Streamlit app that allows users to upload a CSV file containing child data