"""Importazione delle librerie utili"""
import serial                   
import numpy  
import matplotlib.pyplot as plt 
from drawnow import *


"""Creazione variabili(liste, ecc. ) """
tempC= []
pressure=[]
arduinoData = serial.Serial('COM7', 9600)

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
while True: 
    while (arduinoData.inWaiting()==0): #Aspetta fino a quando ci sono i dati
        pass #non fare niente
    arduinoString = arduinoData.readline() #leggi la linea di testo dalla porta seriale
    arduinoString = arduinoString.decode().strip()  # converte in una stringa di testo e rimuove i caratteri di spazio bianco
    dataArray = arduinoString.split(',')   #Dividi i dati in un array
    temp = float( dataArray[1])            #Converti il primo dato in variabile float e mettilo in temp
    P = float( dataArray[0])            #Converti il secondo dato in variabile float e mettilo in P
    tempC.append(temp)                     #Costruisci il vettore tempC aggiungendo i valori della variabile temp
    pressure.append(P)                     #Costruisci il vettore pressure aggiungendo i valori della variabile pressure 
    drawnow(makeFig)                       #Chiama la funzione drawnow per caricare il grafico in tempo reale
    plt.pause(.000001 )              #Breve pausa. Importante per evitare il crash della funzione drawnow
    cnt=cnt+1                                #Aumenta il conteggio di 1
    if(cnt>50):                            # Quando arriva a 50 punti elimina i primi dall'array
        tempC.pop(0)                       #Ci consente di vedere i primi 50 punti
        pressure.pop(0)
