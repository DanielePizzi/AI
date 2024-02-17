## cos'è la varianza?
La varianza è la media dei quadrati delle differenze tra ciascun valore e la media.
La viarianza misura quanto una singola variabile si allontana dalla media, o comunque dal valore 
atteso.
La varianza calcola il rumore del dataset.  Il rumore identifica i dati che sono molto lontani dalla media.

## cos'è il bias e perchè un modello con bias elevato viene detto underfitting?
Sarebbe il pregiudizio con cui alleno il modello. Per esempio se ho dieci caratteristiche, e decido
di allenare il modello solo su una caratteristica, ho introdotto un bias, in quanto ho introdotto
un pregiudizio su quale caratteristicha è piu importante analizzare.

## perchè un modello con varianza elevata viene detto overfitting?
Se ho varianza elevata nel mio dataset, significa che nel mio dataset sono presenti molti dati 
di rumore, ovvero molti dati che si allontanano dalla media(o da un valore atteso).Utilizzare
questo dataset per l'apprendimento automatico, può portare ad un modello iper adattato, che 
non riesce quindi a generalizzare i dettagli. Quindi il modello memorizza i dettagli e i rumore
presenti nel dataset, invece cha apprendere i pattern.
Questo succede quando il modello diventa troppo complesso e inizia a catturare anche il rumore
nei dati. Se il modello ha varianza elevata, si può pensare di eliminare caratteristiche(feature).

## Perchè usare la regressione lineare nell'addestramento supervisionato?
è un modo per minimizzare gli errori . MI permette di trovare una retta che in media
sia piu vicina a tutti i miei punti. La discesa del gradiente è uno dei metodi utilizzati 
per minimizzare l'errore.

## cosa si intende per deviazione standard?
la deviazione standard è la radice quadrata della varianza. Il motivo è che cosi ho un metro di paragone, utilizzando la stessa unità di misura.
Serve a me per poter interpretare meglio i dati.
In pratica, indica quanto i dati sono distribuiti attorno alla media. Più è alta la deviazione standard, maggiore è la dispersione dei dati; al contrario, una deviazione standard bassa indica che i dati sono più vicini alla media.

## porre la deviazione standard ad 1 mi facilità nelle comprensione del bias e della varianza in un algoritmo di IA?
Ridurre la deviazione standard a 1 può facilitare la comprensione del trade-off tra bias e varianza in un algoritmo di intelligenza artificiale.
Bias: Il bias si riferisce all'errore introdotto dall'assunzione semplificativa fatta da un modello durante il processo di apprendimento. Un bias elevato può indicare che il modello non è sufficientemente complesso da catturare la relazione tra le variabili di input e di output. In termini di deviazione standard, se la deviazione standard del modello è bassa (vicino a 1), ciò potrebbe indicare che il modello è ben adattato ai dati di addestramento e quindi ha un basso bias.
Varianza: La varianza si riferisce alla sensibilità del modello alle piccole variazioni nei dati di addestramento. Una varianza elevata può indicare che il modello è troppo sensibile al rumore nei dati di addestramento e potrebbe non generalizzare bene su nuovi dati. In termini di deviazione standard, se la deviazione standard del modello è alta, ciò potrebbe indicare una varianza elevata, poiché i risultati del modello possono variare notevolmente da un set di dati all'altro.
Quindi, se riduci la deviazione standard a 1, stai essenzialmente standardizzando il modello, il che significa che il modello si adatta bene ai dati di addestramento senza essere troppo sensibile al rumore o agli outlier. Tuttavia, è importante trovare un equilibrio tra bias e varianza per ottenere prestazioni ottimali del modello su nuovi dati.
