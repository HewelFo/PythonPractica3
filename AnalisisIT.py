# problema 6 manejo de pandas hewel.ochoa@utp.ac.pa
import pandas as pd
import matplotlib.pyplot as plt

inf = pd.read_csv('ITUsagePerAge-2020.csv')


# se muestran los datos de la tabla
print(inf)
print(inf.columns)
print(inf.shape)
print("-----------------------------------------------------------")
#obtien los datos de los lugares evaluados y sus fechas
quest2 = inf['Month'].unique()
quest22 = inf['Location '].unique()
print(quest2,quest22)

print("-----------------------------------------------------------")
maximo = inf[:11].max()
print(maximo)