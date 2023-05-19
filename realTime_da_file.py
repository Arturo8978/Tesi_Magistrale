import csv
import numpy
import matplotlib.pyplot as plt
from drawnow import *


"""Creazione variabili(liste, ecc. ) """
tempC= []
pressure=[]
filename = "C:/Users/masto/OneDrive/Desktop/test_python.txt"

plt.ion()                                                   #Comando per il grafico in tempo reale
cnt=0

"""Grafico"""
def makeFig():                                          #Definizione della funzione ""makeFig()"" per la costruzione del grafico
    #plt.ylim(80,90)                                 #Set y min and max values
    plt.title('My Live Streaming Sensor Data')      #Titolo
    plt.grid(True)                                                      #Attiva la griglia
    plt.ylabel('Temp C')                                            #Inserisce il label all'asseY
    plt.subplot(2,1,1)
    plt.plot(tempC, 'ro-', label='Degrees C')       #grafica sull'asseY la temperatura
    plt.legend(loc='upper left')                            #grafica la legenda
     #plt.ylim(93450,93525)
    plt.subplot(2,1,2)
    plt.plot(pressure, 'b^-', label='Pressure (Pa)') #grafica la pressione sul secondo asseY
    plt.ylabel('Pressrue (Pa)')                                     #Inserisce il label sul secondo asseY
    plt.ticklabel_format(useOffset=False)                   #Force matplotlib to NOT autoscale y axis
    plt.legend(loc='upper left')                                    #plot the legend


"""Acquisizione"""
with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # skip header row
    for row in csvreader:
        temp = float(row[1])
        P = float(row[0])
        tempC.append(temp)
        pressure.append(P)
        drawnow(makeFig)
        plt.pause(.000001 )
        cnt=cnt+1
        if(cnt>50):
            tempC.pop(0)
            pressure.pop(0)
