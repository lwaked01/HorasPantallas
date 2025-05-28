import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

# Configuración de la página
st.set_page_config(page_title="Predicción de Horas en Pantalla", layout="centered")

# Cargar modelo y scaler
modelo = joblib.load("modelo_random_forest.pkl")
scaler = joblib.load("scaler.pkl")

# Título y encabezado
st.markdown("<h1 style='text-align: center; color: #0E76A8;'>📱 Predicción del Promedio de Horas en Pantalla</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Realizado por <i>Leonardo Waked</i> y <i>Jeison Steven Salcedo</i></h4>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)
st.write("Esta aplicación predice el tiempo promedio de pantalla en niños basado en características específicas.")

st.image(
    "https://img.freepik.com/foto-gratis/ninos-tiro-medio-dispositivos-interiores_23-2149056211.jpg",
    use_container_width=True
)

# Entrada de datos organizada en columnas
st.markdown("### 🧩 Ingreso de características:")

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Edad", 4, 16, 10)
    gender = st.selectbox("Género", ["Male", "Female", "Other/Prefer not to say"])
    sample_size = st.slider("Tamaño de muestra estimado", 50, 500, 100)

with col2:
    screen_time_type = st.selectbox("Tipo de uso de pantalla", ["Educational", "Recreational", "Total"])
    day_type = st.selectbox("Tipo de día", ["Weekday", "Weekend"])

# Diccionarios para convertir a numérico
gender_dict = {"Male": 0, "Female": 1, "Other/Prefer not to say": 2}
screen_time_dict = {"Educational": 0, "Recreational": 1, "Total": 2}
day_type_dict = {"Weekday": 0, "Weekend": 1}

gender_num = gender_dict[gender]
screen_time_type_num = screen_time_dict[screen_time_type]
day_type_num = day_type_dict[day_type]

# DataFrame para predicción
data = pd.DataFrame([[
    age, gender_num, screen_time_type_num, day_type_num
]], columns=["Age", "Gender", "Screen Time Type", "Day Type"])

# Escalado y predicción
scaled_data = scaler.transform(data)
prediccion = modelo.predict(scaled_data)[0]

# Resultado de la predicción
st.markdown("---")
st.markdown("### 🎯 Predicción del Tiempo Promedio de Pantalla")
st.write(f"📊 **{prediccion:.2f} horas**")

if prediccion <= 2:
    st.success("✅ El tiempo de pantalla se encuentra en un rango saludable.")
elif 2 < prediccion <= 4:
    st.warning("⚠️ El tiempo de pantalla está en el límite máximo recomendado.")
else:
    st.error("🚨 ¡Cuidado! El tiempo de pantalla es riesgoso para la salud infantil.")

# Sección informativa
st.markdown("---")
st.markdown("### 📚 Información sobre el uso de pantallas en niños")
st.write(
    "El uso excesivo de pantallas puede tener múltiples efectos negativos en la salud infantil. "
    "Desde una edad temprana, los niños están en pleno desarrollo cognitivo, físico y emocional. "
    "La sobreexposición a dispositivos electrónicos puede alterar los patrones de sueño, aumentar la irritabilidad, "
    "y disminuir la capacidad de concentración y socialización. Además, estudios médicos han relacionado el tiempo prolongado "
    "frente a pantallas con problemas de visión, postura y un aumento en el sedentarismo, lo que incrementa el riesgo de obesidad infantil. "
    "Por ello, es fundamental supervisar y limitar el tiempo de pantalla, promoviendo actividades recreativas y al aire libre que contribuyan "
    "a un desarrollo integral y saludable."
)

# Pie de página
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>© UNAB 2025</p>", unsafe_allow_html=True)
