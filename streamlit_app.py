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

st.divider()

col1, col2, col3 = st.columns(3)

# Seleccionar color para las barras
with col1:
    bar_color = st.color_picker("Pick A Color", "#6DF7FD")

# Configurar si mostrar el nombre o el sueldo
with col2:
    show_names = st.checkbox('Mostrar el nombre', value=True)
with col3:
    show_salary = st.checkbox('Mostrar sueldo en la barra')

# Crear gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))

# Crear las barras con el color seleccionado
ax.barh(df['full name'], df['salary'], color=bar_color)

# Añadir etiquetas de salario o nombre según la selección
if show_salary:
  for i, v in enumerate(df['salary']):
      ax.text(v + 50, i, f'{v}', va='center', ha='left', color='black', fontweight='bold')

if show_names == False:
  # Si no se selecciona "Mostrar el nombre", ocultamos los nombres del eje Y
  ax.set_yticklabels([''] * len(df))  # Elimina los nombres del eje Y

# Configuración del gráfico
ax.set_xlabel('Sueldo ($)')
ax.set_ylabel('Empleado')

# Mostrar gráfico
st.pyplot(fig)
