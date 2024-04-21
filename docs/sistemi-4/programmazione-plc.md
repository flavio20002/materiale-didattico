# Programmazione dei PLC

In questa sezione sono descritti i principi per la programmazione dei PLC

## Caratteristiche di un PLC

Il PLC (Programmable Logic Controller) è un dispositivo utilizzato nell'ambito dell'automazione industriale. Presenta molte caratteristiche in comune con i Personal Computer, ma al contrario di questi è progettato per un funzionamento continuo (H24) ed in condizioni di temperatura, umidità o polvere più proibitive.
Il PLC ha progressivamente sostituito la logica cablata nell'ambito dell'automazione industriale per i seguenti motivi:

- Possibilità di riprogrammare il sistema automatico senza modifiche hardware.
- Minor presenza di parti in movimento (relè elettromeccanici).
- Minore consumo di elettricità.
- Minore costo di realizzazione.

## Linguaggio Ladder

## Blocchi funzione

Un Blocco Funzione FB (Function Block) è una POU (Program Organization Unit) che, a fronte di uno più ingressi, restituisce uno o più uscite. Non può essere richiamato direttamente, ma dev'essere dichiarato sotto forma di istanza. Ogni istanza ha uno stato di memoria (tramite l'utilizzo di variabili interne) che persiste tra una chiamata e l'altra dell'istanza del blocco funzione.

### Timer on-delay (TON)

Il Function Block TON (Timer on-delay) è utilizzato per creare un ritardo temporizzato.

<figure markdown="span">
  ![Image title](images/TON.svg){ width="300" }
  <figcaption markdown="span">
    Blocco funzione TON
  </figcaption>
</figure>

Di seguito viene descritto il principio di funzionamento.

- L'ingresso di abilitazione (IN) determina se il blocco è abilitato o disabilitato. Finché l'ingresso rimane a livello logico **FALSE**, il blocco è disabilitato e l'uscita Q è a livello logico **FALSE**. Quando invece viene portato a **TRUE**, il blocco inizia a contare il tempo trascorso. Il tempo trascorso è disponibile nell'uscita Elapsed TIme (ET).

- L'ingresso Preset Time (PT) definisce la durata del ritardo temporizzato. Quando il tempo trascorso supera il tempo impostato nell'ingresso PT, l'uscita Q viene posta a livello logico **TRUE** e vi permane finché il segnale IN rimane a livello logico **TRUE**.

- Se l'ingresso IN viene posto a **FALSE** prima che il tempo PT sia trascorso, l'uscita Q non assumerà il valore logico **TRUE**.

- Per effettuare un altro conteggio, l'ingresso IN deve essere portato a livello logico **FALSE** e successivamente a livello logico **TRUE**.

### Timer off-delay (TOF)

Il Function Block TOF (Timer off-delay) è utilizzato per creare un ritardo temporizzato ed il suo funzionamento è duale rispetto al blocco TON.

<figure markdown="span">
  ![Image title](images/TOF.svg){ width="300" }
  <figcaption markdown="span">
    Blocco funzione TOF
  </figcaption>
</figure>

- L'ingresso di abilitazione (IN) determina se il blocco è abilitato o disabilitato. Finché l'ingresso rimane a livello logico **TRUE**, il blocco è disabilitato e l'uscita Q è a livello logico **TRUE**. Quando invece viene portato a **FALSE**, il blocco inizia a contare il tempo trascorso. Il tempo trascorso è disponibile nell'uscita Elapsed TIme (ET).

- L'ingresso Preset Time (PT) definisce la durata del ritardo temporizzato. Quando il tempo trascorso supera il tempo impostato nell'ingresso PT, l'uscita Q viene posta a livello logico **FALSE** e vi permane finché il segnale IN rimane a livello logico **FALSE**.

- Se l'ingresso IN viene posto a **TRUE** prima che il tempo PT sia trascorso, l'uscita Q non assumerà il valore logico **FALSE**.

- Per effettuare un altro conteggio, l'ingresso IN deve essere portato a livello logico **TRUE** e successivamente a livello logico **FALSE**.

### Pulse Timer (TP)

