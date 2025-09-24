import pandas as pd

# Archivos
input_file = "data/NOX-2020-ext.csv"
nox_file = "data/nox.csv"
nox_full_file = "data/NOX-2020.csv"
counties_file = "data/counties.csv"
states_file = "data/states.csv"
methods_file = "data/methods.csv"
resumen_file = "data/resumen.txt"

# Columnas
cols_nox = [
    "State.Code", "County.Code", "Site.Num", "Latitude", "Longitude",
    "Date.Local", "Time.Local", "Sample.Measurement", "Method.Type",
    "Method.Code"
]
cols_nox_simple = ["Date.Local", "Time.Local", "Sample.Measurement"]

# Cargar CSV completo
df = pd.read_csv(input_file, sep='\t')

# Guardar NOX-2020.csv (todas las columnas relevantes)
df[cols_nox].to_csv(nox_full_file, sep='\t', index=False)

# Guardar nox.csv (solo 3 columnas)
df[cols_nox_simple].to_csv(nox_file, sep='\t', index=False)

# counties.csv
counties = df[["State.Code", "County.Code", "County.Name"]].drop_duplicates()
counties.to_csv(counties_file, sep='\t', index=False)

# states.csv
states = df[["State.Code", "State.Name"]].drop_duplicates()
states.to_csv(states_file, sep='\t', index=False)

# methods.csv
methods = df[["Method.Code", "Method.Name"]].drop_duplicates()
methods.to_csv(methods_file, sep='\t', index=False)

# Generar resumen
total_states = len(states)
total_counties = len(counties)
total_methods = len(methods)
total_records = len(df)

with open(resumen_file, "w") as f:
    f.write(f"Estados: {total_states}\n")
    f.write(f"Condados: {total_counties}\n")
    f.write(f"Métodos: {total_methods}\n")
    f.write(f"Registros: {total_records}\n")
