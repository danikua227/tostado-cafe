import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("☕ Simulador de Tostión")

# ---------------- MODELO ----------------

def parametros_base(tostion):
    if tostion == "Clara":
        return 180, 12, 5, 8
    elif tostion == "Media":
        return 200, 11, 5.5, 10
    elif tostion == "Fuerte":
        return 220, 10, 6, 12

def ajustar_tiempo(tiempo_base, peso, temp, hum):
    factor_peso = 1 + (peso - 250) / 500
    factor_temp = 1 - (temp - 200) / 400
    factor_hum = 1 + (hum - 10) / 50
    return tiempo_base * factor_peso * factor_temp * factor_hum

def simular(temp, hum, pres, tiempo):
    t = np.linspace(0, tiempo, 100)

    temp_grano = temp * (1 - np.exp(-t/3))
    humedad = hum * (1 - t/tiempo)
    presion = 1 + (pres-1)*(t/tiempo)

    aminoacidos = np.exp(-0.3*t)
    azucares = np.exp(-0.2*t)
    compuestos = 1 - np.exp(-0.4*t)

    reaccion_maillard = compuestos * (temp_grano / temp)

    return t, temp_grano, humedad, presion, aminoacidos, azucares, compuestos, reaccion_maillard

# ---------------- SIDEBAR ----------------

st.sidebar.header("⚙️ Parámetros")

cafe = st.sidebar.selectbox("Tipo de café", ["Caturro", "Castillo"])
peso = st.sidebar.slider("Peso (g)", 50, 500, 250)

tostion = st.sidebar.selectbox("Tostión", ["Clara", "Media", "Fuerte", "Personalizada"])

if tostion == "Personalizada":
    temp = st.sidebar.slider("Temperatura (°C)", 150, 250, 200)
    hum = st.sidebar.slider("Humedad (%)", 8, 15, 11)
    pres = st.sidebar.slider("Presión (atm)", 1.0, 6.0, 5.0)
    tiempo = st.sidebar.slider("Tiempo base (min)", 3, 20, 10)
else:
    temp, hum, pres, tiempo = parametros_base(tostion)

# 🔥 TIEMPO DINÁMICO
tiempo = ajustar_tiempo(tiempo, peso, temp, hum)

# ---------------- SIMULACIÓN ----------------

t, temp_g, hum_g, pres_g, aa, az, comp, maillard = simular(temp, hum, pres, tiempo)

indice_maillard = np.trapz(maillard, t)
consistencia = 100 - np.std(temp_g)
eficiencia = (10 / tiempo) * 100

# ---------------- KPIs ----------------

col1, col2, col3 = st.columns(3)

col1.metric("🔥 Índice Maillard", round(indice_maillard,2))
col2.metric("⚙️ Eficiencia", f"{eficiencia:.1f}%")
col3.metric("🎯 Consistencia", f"{consistencia:.1f}%")

# ---------------- GRÁFICAS ----------------

st.subheader("⏱ Curva de tostión")

fig1, ax1 = plt.subplots()
ax1.plot(t, temp_g, label="Temperatura")
ax1.plot(t, hum_g, label="Humedad")
ax1.plot(t, pres_g, label="Presión")
ax1.legend()
ax1.set_xlabel("Tiempo")
st.pyplot(fig1)

st.subheader("🧪 Reacción de Maillard")

fig2, ax2 = plt.subplots()
ax2.plot(t, aa, label="Aminoácidos")
ax2.plot(t, az, label="Azúcares")
ax2.plot(t, maillard, label="Maillard")
ax2.legend()
ax2.set_xlabel("Tiempo")
st.pyplot(fig2)

# ---------------- RECOMENDACIONES ----------------

st.subheader("🧠 Recomendaciones")

if indice_maillard < 200:
    st.warning("Aumentar temperatura o tiempo")
elif indice_maillard > 400:
    st.warning("Reducir temperatura para evitar sobre-tostión")
else:
    st.success("Perfil de tostión óptimo")