import pandas as pd

# Ruta de los archivos
input_file = r'C:\Users\Usuario\OneDrive\Documentos\GitHub\python_scripts\diplomatura_ciencia_de_datos\unidad_mineria_de_datos\v_venta_dia.csv'
output_file = r'C:\Users\Usuario\OneDrive\Documentos\GitHub\python_scripts\diplomatura_ciencia_de_datos\unidad_mineria_de_datos\v_venta_dia_fixed.csv'

# Número esperado de columnas
EXPECTED_COLUMNS = 18

def fix_csv(input_file, output_file, expected_columns):
    try:
        # Leer el archivo como texto para analizar línea por línea
        with open(input_file, 'r', encoding='ISO-8859-1') as file:
            lines = file.readlines()

        # Separar encabezado y contenido
        header = lines[0].strip().split(';')
        fixed_lines = [header]

        # Revisar cada línea
        for i, line in enumerate(lines[1:], start=2):  # Comienza en la línea 2
            columns = line.strip().split(';')

            if len(columns) == expected_columns:
                fixed_lines.append(columns)
            else:
                print(f"Línea {i} con problemas: {columns}")
                # Opción 1: Rellenar con valores vacíos
                if len(columns) < expected_columns:
                    columns.extend([''] * (expected_columns - len(columns)))
                    fixed_lines.append(columns)
                # Opción 2: Truncar si hay columnas extra
                elif len(columns) > expected_columns:
                    fixed_lines.append(columns[:expected_columns])

        # Convertir a DataFrame y guardar
        df = pd.DataFrame(fixed_lines[1:], columns=fixed_lines[0])
        df.to_csv(output_file, index=False, encoding='utf-8', sep=',')
        print(f"Archivo corregido guardado en: {output_file}")

    except Exception as e:
        print(f"Error: {e}")

# Ejecutar la función
fix_csv(input_file, output_file, EXPECTED_COLUMNS)
