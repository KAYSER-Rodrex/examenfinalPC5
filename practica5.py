#El trabajo esta hecho en jupyer pero por las dudas he importado,
#todos los codigos para que sea mas facil de enviar y abrir desde github

#2-FILTRADO DE DATAFRAMES Y SERIES


import pandas as pd
df_airbnb = pd.read_csv("./src/pandas/airbnb.csv")
df_airbnb
df_airbnb.dtypes

#En concreto el dataset tiene las siguientes variables:
#room_id: el identificador de la propiedad
#host_id: el identificador del dueño de la propiedad
#room_type: tipo de propiedad (vivienda completa/(habitacion para compartir/habitación privada)
#neighborhood: el barrio de Lisboa
#reviews: El numero de opiniones
#overall_satisfaction: Puntuacion media del apartamento
#accommodates: El numero de personas que se pueden alojar en la propiedad
#bedrooms: El número de habitaciones
#price: El precio (en euros) por noche



#CASO 1
import pandas as pd
df_airbnb = pd.read_csv("./src/pandas/airbnb.csv")
df_airbnb.loc[[], ["reviews","overall_satisfaction","accommodates"] ]

#CASO 2
import pandas as pd
df_airbnb = pd.read_csv("./src/pandas/airbnb.csv", header=None)
df_airbnb.iloc[[3,4],[4]]
df_airbnb.to_excel("airbnb1.xlsx", sheet_name='Sheet1')

#CASO 3
import pandas as pd
df_airbnb = pd.read_csv("./src/pandas/airbnb.csv")
df_airbnb.loc[[0,1,2,13229], ["room_type","overall_satisfaction","price"]]

#CASO 4
import matplotlib.pyplot as plt
import pandas as pd
df_airbnb = pd.read_csv("./src/pandas/airbnb.csv")
plt.pie(df_airbnb['room_type'])




# 1-DATAFRAMES Y SERIES EJERCICIOS

#importa pandas

# Crea una Serie de los numeros 10, 20 and 10.
series = pd.Series([10,20,10])
series

# Crea una Serie con tres objetos: 'rojo', 'verde', 'azul'
colores = pd.Series(['rojo','verde','azul'])
colores

# Crea un dataframe vacío llamado 'df'
df = pd.DataFrame()
df

# Crea otra columna en el dataframe y asignale la segunda Serie que has creado
df.assign(colores=lambda x:['rojo','verde','azul'])

# Lee el archivo llamado 'avengers.csv" localizado en la carpeta "data" y crea un DataFrame, llamado 'avengers'. 
# El archivo está localizado en "data/avengers.csv"

df_avengers = pd.read_csv("./src/pandas/avengers.csv")

# Muestra las primeras 5 filas del DataFrame.
df_avengers.head(5)

# Muestra las primeras 10 filas del DataFrame. 
df_avengers.head(10)

# Muestra las últimas 5 filas del DataFrame.

df_avengers.tail(5)

# Muestra el tamaño del DataFrame
df_avengers.size

# Muestra los data types del dataframe
df_avengers = pd.read_csv("./src/pandas/avengers.csv")
df_avengers.dtypes

# Cambia el indice a la columna "fecha_inicio".

df_avengers = df_avengers.rename(columns={'fecha_inicio': 'inicio_fecha'})

# Ordena el índice de forma descendiente
df_avengers.sort_values(by=['URL','nombre'], ascending=[False,True])

# Resetea el índice

df_avengers = df_avengers.reset_index()