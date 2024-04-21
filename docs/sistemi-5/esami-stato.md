# Esami di Stato

## Sessione ordinaria 2018

Il candidato svolga la prima parte della prova e due tra i quesiti proposti nella
seconda parte. 

### Prima parte

All’interno di un prosciuttificio è presente una stazione di smistamento dei prosciutti per
procedere alle operazioni di marchiatura selezione per la vendita e timbratura.
I prosciutti vengono posti su un nastro trasportatore e arrivano su una piattaforma girevole
e provvista di una cella di carico con portata di fondo scala pari a 150 N, dove vengono
pesati e successivamente distribuiti in funzione del loro peso.
Il nastro trasportatore di arrivo alla piattaforma si ferma per 5 secondi per permettere
l’operazione di pesatura, al termine della quale, in base al peso, il prosciutto viene
smistato.
I prosciutti di peso inferiore a 5 kg vengono convogliati verso uno scivolo di raccolta posto
a 180° per destinarli ad altri usi.
Gli altri vengono indirizzati verso due nastri trasportatori, posti rispettivamente a 90° e
270° rispetto al nastro di arrivo attorno alla piattaforma.
In particolare se il peso è compreso tra 5 e 10 kg la base ruota di 90° verso destra, se il
peso supera i 10 kg la base ruota di 90° verso sinistra.
Alla fine dei due nastri è posto un contenitore di raccolta, che una volta pieno determinerà
un arresto temporaneo del sistema per permettere all’operatore la sua sostituzione.
La rotazione della piattaforma è affidata ad un opportuno motore, mentre lo spostamento
del prosciutto dalla base ruotante alla linea di destinazione è affidato ad una serie di micro
rulli solidali alla base rotante stessa e azionati da un ulteriore motore.
Ogni linea di smistamento è provvista di un opportuno sensore che permette il conteggio
dei prosciutti commerciabili da quelli destinati ad altri usi.
Il candidato, fatte le ulteriori ipotesi aggiuntive che ritiene necessarie:

1. descriva l’impianto attraverso uno schema e individui i dispositivi necessari alla sua
realizzazione, fornendo una tabella di I/O rappresentante i principali segnali elettrici di
controllo;

2. rappresenti mediante un diagramma di flusso di propria conoscenza, l’algoritmo di
gestione dell’impianto;

3. elabori il programma in grado di gestire l’automatismo utilizzando un sistema
programmabile di propria conoscenza;

4. progetti un sistema in grado di effettuare una stima percentuale dei prosciutti
commerciabili da quelli destinati ad altri usi.
Inoltre, il candidato progetti un idoneo sistema di segnalazioni luminose nelle fasi di
movimentazione dei nastri, nonché i pulsanti di marcia e arresto dell’impianto.

**Soluzione:**

Di seguito viene riportato lo schema dell'impianto.

<figure markdown="span">
  ![Image title](images/esame2018_schema.svg){ width="500" }
  <figcaption markdown="span">
    Schema dell'impianto
  </figcaption>
</figure>

Di seguito, sono riportatati i dispositivi di input:

| Codice      | Descrizione                          |
| ----------- | ------------------------------------ |
| PB1      | Pulsante di avvio NA                 |
| PB2      | Pulsante di stop (gestito) NC        |
| PBE      | Pulsante di emergenza a fungo NC     |
| PS1       | Fotocellula rilevamento prosciutto linea di arrivo|
| PS2       | Fotocellula rilevamento prosciutto contenitore di raccolta da 5 a 10 Kg|
| PS3       | Fotocellula rilevamento prosciutto scivolo di raccolta minore di 5 Kg|
| PS4       | Fotocellula rilevamento prosciutto contenitore di raccolta maggiore di 10 Kg|
| FS1       | Sensore di riempimento contenitore di raccolta da 5 a 10 Kg|
| FS2       | Sensore di riempimento contenitore di raccolta maggiore di 10 Kg|
| SB1       | Sensore di finecorsa che indica la rotazione di 0°|
| SB2       | Sensore di finecorsa che indica la rotazione di 90° a destra|
| SB3       | Sensore di finecorsa che indica la rotazione di 90° a sinistra|


Di seguito, sono riportatati i dispositivi di output:

| Codice      | Descrizione                          |
| ----------- | ------------------------------------ |
| M1          | Motore nastro trasportatore linea di arrivo                 |
| M2          | Motore nastro trasportatore linea da 5 a 10 Kg                 |
| M3          | Motore nastro trasportatore linea maggiore di 10 Kg                 |
| M4          | Motore piattaforma girevole                 |
| M5          | Motore micro rulli               |
| L1          | Lampada di segnalazione bianca (macchina in tensione)               |
| L2          | Lampada di segnalazione verde (macchina in funzione)               |
| L3          | Lampada di segnalazione blu (azione richiesta)               |
| L4          | Lampada di segnalazione gialla (anomalia)               |
| L5          | Lampada di segnalazione rossa (condizione di emergenza)               |

Nella prima parte del programma, vengono gestiti i pulsanti e le luci di segnalazione. La variabile Stop indica che è stato richiesto uno stop, che può avvenire perché il pulsante di stop è stato premuto, oppure perché uno dei contenitori è pieno. Il pulsante di stop ha effetto solo una volta terminato lo smistamento del prosciutto corrente in modo da lasciare la macchina in uno stato gestito.

<figure markdown="span">
  ![Image title](images/esame2018_ladder.svg){ width="500" }
  <figcaption markdown="span">
    Programma Ladder: gestione dei pulsanti e segnalazioni.
  </figcaption>
</figure>

### Seconda parte