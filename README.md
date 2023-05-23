# Tesi_Magistrale

Codici Arduino per la gestione del microcontrollore Arduino Uno, del sensore di temperatura e pressione BMP180 e del potenziometro, così come illustrato nel lavoro di tesi:

- Il file **siringa.ino** è quello per la gestione del potenziometro e del sensore BMP180 nell'esperienza di Boyle
(NOTA: la calibrazione del potenziometro è strettamente legata alla geometria della siringa, andrebbe verificata oppure rifatta);

- Il file **solo_sensore_termometro_gas.ino** è il codice arduino per la gestione del solo sensore BMP180 nel caso dell'esperimento del termometro a gas;

- il file **sensor_and:BLE.ino** è il codice per la gestione del sensore BMP180 e del modulo bluetooth HC05 nell'esperienza della seconda legge di Gay Lussac e nel primo esperimento del termometro a gas.

Per il plottaggio dei dati in tempo reale è stato utilizzato il software KST scaricabile al seguente link:
https://kst-plot.kde.org/download.html

Per la gestione della comunicazione seriale tra scheda ArduinoUno\PC e il salvataggio dei dati è stato utilizzato il monitor seriale RealTerm scaricabile al seguente link: https://realterm.sourceforge.io/#Installing_Realterm

Le informazioni per il settaggio di KST e di RealTerm sono contenute nel terzo capitolo della tesi.

Quasi tutti i componenti sono disponibili su Amazon.it:

- https://amzn.to/43hWfdX (link per l'acquisto di due modulo bluetooth HC05);
- https://amzn.to/3IASMP4 (link per l'acquisto di tre sensori BMP180 di temperatura e pressione);
- https://amzn.to/3BPHX8f (link per l'acquisto di cinque potenziometri a slitta da 10Kohm. ATTENZIONE: i potenziometri in questione dovrebbero essere lineare, ma capita spesso che vengono inviati potenziometri logaritmici contrariamente a quanto ripostato nella descrizione. In tal caso è possibile rispedire indietro il prodotto oppure tenere conto di questo fatto ed eseguire una opportuna calibrazione);
- https://amzn.to/43nlCKU (link per l'acquisto delle basette millefori per il cablaggio dell'hardware come descritto in tesi);
- https://amzn.to/3OxcEGN (link per l'acquisto della scheda a microcontrollore Arduino Uno, in alternativa è possibili acquistare la scheda arduino nano BLE che comprende già un sistema bluetooth integrato al link https://amzn.to/3IxH3Rt);
- Una siringa da 50 mL acquistabile in qualsiasi farmacia al prezzo di 2 euro circa;
- Tubi in gomma di collegamento da 4/5mm di diamentro interno, acquistabili in ferramenta;
- Cavo piattino telefonico 4x1 per collegre il potenziometro, acquistabile in negozio di materiale elettrico;
- Colla a caldo per fissare il potenziometro alla siringa;
- Valvola di sfiato a 3 vie per l'esperienza di Boyle, acquistabile in farmacia (opzionale).


Per dubbi, ulteriori chiarimenti e segnalazione errori contattatemi alla e-mail: fra.guida@outlook.com



Riportiamo inoltre alcuni codici python per l'analisi e il plottaggio dei dati che però non sono descritti nel progetto di tesi, ma che comunque sono stati testati.

- realTime_da_file.py prende i dati di temperatura e pressione da un file .csv (acquisiti con un monitor seriale come RealTerm) e li plotta nel diagramma p-T in tempo reale;
- realTime_da_posta_seriale.py fa lo stesso lavoro del codice precedente, ma acquisendo direttamente da porta seriale i dati (cammo impostati nel codice ba baud rate e la corta COM??);
- regressione_p_T.py restituisce i parametri di regressione lineare tra una colonna di dati in temperatura e una colonna in pressione, prelevati sempre da un file.csv;
- reg_and_plot.py restituisce il grafico di pressione in funzione della temperatura dei dati prelevati da un file.csv, grafica inoltre la retta di regressione lineare e mostra il punto di intersezione di quest'ultima con l'asse delle temperature fornendo così una stima di T_0.





