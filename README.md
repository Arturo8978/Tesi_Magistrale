# Tesi_Magistrale
Codici Python e Arduino per plottaggio, analisi dati e gestione sensori



Nel seguente progetto sono contenuti i codici python per la gestione dei dati rilevati mediante il sensore BMP180 di temperatura e pressione. In particolare:

- realTime_da_file.py prende i dati di temperatura e pressione da un file .csv (acquisiti con un monitor seriale come RealTerm) e li plotta nel diagramma p-T in tempo reale;
- realTime_da_posta_seriale.py fa lo stesso lavoro del codice precedente, ma acquisendo direttamente da porta seriale i dati (cammo impostati nel codice ba baud rate e la corta COM??);
- regressione_p_T.py restituisce i parametri di regressione lineare tra una colonna di dati in temperatura e una colonna in pressione, prelevati sempre da un file.csv;
- reg_and_plot.py restituisce il grafico di pressione in funzione della temperatura dei dati prelevati da un file.csv, grafica inoltre la retta di regressione lineare e mostra il punto di intersezione di quest'ultima con l'asse delle temperature fornendo così una stima di T_0.

Inoltre sono qui contenuti i codici (.ino) per la gestione del sensore e del potenziometro nelle divers configurazioni descritte nella tesi.


Per dubbi, chiarimenti e segnalazione errori contattatemi alla e-mail: fra.guida@outlook.com
