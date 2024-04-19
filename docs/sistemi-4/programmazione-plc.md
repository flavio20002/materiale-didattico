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

Il Function Block TON (Timer ON Delay) è utilizzato per creare un ritardo temporizzato.

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

Il Function Block TON (Timer ON Delay) è utilizzato per creare un ritardo temporizzato ed il suo funzionamento è duale rispetto al blocco TON.

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

### Rising Edge Trigger (F_TRIG)

Il Function Block F_TRIG (Falling Edge Trigger) è utilizzato per rilevare un fronte di discesa (passaggio da livello logico **TRUE** a livello logico **FALSE**) sull'ingresso CLK.

<figure markdown="span">
  ![Image title](images/F_TRIG.svg){ width="300" }
  <figcaption markdown="span">
    Blocco funzione F_TRIG
  </figcaption>
</figure>

Di seguito viene descritto il principio di funzionamento.

- Quando il segnale di ingresso CLK passa da livello logico **TRUE** a livello logico **FALSE**, l'uscita Q viene portata a livello logico **TRUE** solamente per un ciclo del PLC.

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

## Macchina a Stati

## Ambiente di sviluppo TwinCAT

### Installazione

[Scarica TC31-FULL-Setup.3.1.4024.44.exe](https://drive.google.com/file/d/1ebump_CRpeMDpodTEIvXfvRQp7_5mQY3/view?usp=sharing){:target="_blank"}

<div class="video-wrapper">
  <iframe src="https://www.youtube.com/embed/GzbMc2GxRYY" frameborder="0" allowfullscreen></iframe>
</div>

### Il primo progetto

<div class="video-wrapper">
  <iframe src="https://www.youtube.com/embed/GVevocz6wfI" frameborder="0" allowfullscreen></iframe>
</div>

### HMI

<div class="video-wrapper">
  <iframe src="https://www.youtube.com/embed/1uTgwMqExw8" frameborder="0" allowfullscreen></iframe>
</div>

### Temporizzazioni

<div class="video-wrapper">
  <iframe src="https://www.youtube.com/embed/PPws5IBSID4" frameborder="0" allowfullscreen></iframe>
</div>


### Macchina a stati: semaforo

<div class="video-wrapper">
  <iframe src="https://www.youtube.com/embed/JZzBVN1RTCc" frameborder="0" allowfullscreen></iframe>
</div>

[Scarica il progetto](files/Progetto5-Macchina a Stati ST.tnzip)

### Macchina a stati: Carrello

Realizzare un progetto TwinCAT usando la struttura della macchina a stati in linguaggio ST che controlli il movimento in due versi (sinistra e destra) di un carrello con le seguenti caratteristiche:

- La HMI deve avere questo aspetto:

<figure markdown="span">
  ![Image title](images/carrello.gif){ width="300" }
  <figcaption markdown="span">
    HMI del progetto Carrello
  </figcaption>
</figure>

 - Il Function Block chiamato FB_StateMachine ha queste caratteristiche:

    * Gli stati sono 4: stop con prossimo movimento a destra (stato iniziale), movimento a destra, movimento a sinistra, stop con prossimo movimento a sinistra.
    * Gli input sono 4: pulsante start, pulsante stop, FC sinistra e FC destra. La gestione dei sensori finecorsa è gestita dalla posizione del carrello sullo schermo.
    * Gli output sono 2: Motore destra e Motore sinistra.

  - Il Function Block chiamato FB_VisuManager ha queste caratteristiche:

    * Gestisce la posizione del carrello (coordinata x)
    * Gli input sono 2: Motore destra e Motore sinistra che userà per incrementare o decrementare la coordinata.
    * Gli output sono 2: FC destra e FC sinistra a seconda se il carrello ha raggiunto il punto iniziale o quello finale.


### Esecuzione su target remoto