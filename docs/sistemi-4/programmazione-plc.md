# Programmazione dei PLC

In questa sezione sono descritti i principi per la programmazione dei PLC

## Caratteristiche di un PLC

## Linguaggio Ladder

## Blocchi funzione

Un Blocco Funzione FB (Function Block) è una POU (Program Organization Unit) che, a fronte di uno più ingressi, restituisce uno o più uscite. Non può essere richiamato direttamente, ma dev'essere dichiarato sottoforma di istanza. Ogni istanza ha uno stato di memoria (tramite l'utilizzo di variabili interne) che persiste tra una chiamata e l'altra dell'istanza del blocco funzione.

### Timer on-delay (TON)

Il Function Block TON (Timer ON Delay) è utilizzato per creare un ritardo temporizzato.

<figure markdown="span">
  ![Image title](images/TON.svg){ width="300" }
  <figcaption markdown="span">
    Blocco funzione TON
  </figcaption>
</figure>

Di seguito viene descritto il principio di funzionamento.

- L'ingresso di abilitazione (IN) determina se il blocco è abilitato o disabilitato. Finchè l'ingresso rimane a livello logico **FALSE**, il blocco è disabilitato e l'uscita Q è a livello logico **FALSE**. Quando invece viene portato a **TRUE**, il blocco inizia a contare il tempo trascorso. Il tempo trascorso è disponibile nell'uscita Elapsed TIme (ET).

- L'ingresso Preset Time (PT) definisce la durata del ritardo temporizzato. Quando il tempo trascorso supera il tempo impostato nell'ingresso PT, l'uscita Q viene posta a livello logico **TRUE** e vi permane finchè il segnale IN rimane a livello logico **TRUE**.

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

- L'ingresso di abilitazione (IN) determina se il blocco è abilitato o disabilitato. Finchè l'ingresso rimane a livello logico **TRUE**, il blocco è disabilitato e l'uscita Q è a livello logico **TRUE**. Quando invece viene portato a **FALSE**, il blocco inizia a contare il tempo trascorso. Il tempo trascorso è disponibile nell'uscita Elapsed TIme (ET).

- L'ingresso Preset Time (PT) definisce la durata del ritardo temporizzato. Quando il tempo trascorso supera il tempo impostato nell'ingresso PT, l'uscita Q viene posta a livello logico **FALSE** e vi permane finchè il segnale IN rimane a livello logico **FALSE**.

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

- L'ingresso di abilitazione (IN) determina se il blocco è abilitato o disabilitato. Finchè l'ingresso rimane a livello logico **FALSE**, il blocco è disabilitato e l'uscita Q è a livello logico **FALSE**. Quando invece viene portato a **TRUE**, l'uscita Q viene portata a livello logico **TRUE**.

- L'ingresso Preset Time (PT) definisce la durata dell'impulso temporizzato. Quando il tempo trascorso supera il tempo impostato nell'ingresso PT, l'uscita Q viene posta a livello logico **FALSE**.

- Se l'ingresso IN viene posto a **FALSE** prima che il tempo PT sia trascorso, l'uscita Q rimane comunque a livello logico **TRUE** finchè non è trascorso il tempo impostato in PT.

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

### Macchina a Stati