import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

# Cargar el modelo y el scaler
modelo = joblib.load("modelo_random_forest.pkl")
scaler = joblib.load("scaler.pkl")

# Configuración de la página
st.title("Predicción del promedio de horas en pantalla")
st.subheader("Realizado por Leonardo Waked y Jeison Steven Salcedo")
st.write("Esta aplicación predice el tiempo promedio de pantalla en niños basado en características específicas.")
st.image("https://img.freepik.com/foto-gratis/ninos-tiro-medio-dispositivos-interiores_23-2149056211.jpg", use_container_width=True)

# Entrada de datos
age = st.slider("Edad", 4, 16, 10)
gender = st.selectbox("Género", ["Male", "Female", "Other/Prefer not to say"])
screen_time_type = st.selectbox("Tipo de uso de pantalla", ["Educational", "Recreational", "Total"])
day_type = st.selectbox("Tipo de día", ["Weekday", "Weekend"])

# Convertir entradas categóricas a numéricas
gender_dict = {"Male": 0, "Female": 1, "Other/Prefer not to say": 2}
screen_time_dict = {"Educational": 0, "Recreational": 1, "Total": 2}
day_type_dict = {"Weekday": 0, "Weekend": 1}

gender_num = gender_dict[gender]
screen_time_type_num = screen_time_dict[screen_time_type]
day_type_num = day_type_dict[day_type]

# Crear DataFrame para la predicción
data = pd.DataFrame([[age, gender_num, screen_time_type_num, day_type_num]], 
                    columns=["Age", "Gender", "Screen Time Type", "Day Type"])

# Escalar los datos
scaled_data = scaler.transform(data)

# Hacer la predicción
prediccion = modelo.predict(scaled_data)[0]

# Mostrar resultados
st.subheader("Predicción del tiempo promedio en pantalla")
st.write(f"**{prediccion:.2f} horas**")

if prediccion <= 2:
    st.success("El tiempo de pantalla se encuentra en buen manejo del tiempo.")
elif 2 < prediccion <= 4:
    st.warning("El tiempo de pantalla está en el máximo recomendado.")
else:
    st.error("¡Cuidado! El tiempo de pantalla está en un límite riesgoso para la salud de los niños.")

# Sección informativa
st.markdown("---")
st.write("**Información sobre el uso de pantallas en niños:**")
st.write("El uso excesivo de pantallas en la infancia puede afectar el desarrollo físico y mental. Estudios han demostrado que una exposición prolongada puede causar fatiga ocular, alteraciones en el sueño y una reducción en la capacidad de atención. Además, el sedentarismo asociado con el uso excesivo de dispositivos electrónicos incrementa el riesgo de obesidad infantil y problemas posturales.")

# Pie de página
st.markdown("---")
st.write("© UNAB 2025")
