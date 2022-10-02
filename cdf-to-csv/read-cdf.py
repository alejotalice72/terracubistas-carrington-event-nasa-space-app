import os
from spacepy import pycdf
import pandas as pd

exten_archivo = ".cdf"
ruta_maestra = str(os.getcwd()) + "/"            # Executable relative route

ruta_archivo_cdf_DSCVR = ruta_maestra + "datos_cdf_DSCVR/" 
ruta_archivo_csv_DSCVR = ruta_maestra + "datos_csv_DSCVR/"
ruta_archivo_xlsx_DSCVR = ruta_maestra + "datos_xlsx_DSCVR/"

ruta_archivo_cdf_WIND = ruta_maestra + "datos_cdf_WIND/" 
ruta_archivo_csv_WIND = ruta_maestra + "datos_csv_WIND/"
ruta_archivo_xlsx_WIND = ruta_maestra + "datos_xlsx_WIND/"

print("*" * 100)

if not os.path.isdir(ruta_archivo_csv_DSCVR):                   
    print("Creando Carpeta")
    os.mkdir("datos_csv_DSCVR")

elif not os.path.isdir(ruta_archivo_csv_WIND):
    print("Creando Carpeta")
    os.mkdir("datos_csv_WIND")

else:
    pass

print("*" * 100)

# ---------------------------------------------------------------------------------
# Recupera los datos requeridos de los CDF de DSCVR y genera el dataframe
# ---------------------------------------------------------------------------------

#print(cdf_DSCVR["B1GSE"].attrs)

with os.scandir(ruta_archivo_cdf_DSCVR) as files:
    lista__cdf_DSCVR = [file.name for file in files if file.is_file() and file.name.endswith(exten_archivo)]

print("*" * 100)
print("Se procesaran " + str(len(lista__cdf_DSCVR)) + " CDFs.")
print("Los nombres de los CDFs a procesar son:")
for file in lista__cdf_DSCVR:
    print(file)

tiempo_DSCRV = []
valor_DSCRV_X = []
valor_DSCRV_Y = []
valor_DSCRV_Z = []
n_DSCRV = 86400

print("Tomando datos de DSCRV")

for file in lista__cdf_DSCVR:
    print("Procesando : " + file)
    file_path = os.path.join(ruta_archivo_cdf_DSCVR, file)
    cdf_DSCVR = pycdf.CDF(file_path)

    for fila in range(n_DSCRV):
        tiempo = cdf_DSCVR["Epoch1"][fila]
        campo_mag_X = cdf_DSCVR["B1GSE"][fila][0]
        #campo_mag_Y = cdf_DSCVR["B1GSE"][fila][1]
        #campo_mag_Z = cdf_DSCVR["B1GSE"][fila][2]
        tiempo_DSCRV.append(tiempo)
        valor_DSCRV_X.append(campo_mag_X)
        #valor_DSCRV_Y.append(campo_mag_Y)
        #valor_DSCRV_Z.append(campo_mag_Z)

    cdf_DSCVR.close()

lista_DSCRV = {"tiempo" : tiempo_DSCRV, "campo_mag_X" : valor_DSCRV_X}
df_DSCRV = pd.DataFrame(data = lista_DSCRV)

# Save dataframe in CSV.
print("Guardando datos de DSCRV")
df_DSCRV.to_csv(os.path.join(ruta_archivo_csv_DSCVR, "DSCVR.csv"), index = False, header = True)

print("*" * 100)
# ---------------------------------------------------------------------------------
# Recupera los datos requeridos de los CDF de WIND y genera el dataframe
# ---------------------------------------------------------------------------------

with os.scandir(ruta_archivo_cdf_WIND) as files:
    lista__cdf_WIND = [file.name for file in files if file.is_file() and file.name.endswith(exten_archivo)]

print("*" * 100)
print("Se procesaron " + str(len(lista__cdf_WIND)) + " CDFs.")
print("Los nombres de los CDFs procesados son:")
for file in lista__cdf_WIND:
    print(file)

tiempo_WIND = []
valor_WIND_X = []
valor_WIND_Y = []
valor_WIND_Z = []
n_WIND = 925803

print("Tomando datos de WIND")

for file in lista__cdf_WIND:
    print("Procesando : " + file)
    file_path = os.path.join(ruta_archivo_cdf_WIND, file)
    cdf_WIND = pycdf.CDF(file_path)

    for fila in range(n_WIND):
        tiempo = cdf_WIND["Epoch"][fila][0]
        campo_mag_X = cdf_WIND["BGSE"][fila][0]
        #campo_mag_Y = cdf_WIND["BGSE"][fila][1]
        #campo_mag_Z = cdf_WIND["BGSE"][fila][2]
        tiempo_WIND.append(tiempo)
        valor_WIND_X.append(campo_mag_X)
        #valor_WIND_Y.append(campo_mag_Y)
        #valor_WIND_Z.append(campo_mag_Z)

    cdf_WIND.close()

lista_WIND = {"tiempo" : tiempo_WIND, "campo_mag_X" : valor_WIND_X}
df_WIND = pd.DataFrame(data = lista_WIND)

# Save dataframe in CSV.
print("Guardando datos de WIND en CSV")
df_WIND.to_csv(os.path.join(ruta_archivo_csv_WIND, "WIND.csv"), index = False, header = True)

print("*"*100)
print("Programa finalizado")
print("*"*100)