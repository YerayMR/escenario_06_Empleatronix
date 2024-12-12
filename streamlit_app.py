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

# Seleccionar color para las barras
bar_color = st.selectbox('Elige un color para las barras', ['#0099ff', '#ff5733', '#33cc33'])

# Configurar si mostrar el nombre o el sueldo
show_names = st.checkbox('Mostrar el nombre')
show_salary = st.checkbox('Mostrar sueldo en la barra')

# Crear gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))

# Crear las barras con el color seleccionado
ax.barh(df['full name'], df['salary'], color=bar_color)

# Añadir etiquetas de salario o nombre según la selección
if show_salary:
    for i, v in enumerate(df['salary']):
        ax.text(v + 50, i, f'{v}', va='center', ha='left', color='black', fontweight='bold')

if show_names:
    for i, v in enumerate(df['full name']):
        ax.text(-100, i, v, va='center', ha='right', color='black', fontweight='bold')

# Configuración del gráfico
ax.set_xlabel('Sueldo ($)')
ax.set_ylabel('Empleado')

# Mostrar gráfico
st.pyplot(fig)
