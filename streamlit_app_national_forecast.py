import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Somalia National Load Forecast", layout="centered")
st.title("🔋 Somalia National Load Forecasting Dashboard")

model = joblib.load("national_load_forecast_model_compressed.pkl")


st.markdown("Use the form below to simulate an hourly forecast for a region.")

region = st.selectbox("Region", [
    "Hargeisa", "Bosaso", "Kismayo", "Garowe", "Baidoa",
    "Beledweyne", "Marka", "Galkayo", "Dhusamareeb", "Mogadishu"
])
hour = st.slider("Hour of Day", 0, 23, 18)
month = st.slider("Month", 1, 12, 6)
dow = st.slider("Day of Week (0=Mon)", 0, 6, 0)
temp = st.slider("Temperature (°C)", 24.0, 38.0, 31.0)
humidity = st.slider("Humidity (%)", 30, 80, 55)
solar = st.slider("Solar Input (kW)", 0.0, 5.0, 2.5)
pop = st.slider("Population Served", 50000, 400000, 120000, 1000)
holiday = st.selectbox("Holiday?", [0, 1])

features = {
    "hour": [hour],
    "day_of_week": [dow],
    "month": [month],
    "population_served": [pop],
    "temperature_C": [temp],
    "humidity": [humidity],
    "solar_input_kW": [solar],
    "holiday_flag": [holiday]
}

# Add region one-hot
for r in ["Hargeisa", "Bosaso", "Kismayo", "Garowe", "Baidoa",
          "Beledweyne", "Marka", "Galkayo", "Dhusamareeb"]:
    features[f"region_{r}"] = [1 if r == region else 0]

input_df = pd.DataFrame(features)
prediction = model.predict(input_df)[0]

st.success(f"⚡ Predicted Load: {prediction:.2f} kWh")
