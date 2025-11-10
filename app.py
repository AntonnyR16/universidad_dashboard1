import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(page_title="University Dashboard", layout="wide")

# Cargar datos
@st.cache_data
def load_data():
    df = pd.read_csv('university_student_data.csv')
    return df

df = load_data()

# Título del dashboard
st.title("University Student Data Dashboard")

# Filtros en la barra lateral
st.sidebar.header("Filtros")
years = st.sidebar.multiselect("Seleccionar Año", sorted(df['Year'].unique()), default=sorted(df['Year'].unique()))
terms = st.sidebar.multiselect("Seleccionar Periodo (Term)", sorted(df['Term'].unique()), default=sorted(df['Term'].unique()))

# Filtrar datos según selección
filtered = df[(df['Year'].isin(years)) & (df['Term'].isin(terms))]

# Métricas clave
col1, col2 = st.columns(2)
col1.metric("Retención Promedio (%)", f"{filtered['Retention Rate (%)'].mean():.2f}")
col2.metric("Satisfacción Promedio (%)", f"{filtered['Student Satisfaction (%)'].mean():.2f}")

# Gráfico 1: Tasa de retención por año
st.subheader("Tasa de Retención por Año")
fig1, ax1 = plt.subplots()
sns.lineplot(data=filtered, x='Year', y='Retention Rate (%)', marker='o', ax=ax1)
ax1.set_ylabel("Retención (%)")
st.pyplot(fig1)

# Gráfico 2: Satisfacción estudiantil por año
st.subheader("Satisfacción Estudiantil por Año")
fig2, ax2 = plt.subplots()
sns.barplot(data=filtered, x='Year', y='Student Satisfaction (%)', ax=ax2)
ax2.set_ylabel("Satisfacción (%)")
st.pyplot(fig2)

# Gráfico 3: Comparación entre Spring y Fall
st.subheader(" Comparación de Satisfacción entre Spring y Fall")
fig3, ax3 = plt.subplots()
sns.boxplot(data=filtered, x='Term', y='Student Satisfaction (%)', ax=ax3)
ax3.set_ylabel("Satisfacción (%)")
st.pyplot(fig3)

# Pie de página
st.markdown("---")
st.markdown(" *Dashboard interactivo creado con Streamlit Cloud*")
