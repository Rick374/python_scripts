# Importación de bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Bibliotecas para visualizaciones geoespaciales
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Configuración de estilo para gráficos
sns.set(style='whitegrid')

# Ignorar warnings
import warnings
warnings.filterwarnings('ignore')

# Cargar el primer dataset: atom_integrated_columns.csv
atom_data_path = "C:/Users/Usuario/iCloudDrive/Documentos/Diplomatura Ciencia de Datos/Proyecto Final/Base de Datos/ATom_Mapping_OH_Troposphere_1669/ATom_Mapping_OH_Troposphere_1669/data/atom_integrated_columns.csv"
df_atom = pd.read_csv(atom_data_path)

# Cargar el segundo dataset: omi_gridded_hcho_and_xoh.csv
omi_data_path = "C:/Users/Usuario/iCloudDrive/Documentos/Diplomatura Ciencia de Datos/Proyecto Final/Base de Datos/ATom_Mapping_OH_Troposphere_1669/ATom_Mapping_OH_Troposphere_1669/data/omi_gridded_hcho_and_xoh.csv"
df_omi = pd.read_csv(omi_data_path)

# Mostrar las primeras filas del dataset atom
print("Datos de ATom:")
print(df_atom.head())

# Mostrar información general
print("\nInformación del dataset ATom:")
print(df_atom.info())

# Mostrar las primeras filas del dataset omi
print("\nDatos de OMI:")
print(df_omi.head())

# Mostrar información general
print("\nInformación del dataset OMI:")
print(df_omi.info())

# Reemplazar valores faltantes indicados por -999 por NaN en df_atom
df_atom.replace(-999, np.nan, inplace=True)

# Reemplazar valores faltantes en df_omi
df_omi.replace(-999, np.nan, inplace=True)

# Verificar la cantidad de valores faltantes en df_atom
print("\nValores faltantes en df_atom:")
print(df_atom.isnull().sum())

# Verificar la cantidad de valores faltantes en df_omi
print("\nValores faltantes en df_omi:")
print(df_omi.isnull().sum())

# Eliminar filas con valores faltantes críticos si es necesario
df_atom_clean = df_atom.dropna(subset=['hcho', 'oh', 'lat_mid', 'lon_mid'])
df_omi_clean = df_omi.dropna(subset=['hcho_omi_atom1', 'xoh_atom1', 'lat', 'lon'])

# Convertir 'date' a datetime en df_atom
df_atom_clean['date'] = pd.to_datetime(df_atom_clean['date'], format='%Y%m%d')

# Añadir columna de año y mes para análisis temporal
df_atom_clean['year'] = df_atom_clean['date'].dt.year
df_atom_clean['month'] = df_atom_clean['date'].dt.month

# Estadísticas descriptivas para variables clave en df_atom
print("\nEstadísticas descriptivas de df_atom:")
print(df_atom_clean[['hcho', 'oh', 'p_oh']].describe())

# Estadísticas descriptivas para variables clave en df_omi
print("\nEstadísticas descriptivas de df_omi:")
print(df_omi_clean[['hcho_omi_atom1', 'xoh_atom1']].describe())

# # Histograma de hcho en df_atom
# plt.figure(figsize=(10,5))
# sns.histplot(df_atom_clean['hcho'], bins=30, kde=True)
# plt.title('Distribución de HCHO en ATom')
# plt.xlabel('HCHO (cm⁻²)')
# plt.ylabel('Frecuencia')
# plt.show()

# # Histograma de oh en df_atom
# plt.figure(figsize=(10,5))
# sns.histplot(df_atom_clean['oh'], bins=30, kde=True, color='orange')
# plt.title('Distribución de OH en ATom')
# plt.xlabel('OH (cm⁻²)')
# plt.ylabel('Frecuencia')
# plt.show()

# # Histograma de hcho_omi_atom1 en df_omi
# plt.figure(figsize=(10,5))
# sns.histplot(df_omi_clean['hcho_omi_atom1'], bins=30, kde=True, color='green')
# plt.title('Distribución de HCHO OMI - ATom 1')
# plt.xlabel('HCHO OMI (cm⁻²)')
# plt.ylabel('Frecuencia')
# plt.show()

# Visualización de los perfiles de ATom con concentraciones de HCHO
# plt.figure(figsize=(12,6))
# ax = plt.axes(projection=ccrs.PlateCarree())
# scatter = ax.scatter(df_atom_clean['lon_mid'], df_atom_clean['lat_mid'], c=df_atom_clean['hcho'], cmap='viridis', transform=ccrs.PlateCarree())
# ax.coastlines()
# ax.set_title('Perfiles de ATom - Concentración de HCHO')
# cbar = plt.colorbar(scatter, ax=ax, orientation='vertical', label='HCHO (cm⁻²)')
# plt.show()

# # Visualización de HCHO OMI - ATom 1
# plt.figure(figsize=(12,6))
# ax = plt.axes(projection=ccrs.PlateCarree())
# scatter = ax.scatter(df_omi_clean['lon'], df_omi_clean['lat'], c=df_omi_clean['hcho_omi_atom1'], cmap='plasma', transform=ccrs.PlateCarree())
# ax.coastlines()
# ax.set_title('OMI HCHO Column Density - ATom 1')
# cbar = plt.colorbar(scatter, ax=ax, orientation='vertical', label='HCHO OMI (cm⁻²)')
# plt.show()

