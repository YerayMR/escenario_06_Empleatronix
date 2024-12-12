import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv('src/employees.csv')

# Configuración de Streamlit
st.title('EMPLEATRONIX')
st.write('Todos los datos sobre los empleados en una aplicación.')

# Mostrar la tabla de empleados
st.dataframe(df)

# Opción para elegir color de las barras
bar_color = st.selectbox('Elige un color para las barras', ['#0099ff', '#ff5733', '#33cc33'])

# Mostrar nombres y salarios en las barras
show_names = st.checkbox('Mostrar el nombre')
show_salary = st.checkbox('Mostrar sueldo en la barra')

# Crear gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))

# Crear las barras
bars = ax.barh(df['full name'], df['salary'], color=bar_color)

# Mostrar nombres o sueldos según la selección
if show_names:
    for bar in bars:
        ax.text(bar.get_width() - 100, bar.get_y() + bar.get_height()/2,
                f'{bar.get_width():,.0f}', va='center', ha='right', color='white', fontweight='bold')

if show_salary:
    for bar in bars:
        ax.text(bar.get_width() + 100, bar.get_y() + bar.get_height()/2,
                f'{bar.get_width():,.0f}', va='center', ha='left', color='black', fontweight='bold')

# Configuración del gráfico
ax.set_xlabel('Sueldo ($)')
ax.set_ylabel('Empleado')

# Mostrar el gráfico
st.pyplot(fig)
