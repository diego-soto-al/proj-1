import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos ya procesados
df = pd.read_csv("data/nox.csv", sep='\t')

# Combinar Date.Local y Time.Local en una sola columna datetime
df["Datetime"] = pd.to_datetime(df["Date.Local"] + " " + df["Time.Local"], errors="coerce")

# Ordenar por tiempo
df = df.sort_values("Datetime")

# Graficar
plt.figure(figsize=(12,6))
plt.plot(df["Datetime"], df["Sample.Measurement"], linewidth=0.5, color="blue")
plt.title("TS-NOX-202")
plt.xlabel("Datetime")
plt.ylabel("Sample.Measurement")
plt.tight_layout()

# Guardar gráfico
plt.savefig("data/TS-NOX-202.png", dpi=150)
plt.close()