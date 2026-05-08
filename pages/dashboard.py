import streamlit as st

st.set_page_config(page_title="Software de Tostión", layout="wide")

st.title("☕ Plataforma Inteligente de Perfiles de Tostión")

# =========================
# SECCIÓN 1: INDICADORES
# =========================
st.header(" Indicadores del Sistema")

st.markdown("Métricas clave para evaluar el rendimiento del software y su impacto en el negocio.")

# INDICADOR 1
with st.expander(" Tasa de Optimización de Tostión"):
    st.write("Mide qué tanto mejora el software los perfiles de tostión.")
    st.latex(r'''
    \frac{Perfiles\ Mejorados}{Total\ de\ Perfiles} \times 100
    ''')
    st.write(" **¿Para qué sirve?** Permite comprobar si el software realmente agrega valor mejorando la calidad del perfil de tostión.")

# INDICADOR 2
with st.expander(" Tiempo Promedio de Tostión"):
    st.write("Evalúa la eficiencia del proceso.")
    st.latex(r'''
    \frac{\sum Tiempo}{Número\ de\ tostiones}
    ''')
    st.write(" **¿Para qué sirve?** Ayuda a identificar si el proceso es eficiente; menos tiempo implica mayor productividad y menores costos.")

# INDICADOR 3
with st.expander(" Consistencia del Perfil"):
    st.write("Mide la repetibilidad de los resultados.")
    st.latex(r'''
    \sigma = \sqrt{\frac{\sum (x_i - \mu)^2}{n}}
    ''')
    st.write(" **¿Para qué sirve?** Permite asegurar que los perfiles se puedan repetir con la misma calidad; menor variación significa mayor confiabilidad.")

# INDICADOR 4
with st.expander(" Retención de Clientes"):
    st.write("Mide cuántos clientes siguen usando el software.")
    st.latex(r'''
    \frac{Clientes\ Activos}{Clientes\ Totales} \times 100
    ''')
    st.write("**¿Para qué sirve?** Indica si el software es útil y valioso para los clientes a largo plazo.")

# INDICADOR 5
with st.expander(" Uso del Software"):
    st.write("Frecuencia de uso por usuario.")
    st.latex(r'''
    \frac{Sesiones}{Usuarios}
    ''')
    st.write("**¿Para qué sirve?** Permite medir qué tan necesario es el software en el día a día del usuario.")

# INDICADOR 6
with st.expander("Satisfacción del Cliente"):
    st.write("Nivel de satisfacción promedio.")
    st.latex(r'''
    \frac{\sum Calificaciones}{Usuarios}
    ''')
    st.write("**¿Para qué sirve?** Evalúa la percepción del usuario y la aceptación general del software.")


# =========================
# SECCIÓN 2: MODELO DE NEGOCIO
# =========================
st.header("Modelo de Negocio")

st.markdown("Estructura del modelo de negocio del software de perfiles de tostión.")

with st.expander("Propuesta de Valor"):
    st.write("""
    - Personalización inteligente de perfiles de tostión  
    - Mejora en la calidad del café  
    - Reducción de errores humanos  
    - Ahorro de tiempo y costos  
    """)

with st.expander("Segmento de Clientes"):
    st.write("""
    - Tostadores de café artesanales  
    - Empresas cafeteras  
    - Emprendedores del café  
    - Laboratorios de calidad  
    """)

with st.expander("Canales"):
    st.write("""
    - Plataforma web (Streamlit)  
    - Redes sociales  
    - Marketing digital  
     st.subheader("📱 Síguenos en Instagram")

    st.image("qr_instagram.png", caption="Escanea para ir a nuestro Instagram")

    st.write(" Escanea el código QR para acceder directamente a nuestro perfil.")
    """)

with st.expander("Relación con Clientes"):
    st.write("""
    - Soporte técnico  
    - Capacitación  
    - Atención personalizada  
    """)

with st.expander("Fuentes de Ingreso"):
    st.write("Modelo de suscripción:")
    st.write("""
    - Plan mensual: $10 USD  
    - Plan trimestral: $25 USD  
    - Plan anual: $90 USD  
    """)
    if st.button("Suscribirse"):
        st.success("Redirigiendo a plataforma de pago...")

with st.expander("Recursos Clave"):
    st.write("""
    - Algoritmos de optimización  
    - Base de datos de perfiles  
    - Plataforma digital  
    """)

with st.expander("Actividades Clave"):
    st.write("""
    - Desarrollo del software  
    - Análisis de datos  
    - Soporte al cliente  
    """)

with st.expander("Socios Clave"):
    st.write("""
    - Caficultores  
    - Empresas de maquinaria  
    - Expertos en café  
    """)

with st.expander("Estructura de Costos"):
    st.write("""
    - Desarrollo tecnológico  
    - Hosting  
    - Marketing  
    - Soporte técnico  
    """)
