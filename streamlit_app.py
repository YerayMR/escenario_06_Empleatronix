import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos de empleados
df = pd.read_csv('src/employees.csv')

# Título de la aplicación
st.title('EMPLEATRONIX')
st.write('Datos sobre los empleados.')

# Mostrar tabla
st.dataframe(df)

# Crear gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))

# Color para las barras y mostrar nombres
bar_color = '#0099ff'  # Color predeterminado
ax.barh(df['full name'], df['salary'], color=bar_color)

# Añadir etiquetas de salario
for i, v in enumerate(df['salary']):
    ax.text(v + 50, i, f'{v}', va='center', ha='left', color='black', fontweight='bold')

# Configuración del gráfico
ax.set_xlabel('Sueldo ($)')
ax.set_ylabel('Empleado')

# Mostrar gráfico
st.pyplot(fig)
