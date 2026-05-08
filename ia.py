import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

st.title("🤖 Inteligencia Artificial")

st.subheader("Predicción de perfil de sabor")

# Datos simulados
X = np.array([
    [180, 8],
    [200, 10],
    [220, 12],
    [210, 11],
    [190, 9]
])

y = np.array([1, 2, 3, 2.5, 1.5])  # perfil sabor

model = LinearRegression()
model.fit(X, y)

temp = st.slider("Temperatura", 150, 250, 200)
tiempo = st.slider("Tiempo", 5, 20, 10)

pred = model.predict([[temp, tiempo]])

st.metric("Perfil de sabor estimado", round(pred[0],2))

if pred < 1.5:
    st.write("☕ Perfil ácido")
elif pred < 2.5:
    st.write("🍫 Perfil balanceado")
else:
    st.write("🔥 Perfil intenso")