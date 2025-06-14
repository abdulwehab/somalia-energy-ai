# 🇸🇴 Somalia National Load Forecasting AI Model

This project builds a machine learning model to forecast hourly electricity demand across major Somali regions. It supports rural mini-grid optimization and aligns with SESRP and ASCENT energy modernization goals.

---

## 📊 Dataset

Synthetic data (Jan–June 2024) for 10 regions:
- Mogadishu, Hargeisa, Bosaso, Kismayo, Garowe
- Baidoa, Beledweyne, Marka, Galkayo, Dhusamareeb

Each record includes:
- `timestamp`, `region`, `temperature`, `humidity`, `solar_input`, `population`, `holiday_flag`, `load_kWh`

---

## 🤖 Model

- **Algorithm**: Random Forest Regressor
- **MAE**: 0.77 kWh
- **RMSE**: 1.19 kWh
- **R²**: 0.78

Trained on weather, solar, time, and population inputs per region.

---

## 💻 Streamlit Dashboard

Predict regional electricity demand interactively.

### Run locally:

```bash
streamlit run streamlit_app_national_forecast.py
```

### Files required:
- `national_load_forecast_model.pkl`
- `somalia_national_load_dataset.csv`
- `requirements.txt`

---

## 🌍 Use Cases

- Forecast evening peak loads in rural mini-grids
- Optimize solar-diesel hybrid planning
- Support ESPs with real-time demand insights

---

## 📝 Concept Note & Pilot

A 1-page PDF proposal is available for submission to:
- Ministry of Energy & Water Resources
- SESRP / ASCENT
- Donor organizations (USAID, GIZ, WB)

---

## 📁 Files Included

| File | Purpose |
|------|---------|
| `streamlit_app_national_forecast.py` | Interactive dashboard |
| `national_load_forecast_model.pkl` | Trained ML model |
| `somalia_national_load_dataset.csv` | Regional synthetic dataset |
| `requirements.txt` | Package list |
| `README.md` | This file |

---

## 📜 License

MIT License – free to use with attribution.

---

## 👨‍💻 Developed by

Abdiwahab Khalif Jama  
Electrical & Electronics Engineer | AI for Energy Access  