Il Function Block TP (Pulse timer) è utilizzato per generare un impulso di durata predefinita.

<figure markdown="span">
  ![Image title](images/TP.svg){ width="300" }
  <figcaption markdown="span">
    Blocco funzione TP
  </figcaption>
</figure>

Di seguito viene descritto il principio di funzionamento.

- L'ingresso di abilitazione (IN) determina se il blocco è abilitato o disabilitato. Finché l'ingresso rimane a livello logico **FALSE**, il blocco è disabilitato e l'uscita Q è a livello logico **FALSE**. Quando invece viene portato a **TRUE**, l'uscita Q viene portata a livello logico **TRUE**.

- L'ingresso Preset Time (PT) definisce la durata dell'impulso temporizzato. Quando il tempo trascorso supera il tempo impostato nell'ingresso PT, l'uscita Q viene posta a livello logico **FALSE**.

- Se l'ingresso IN viene posto a **FALSE** prima che il tempo PT sia trascorso, l'uscita Q rimane comunque a livello logico **TRUE** finché non è trascorso il tempo impostato in PT.

- Per generare un altro impulso, l'ingresso IN deve essere portato a livello logico **FALSE** e successivamente a livello logico **TRUE**.

### Rising Edge Trigger (R_TRIG)

Il Function Block R_TRIG (Rising Edge Trigger) è utilizzato per rilevare un fronte di salita (passaggio da livello logico **FALSE** a livello logico **TRUE**) sull'ingresso CLK.

<figure markdown="span">
  ![Image title](images/R_TRIG.svg){ width="300" }
  <figcaption markdown="span">
    Blocco funzione R_TRIG
  </figcaption>
</figure>

Di seguito viene descritto il principio di funzionamento.

- Quando il segnale di ingresso CLK passa da livello logico **FALSE** a livello logico **TRUE**, l'uscita Q viene portata a livello logico **TRUE** solamente per un ciclo del PLC.

### Falling Edge Trigger (F_TRIG)

Il Function Block F_TRIG (Falling Edge Trigger) è utilizzato per rilevare un fronte di discesa (passaggio da livello logico **TRUE** a livello logico **FALSE**) sull'ingresso CLK.

<figure markdown="span">
  ![Image title](images/F_TRIG.svg){ width="300" }
  <figcaption markdown="span">
    Blocco funzione F_TRIG
  </figcaption>
</figure>

Di seguito viene descritto il principio di funzionamento.

- Quando il segnale di ingresso CLK passa da livello logico **TRUE** a livello logico **FALSE**, l'uscita Q viene portata a livello logico **TRUE** solamente per un ciclo del PLC.

### Down Counter (CTD)

Il Function Block CTD (Down Counter) permette di contare all'indietro.

<figure markdown="span">
  ![Image title](images/CTD.svg){ width="300" }
  <figcaption markdown="span">
    Blocco funzione CTD
  </figcaption>
</figure>

Di seguito viene descritto il principio di funzionamento.

- Quando l'ingresso LOAD ha valore logico **TRUE**, la variabile di conteggio CV viene inizializzata con il valore contenuto nella variabile d'ingresso PV (preset value). Se la variabile di ingresso CD ha un fronte di salita da **FALSE** a **TRUE**, CV viene decrementato di 1, finché CV è maggiore di zero. Il valore di Q vale **TRUE** quando CV è minore o uguale a zero.

### Up Counter (CUD)

Il Function Block CUD (Down Counter) permette di contare in avanti.

<figure markdown="span">
  ![Image title](images/CUD.svg){ width="300" }
  <figcaption markdown="span">
    Blocco funzione CUD
  </figcaption>
</figure>

Di seguito viene descritto il principio di funzionamento.

- Quando l'ingresso RESET ha valore logico **TRUE**, la variabile di conteggio CV viene portata a valore 0. Se la variabile di ingresso CU ha un fronte di salita da **FALSE** a **TRUE**, CV viene incrementato di 1, finché CV è minore di PV. Il valore di Q vale **TRUE** quando CV è maggiore o uguale a PV.

### Bistabile reset dominante (RS)

Il Function Block RS è un bistabile con ingresso di reset dominante.

