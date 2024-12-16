import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor

# Cargar los datos de Estados Unidos
df_us = pd.read_csv("C:\\Users\\Usuario\\iCloudDrive\\Documentos\\Diplomatura Ciencia de Datos\\Proyecto Final\\Base de Datos\\openaq_location_384_measurments.csv")

# Cargar los datos de Brasil
df_brazil = pd.read_csv("C:\\Users\\Usuario\\iCloudDrive\\Documentos\\Diplomatura Ciencia de Datos\\Proyecto Final\\Base de Datos\\openaq_location_820326_measurments.csv")

# Cargar los datos de Chile
df_chile = pd.read_csv("C:\\Users\\Usuario\\iCloudDrive\\Documentos\\Diplomatura Ciencia de Datos\\Proyecto Final\\Base de Datos\\openaq_location_25_measurments.csv")

# # Redondear los valores decimales a valores enteros
# df_us['value'] = df_us['value'].round().astype(int)
# df_brazil['value'] = df_brazil['value'].round().astype(int)
# df_chile['value'] = df_chile['value'].round().astype(int)

# # Guardar los DataFrames redondeados en nuevos archivos CSV
# df_us.to_csv("C:\\Users\\Usuario\\iCloudDrive\\Documentos\\Diplomatura Ciencia de Datos\\Proyecto Final\\Base de Datos\\openaq_location_384_measurments_rounded.csv", index=False)
# df_brazil.to_csv("C:\\Users\\Usuario\\iCloudDrive\\Documentos\\Diplomatura Ciencia de Datos\\Proyecto Final\\Base de Datos\\openaq_location_820326_measurments_rounded.csv", index=False)
# df_chile.to_csv("C:\\Users\\Usuario\\iCloudDrive\\Documentos\\Diplomatura Ciencia de Datos\\Proyecto Final\\Base de Datos\\openaq_location_25_measurments_rounded.csv", index=False)

# Añadir una columna para identificar el país
df_us['country'] = 'USA'
df_brazil['country'] = 'Brazil'
df_chile['country'] = 'Chile'

# Concatenar los DataFrames
df_all = pd.concat([df_us, df_brazil, df_chile], ignore_index=True)

# Verificar valores faltantes por columna antes de eliminar
print("Valores faltantes por columna antes de eliminar:")
print(df_all.isnull().sum())

# Eliminar las columnas que contienen valores faltantes
df_all = df_all.dropna(axis=1, how='any')

# Verificar que las columnas faltantes hayan sido eliminadas
print("Valores faltantes por columna después de eliminar:")
print(df_all.isnull().sum())

# Mostrar las primeras filas del DataFrame resultante
print(df_all.head())

# Convertir Fechas a Formato Datetime con utc=True
df_all['datetimeUtc'] = pd.to_datetime(df_all['datetimeUtc'], errors='coerce', utc=True)
df_all['datetimeLocal'] = pd.to_datetime(df_all['datetimeLocal'], errors='coerce', utc=True)

# Asegurarse de que no hay errores en la conversión
print(df_all[['datetimeLocal']].dtypes)

# Análisis Exploratorio de Datos (EDA)

# 1. Distribución de Mediciones por País y Parámetro
print("Conteo por país y parámetro:")
print(df_all.groupby(['country', 'parameter']).size())

# 2. Visualización de la Distribución de Valores
df_pm = df_all[df_all['parameter'].isin(['pm10', 'pm25'])].copy()

plt.figure(figsize=(10,6))
sns.histplot(data=df_pm, x='value', hue='country', bins=30, kde=True)
plt.title('Distribución de PM10 y PM2.5 por País')
plt.xlabel('Concentración')
plt.ylabel('Frecuencia')
plt.show()

# 3. Series Temporales
df_pm['datetimeLocal'] = pd.to_datetime(df_pm['datetimeLocal'], errors='coerce', utc=True)
df_pm.loc[:, 'date'] = df_pm['datetimeLocal'].dt.date
df_pm_daily = df_pm.groupby(['country', 'date', 'parameter'])['value'].mean().reset_index()

plt.figure(figsize=(12,6))
sns.lineplot(data=df_pm_daily, x='date', y='value', hue='country', style='parameter')
plt.title('Concentración Diaria Promedio de PM10 y PM2.5')
plt.xlabel('Fecha')
plt.ylabel('Concentración')
plt.legend(title='País y Parámetro')
plt.show()

# 4. Boxplots por País y Contaminante
plt.figure(figsize=(10,6))
sns.boxplot(data=df_pm, x='parameter', y='value', hue='country')
plt.title('Distribución de PM10 y PM2.5 por País')
plt.xlabel('Parámetro')
plt.ylabel('Concentración')
plt.show()

# 5. Mapas Geográficos
m = folium.Map(location=[-15, -60], zoom_start=3)

for index, row in df_all.iterrows():
    folium.CircleMarker(location=[row['latitude'], row['longitude']],
                        radius=3,
                        popup=f"{row['location_name']} ({row['country']})",
                        color='blue',
                        fill=True,
                        fill_color='blue').add_to(m)

m.save('mapa_mediciones.html')

# 6. Promedio por Hora del Día
df_all['hour'] = df_all['datetimeLocal'].dt.hour
df_all['day_of_week'] = df_all['datetimeLocal'].dt.day_name()

df_hourly = df_all.groupby(['country', 'hour', 'parameter'])['value'].mean().reset_index()

plt.figure(figsize=(12,6))
sns.lineplot(data=df_hourly[df_hourly['parameter']=='pm25'], x='hour', y='value', hue='country')
plt.title('Promedio Horario de PM2.5')
plt.xlabel('Hora del Día')
plt.ylabel('Concentración Promedio')
plt.show()
