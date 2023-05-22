# Tesi_Magistrale

Codici Arduino per la gestione del microcontrollore Arduino Uno, del sensore di temperatura e pressione BMP180 e del potenziometro, così come illustrato nel lavoro di tesi:

- Il file siringa.ino è quello per la gestione del potenziometro e del sensore BMP180 nell'esperienza di Boyle
(NOTA: la calibrazione del potenziometro è strettamente legata alla geometria della siringa, andrebbe verificata oppure rifatta);

- Il file solo_sensore_termometro_gas.ino è il codice arduino per la gestione del solo sensore BMP180 nel caso dell'esperimento del termometro a gas;

- il file sensor_and:BLE.ino è il codice per la gestione del sensore BMP180 e del modulo bluetooth HC05 nell'esperienza della seconda legge di Gay Lussac e nel primo esperimento del termometro a gas.

Per il plottaggio dei dati in tempo reale è stato utilizzato il software KST scaricabile al seguente link:
https://kst-plot.kde.org/download.html

Per la gestione della comunicazione seriale tra scheda ArduinoUno\PC e il salvataggio dei dati è stato utilizzato il monitor seriale RealTerm scaricabile al seguente link: https://realterm.sourceforge.io/#Installing_Realterm

Le informazioni per il settaggio di KST e di RealTerm sono contenute nel terzo capitolo della tesi.

Tutti i componenti sono disponibili su Amazon.it, a breve forniremo i link per chi volesse comprarli per replicare gli esperimenti.

Per dubbi, ulteriori chiarimenti e segnalazione errori contattatemi alla e-mail: fra.guida@outlook.com



Riportiamo inoltre alcuni codici python per l'analisi e il plottaggio dei dati che però non sono descritti nel progetto di tesi, ma che comunque sono stati testati.

- realTime_da_file.py prende i dati di temperatura e pressione da un file .csv (acquisiti con un monitor seriale come RealTerm) e li plotta nel diagramma p-T in tempo reale;
- realTime_da_posta_seriale.py fa lo stesso lavoro del codice precedente, ma acquisendo direttamente da porta seriale i dati (cammo impostati nel codice ba baud rate e la corta COM??);
- regressione_p_T.py restituisce i parametri di regressione lineare tra una colonna di dati in temperatura e una colonna in pressione, prelevati sempre da un file.csv;
- reg_and_plot.py restituisce il grafico di pressione in funzione della temperatura dei dati prelevati da un file.csv, grafica inoltre la retta di regressione lineare e mostra il punto di intersezione di quest'ultima con l'asse delle temperature fornendo così una stima di T_0.