<figure markdown="span">
  ![Image title](images/RS.svg){ width="300" }
  <figcaption markdown="span">
    Blocco funzione RS
  </figcaption>
</figure>

Di seguito viene descritto il principio di funzionamento.

- Quando vi è un fronte di salita sull'ingresso SET, l'uscita Q va a livello logico *TRUE* e vi permane finché l'ingresso RESET1 non va a livello logico *TRUE*. Il reset ha la precedenza sul set.

### Bistabile set dominante (SR)

Il Function Block SR è un bistabile con ingresso di set dominante.

<figure markdown="span">
  ![Image title](images/SR.svg){ width="300" }
  <figcaption markdown="span">
    Blocco funzione SR
  </figcaption>
</figure>

Di seguito viene descritto il principio di funzionamento.

- Quando vi è un fronte di salita sull'ingresso SET1, l'uscita Q va a livello logico *TRUE* e vi permane finché l'ingresso RESET non va a livello logico *TRUE*. Il set ha la precedenza sul reset.

## Funzioni

Una funzione è una porzione di codice che può essere chiamata da un programma o un'altra POU. Le funzioni non vanno dichiarate e sono prive di memoria. Di seguito sono riportate le funzioni di uso più comune:

| Funzione      | Descrizione                          |
| ----------- | ------------------------------------ |
| `ADD`       | Somma due variabili  |
| `SUB`       | Sottrae una variabile da un'altra |
| `MUL`    | Moltiplica due variabili |
| `DIV`    | Esegue la divisione fra due variabili. |
| `MOD`    | Calcola il resto della divisione fra due variabili |
| `SQRT`    | Esegue la radice quadrata di una variabile |
| `EXP`    | Calcola la funzione esponenziale $e^x$ |
| `EXPT`    | Date in ingresso due variabili b e x, calcola la funzione $b^x$ |
| `EQ`    | Compara due variabili e restituisce TRUE se sono uguali |
| `NE`    | Compara due variabili e restituisce TRUE se sono diverse |
| `GE`    | Compara due variabili e restituisce TRUE se la prima è maggiore o uguale alla seconda |
| `GT`    | Compara due variabili e restituisce TRUE se la prima è maggiore alla seconda |
| `LE`    | Compara due variabili e restituisce TRUE se la prima è minore o uguale alla seconda |
| `LT`    | Compara due variabili e restituisce TRUE se la prima è minore alla seconda |


## Linguaggio ST

### IF

IF è usato per testare una condizione, ed eseguire le istruzioni successive solo al verificarsi della condizione. La condizione è rappresentata da un'espressione che ritorna un valore booleano, TRUE o FALSE. Se la condizione è verificata, le istruzioni successive sono eseguite. Altrimenti, viene testata la condizione successiva nel ramo chiamato ELSIF. Infine, se nessuna condizione è verificata, viene eseguito il codice contenuto nel ramo ELSE. I rami ELSIF ed ELSE sono opzionali.


``` iecst
VAR
    nTemp       : INT;
    bHeatingOn  : BOOL;
    bOpenWindow : BOOL;
END_VAR

IF nTemp < 17 THEN
    bHeatingOn  := TRUE;
ELSIF nTemp > 25 THEN
    bOpenWindow := TRUE;
ELSE
    bHeatingOn  := FALSE;
    bOpenWindow := FALSE;
END_IF;
```

### CASE

CASE è usato per verificare più condizioni sulla stessa variabile. Le condizioni vengono verificate in sequenza e l'istruzione termina quando viene raggiunta la prima condizione verificata. Se nessuna condizione viene verificata, vengono eseguite le istruzioni contenute nel ramo ELSE.


``` iecst
VAR
    int1       : INT;
    bool1      : BOOL;
    bool2      : BOOL;
    bool3      : BOOL;
END_VAR

CASE int1 OF
1, 5:  
    bool1 := TRUE;
    bool2 := FALSE;
2:     
    bool2 := FALSE;
    bool3 := TRUE;
ELSE
    bool1 := NOT BOOL1;
    bool2 := BOOL1 OR BOOL2;
END_CASE;
```

## Macchina a Stati

