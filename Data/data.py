import pandas as pd

# Importar datos del csv
data_teorico = pd.read_csv(r"C:\Users\david\OneDrive - Universidad Distrital Francisco José de Caldas\Semestre 7\Programación II\5. Clase\Actividad 4\Data\Data ingeniero.csv")

#Código general
""" En caso que se exigiera realizar la limpieza de la data se haría aca"""


#Esta función toma el conjunto de datos llamado "data_teorico" y extrae las columnas de nombre "'Esfuerzo[kN]' y 'Deformacion[mm]'"
#Posteriormente estos valores son devueltos como una tupla
#Son una estructura de datos en Python que se utilizan para almacenar un conjunto ordenado de datos, son similares a una lista
#con la diferencia de que las tuplas no se pueden modificar
def dataTeorico():
    dataTeoricoEsfuerzo = data_teorico['Esfuerzo[kN]']
    dataTeoricoDeformacion = data_teorico['Deformacion[mm]']
    return dataTeoricoEsfuerzo, dataTeoricoDeformacion
