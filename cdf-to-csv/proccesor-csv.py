import pandas as pd
import os
from matplotlib import dates as mdates
import seaborn as sns
import matplotlib.pyplot as plt

exten_archivo = ".cdf"
ruta_maestra = str(os.getcwd()) + "/"            # Executable relative route

ruta_archivo_csv_DSCVR = ruta_maestra + "datos_csv_DSCVR/"

ruta_archivo_csv_WIND = ruta_maestra + "datos_csv_WIND/"

df_DSCVR_csv = pd.read_csv(os.path.join(ruta_archivo_csv_DSCVR, "DSCVR.csv"))

df_WIND_csv = pd.read_csv(os.path.join(ruta_archivo_csv_WIND, "WIND.csv"))

print("*"*100)
print("Uniendo dataframes")

df_union = pd.merge(
    df_DSCVR_csv,
    df_WIND_csv,
    how = "outer",
    on = ["tiempo", "campo_mag_X"],
    left_on = None,
    right_on = None,
    left_index = False,
    right_index = False,
    sort = True,
    suffixes=("_DSCVR", "_WIND"),
    copy = True,
    indicator = False,
    validate = "one_to_one",
)

# Saving dataframe in CSV.
print("Guardando la union de los dataframes en CSV")
df_union.to_csv(os.path.join("union_DSCVR_WIND.csv"), index = False, header = True)

# ---------------------------------------------------------------------------------
# Graphics data
# ---------------------------------------------------------------------------------
"""
print("*"*100)
print("Graficando")

plt.rcParams['figure.figsize'] = [21, 7]        #Tamaño (en pulgadas)
sns.set_theme(style="whitegrid")

plt.plot(df_union["tiempo"], df_union["campo_mag_X"], linewidth=1, label='Campo_Magnetico_X')

sns.set_palette("tab10")                    # https://seaborn.pydata.org/tutorial/color_palettes.html 
    
plt.show()
"""
print("*"*100)
print("Programa finalizado")
print("*"*100)