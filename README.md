# Predicción del Promedio de Horas en Pantalla
Proyecto interdisciplinario: Machine Learning + Streamlit + Android Studio

La app toma datos como edad, género, tipo de uso de pantalla y tipo de día para predecir el tiempo estimado de exposición a pantallas. Se muestran mensajes según el resultado:

- ✅ < 2h: Buen manejo del tiempo
- ⚠️ ≈ 2h: Tiempo máximo recomendado
- ❌ > 4h: Límite riesgoso para la salud

El sistema consta de los siguientes componentes principales:

- Python (Scikit-learn, Pandas, Streamlit)
- Modelo: Random Forest Regressor
- Escalado: StandardScaler
- Kotlin + Jetpack Compose (Android)
- Comunicación: WebView


**Archivos Clave**
- App.py: Aplicación Streamlit

- modelo_random_forest.pkl: Modelo entrenado

- scaler.pkl: Escalador

- AndroidApp/: Proyecto Android Studio
  

**Autores**

Leonardo Waked

Jeison Steven Salcedo

© UNAB - 2025
