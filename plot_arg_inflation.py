import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file
df = pd.read_csv('./data_csv/indice_precios_consumidor_tucuman.csv')

# Extract the two columns
x = df['indice_tiempo']
y = df['nivel_general']

# Create the scatter plot
plt.scatter(x, y)

# Show the plot
plt.show()
