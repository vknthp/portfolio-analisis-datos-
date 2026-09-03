# V.P.C.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# DATOS

# Para obtener siempre los mismos resultados
np.random.seed(42)

# Número de estudiantes
sample_size = 200

# Simulación de los datos
data = {
    'age': np.random.randint(18, 46, size=sample_size),

    'gender': np.random.choice(
        ['Femenino', 'Masculino', 'Otro'],
        size=sample_size,
        p=[0.48, 0.48, 0.04]
    ),

    'satisfaction_score': np.random.normal(
        loc=7.3,
        scale=1.2,
        size=sample_size
    ).clip(1, 10).round(1),

    'weekly_study_hours': np.random.normal(
        loc=8,
        scale=2.5,
        size=sample_size
    ).clip(0).round(1)
}

students_df = pd.DataFrame(data)


print("Primeras 5 filas del DataFrame:\n")
print(students_df.head())


# Seleccionamos las variables numéricas
numeric_columns = [
    'age',
    'satisfaction_score',
    'weekly_study_hours'
]


# Estadísticas descriptivas
descriptive_stats = students_df[numeric_columns].agg(
    ['mean', 'median', 'std']
)

print("\nESTADÍSTICAS DESCRIPTIVAS:\n")
print(descriptive_stats)


# Verificación de valores nulos
print("\nVALORES NULOS:\n")
print(students_df.isnull().sum())


# En este DataFrame simulado no existen valores nulos.
# Si existieran, se podría evaluar su cantidad y, dependiendo
# del caso, eliminarlos o reemplazarlos. Por ejemplo, para
# variables numéricas se podría utilizar la mediana y para
# variables categóricas la moda.


# DISTRIBUCIÓN Y VISUALIZACIÓN


plt.hist(
    students_df['satisfaction_score'],
    bins=10,
    edgecolor='black'
)

plt.title("Distribución de Puntajes de Satisfacción")
plt.xlabel("Puntaje de satisfacción")
plt.ylabel("Frecuencia")

plt.show()


# Media utilizando NumPy
satisfaction_mean = np.mean(
    students_df['satisfaction_score']
)

# Varianza utilizando NumPy
satisfaction_variance = np.var(
    students_df['satisfaction_score']
)


print("\nDISTRIBUCIÓN DEL PUNTAJE DE SATISFACCIÓN:")

print(
    f"Media: "
    f"{satisfaction_mean:.3f}"
)

print(
    f"Varianza: "
    f"{satisfaction_variance:.3f}"
)


# El histograma presenta una forma relativamente simétrica
# y similar a una campana, por lo que los puntajes parecen
# aproximarse a una distribución normal.


# INTERVALO DE CONFIANZA DEL 95%


# Desviación estándar muestral
satisfaction_std = students_df[
    'satisfaction_score'
].std()

# Grados de libertad
degrees_freedom = sample_size - 1

# Valor crítico t para un nivel de confianza del 95%
t_critical = stats.t.ppf(
    0.975,
    df=degrees_freedom
)

# Error estándar
standard_error = (
    satisfaction_std / np.sqrt(sample_size)
)

# Margen de error
margin_error = (
    t_critical * standard_error
)

# Límites del intervalo de confianza
lower_limit = (
    satisfaction_mean - margin_error
)

upper_limit = (
    satisfaction_mean + margin_error
)


print("\nINTERVALO DE CONFIANZA DEL 95%:")

print(
    f"({lower_limit:.3f}, "
    f"{upper_limit:.3f})"
)


# Con un nivel de confianza del 95%, se estima que la verdadera
# media de satisfacción de los estudiantes se encuentra dentro
# del intervalo calculado.


# PRUEBA DE HIPÓTESIS


# Hipótesis:
#
# H0: μ = 7
# H1: μ != 7
#
# Se utiliza una prueba t de una muestra con un nivel de
# significancia del 5%.

hypothesized_mean = 7
alpha = 0.05


t_statistic, p_value = stats.ttest_1samp(
    students_df['satisfaction_score'],
    popmean=hypothesized_mean
)


print("\nPRUEBA DE HIPÓTESIS:")

print(
    f"Estadístico t: "
    f"{t_statistic:.4f}"
)

print(
    f"Valor-p: "
    f"{p_value:.6f}"
)


if p_value < alpha:

    print(
        "Se rechaza la hipótesis nula."
    )

    print(
        "Existe evidencia estadística para afirmar que "
        "el puntaje promedio de satisfacción es diferente de 7."
    )

else:

    print(
        "No se rechaza la hipótesis nula."
    )

    print(
        "No existe evidencia estadística suficiente para afirmar "
        "que el puntaje promedio de satisfacción sea diferente de 7."
    )


# En términos prácticos, si se rechaza H0, la empresa puede
# concluir que la satisfacción promedio de sus estudiantes
# difiere significativamente del valor de referencia de 7.


# REFLEXIÓN FINAL


# La estadística inferencial permite extraer y manipular información de una
# muestra para obtener conclusiones sobre una población.
# Herramientas como los intervalos de confianza y las pruebas de
# hipótesis ayudan a cuantificar la incertidumbre y permiten tomar
# decisiones empresariales respaldadas por evidencia.