import matplotlib.pyplot as plt
import numpy as np


#Este código define la función "gr_con_predicción"
#la cual toma los datos teóricos y reales de esfuerzo y deformación y crea un gráfico de dispersión en matplotlib
#que muestra como se comparan los datos, los datos teórios se representan con una línea 
#y los reales con puntos rojos.

def gr_con_prediccion(x_lim,y_lim,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion):

    plt.figure(figsize=(15, 6))
    plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion)
    plt.scatter(	dataRealEsfuerzo, dataRealDeformacion, color='red')
    plt.xlabel('Esfuerzo [kN]')
    plt.ylabel('Deformación [mm]')
    plt.title('Gráfica 2: teórico versus real [ZOOM]')
    plt.xlim(0, x_lim)
    plt.ylim(0, y_lim)
    plt.grid()
    plt.gca().invert_yaxis()
    plt.show()


#Este código define la función "gr_con_predicción_3000"
#la cual toma los datos teóricos y reales de esfuerzo y deformación y crea un gráfico de dispersión
#tal y como en el código anterior, con la diferencia de que luego de en este punto se traza una línea magenta
# que representa un modelo de predicción en el rango de esfuerzo de 0 a 1000 kN
# luego, se coloca un punto verde en el gráfico en la coordenada (3000, 'prediction') donde 
# 'prediction' es el valor de la predicción para una carga de 3000 kN, esto representa la predicción del 
# modelo para una carga de 3000 kN 

def gr_con_prediccion_3000(prediction,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion,model):
  plt.figure(figsize=(15, 6))
  plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion)
  plt.scatter(	dataRealEsfuerzo , dataRealDeformacion, color='red')
  plt.plot(np.linspace(0,1000).reshape(-1,1),model.predict(np.linspace(0,1000).reshape(-1,1)),'m')
  plt.scatter(	3000 , prediction, color='green')
  plt.xlabel('Esfuerzo [kN]')
  plt.ylabel('Deformación [mm]')
  plt.title('Gráfica 3: Predicción a una carga de 3000 kN')
  plt.xlim(0, 3000)
  plt.ylim(0, 45)
  plt.grid()
  plt.gca().invert_yaxis()
  plt.show()


#En este código se utiliza la función "gr_sin_prediccion" es una gráfica que compara los datos teóricos y reales
# de esfuerzo y deformación, con la diferencia de que este código muestra todos los datos disponibles en 
# la gráfica sin ningún zoom, a diferencia del código de la función "gr_con_prediccion"

def gr_sin_prediccion(dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion):
  plt.figure(figsize=(15, 6))
  plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion)
  plt.scatter(	dataRealEsfuerzo , dataRealDeformacion, color='red')
  plt.xlabel('Esfuerzo [kN]')
  plt.ylabel('Deformación [mm]')
  plt.title('Gráfica 1: teórico versus real')
  plt.grid()
  plt.gca().invert_yaxis()
  plt.show()