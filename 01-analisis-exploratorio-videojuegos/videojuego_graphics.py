# V.P.C. #

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data #
df = pd.read_csv("Videojuegos.csv")


# 1. Grafico de pares #
numeric_variables = [
    "Ventas_NA",
    "Ventas_EU",
    "Ventas_JP",
    "Critica_Puntaje"
]

sns.pairplot(
    data=df,
    vars=numeric_variables,
    hue="Plataforma"
)

plt.show()

# 2. Grafico de violín #

plt.figure(figsize=(10, 6))

sns.violinplot(
    data=df,
    x="Plataforma",
    y="Critica_Puntaje",
    hue="Plataforma",
    palette="Set2",
    legend=False
)

plt.title("Distribución del Puntaje de Crítica por Plataforma")
plt.xlabel("Plataforma")
plt.ylabel("Puntaje de Crítica")
plt.tight_layout()
plt.show()

# 3. Mapa de calor #

correlation_matrix = df[numeric_variables].corr()

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    vmin=-1,
    vmax=1
)

plt.title("Matriz de Correlación de Variables Numéricas")
plt.tight_layout()
plt.show()



# 4. CALCULAR LAS VENTAS GLOBALES #

df["Ventas_Globales"] = (
    df["Ventas_NA"]
    + df["Ventas_EU"]
    + df["Ventas_JP"]
)

per_genere = (
    df.groupby("Genero")["Ventas_Globales"]
    .mean()
    .sort_values(ascending=False)
)


# 5 Y 6. #

fig, ax = plt.subplots(figsize=(12, 7))

bars = ax.bar(
    per_genere.index,
    per_genere.values,
    color="steelblue",
    edgecolor="black"
)

ax.set_title(
    "Promedio de Ventas Globales por Género de Videojuego",
    fontsize=15
)

ax.set_xlabel("Género")
ax.set_ylabel("Promedio de Ventas Globales")


maximum = per_genere.max()
ax.set_ylim(0, maximum * 1.30)


ax.bar_label(
    bars,
    labels=[f"{val:.2f}" for val in per_genere.values],
    padding=3
)

plt.xticks(rotation=45, ha="right")

plt.tight_layout()


plt.savefig(
    "ventas_por_genero_personalizado.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()