# Serie temporal de promedio diario de hcho en df_atom
# df_atom_daily = df_atom_clean.groupby('date')['hcho'].mean().reset_index()

# plt.figure(figsize=(12,5))
# plt.plot(df_atom_daily['date'], df_atom_daily['hcho'], marker='o', linestyle='-')
# plt.title('Promedio Diario de HCHO en ATom')
# plt.xlabel('Fecha')
# plt.ylabel('HCHO (cm⁻²)')
# plt.grid(True)
# plt.show()

# # Matriz de correlación en df_atom
# corr_atom = df_atom_clean[['hcho', 'oh', 'p_oh', 'k_hcho', 'j_hcho']].corr()
# print("\nMatriz de correlación en df_atom:")
# print(corr_atom)

# plt.figure(figsize=(8,6))
# sns.heatmap(corr_atom, annot=True, cmap='coolwarm')
# plt.title('Matriz de Correlación - ATom')
# plt.show()

# Histograma comparativo de hcho_omi_atom1 y hcho_omi_atom2
# plt.figure(figsize=(10,5))
# sns.histplot(df_omi_clean['hcho_omi_atom1'], color='blue', label='ATom 1', kde=True)
# sns.histplot(df_omi_clean['hcho_omi_atom2'], color='red', label='ATom 2', kde=True)
# plt.title('Comparación de HCHO OMI - ATom 1 vs ATom 2')
# plt.xlabel('HCHO OMI (cm⁻²)')
# plt.legend()
# plt.show()

# Definir las resoluciones de la grilla de OMI
lat_resolution = 0.5
lon_resolution = 0.625

# Crear bins para latitud y longitud en df_atom_clean
df_atom_clean['lat_bin'] = ((df_atom_clean['lat_mid'] / lat_resolution).round(0)) * lat_resolution
df_atom_clean['lon_bin'] = ((df_atom_clean['lon_mid'] / lon_resolution).round(0)) * lon_resolution

# Asegurarnos de que las coordenadas estén dentro del rango adecuado (-90 a 90 para latitud, -180 a 180 para longitud)
df_atom_clean['lat_bin'] = df_atom_clean['lat_bin'].clip(-90, 90)
df_atom_clean['lon_bin'] = df_atom_clean['lon_bin'].clip(-180, 180)

# En df_omi_clean, las columnas 'lat' y 'lon' ya representan el centro de los grids
df_omi_clean['lat_bin'] = df_omi_clean['lat']
df_omi_clean['lon_bin'] = df_omi_clean['lon']

# Realizar la unión basada en 'lat_bin' y 'lon_bin'
df_combined = pd.merge(df_atom_clean, df_omi_clean, on=['lat_bin', 'lon_bin'], how='left')

# Verificar cuántas filas tienen valores no nulos en las columnas de interés
df_model = df_combined[['hcho', 'oh', 'p_oh', 'k_hcho', 'j_hcho', 'hcho_omi_atom1', 'xoh_atom1', 'tp_height_atom1', 'air_mass_atom1']]
print("Cantidad de filas antes de dropna:", df_model.shape[0])
print("Cantidad de filas con valores completos:", df_model.dropna().shape[0])

# Continuar con el procesamiento si hay suficientes datos
df_model_clean = df_model.dropna()

# Si hay datos, proceder con el modelado
if not df_model_clean.empty:
    # ... (resto del código)
    # División en entrenamiento y prueba
    X = df_model_clean[['hcho', 'p_oh', 'k_hcho', 'j_hcho', 'hcho_omi_atom1', 'tp_height_atom1', 'air_mass_atom1']]
    y = df_model_clean['oh']

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Continuar con el modelado
    # ...
else:
    print("No hay suficientes datos para el modelado después de eliminar valores faltantes.")

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Crear el modelo
model_lr = LinearRegression()

# Entrenar el modelo
model_lr.fit(X_train, y_train)

# Predicciones en el conjunto de prueba
y_pred = model_lr.predict(X_test)

# Evaluación del modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nResultados de la Regresión Lineal:")
print(f"MSE: {mse}")
print(f"R²: {r2}")

# Gráfico de predicciones vs valores reales
# plt.figure(figsize=(8,6))
# plt.scatter(y_test, y_pred, alpha=0.7)
# plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
# plt.title('Regresión Lineal - Predicciones vs Valores Reales')
# plt.xlabel('Valores Reales de OH')
# plt.ylabel('Predicciones de OH')
# plt.grid(True)
# plt.show()

from sklearn.ensemble import RandomForestRegressor

model_rf = RandomForestRegressor(n_estimators=100, random_state=42)

# Entrenar el modelo
model_rf.fit(X_train, y_train)

# Predicciones y evaluación
y_pred = model_rf.predict(X_test)
mse_rf = mean_squared_error(y_test, y_pred)
r2_rf = r2_score(y_test, y_pred)

print("Resultados de Random Forest:")
print(f"MSE: {mse_rf}")
print(f"R²: {r2_rf}")

# Gráfico de predicciones vs valores reales
plt.figure(figsize=(8,6))
plt.scatter(y_test, y_pred, alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.title('Random Forest - Predicciones vs Valores Reales')
plt.xlabel('Valores Reales de OH')
plt.ylabel('Predicciones de OH')
plt.grid(True)
plt.show()
