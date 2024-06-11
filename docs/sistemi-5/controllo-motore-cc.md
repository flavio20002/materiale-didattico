---
comments: true
---

# Controllo di un motore in corrente continua

In questo capitolo, andremo ad analizzare un esempio di controllo analogico per un motore a corrente continua che fa uso di una dinamo tachimetrica.

## Schema di principio

Partiamo dallo schema del generico sistema di controllo di tipo proporzionale:

<figure markdown="span">
  ![Image title](images/controllo-proporzionale-motore.svg)
  <figcaption markdown="span">
    Sistema di controllo proporzionale.
  </figcaption>
</figure>

La cui funzione di trasferimento vale:

$$ G(s) = \frac{\Omega(s)}{ V_{\text{REF}}} (s)  =  \frac{G_M (s) \cdot K_P}{1+G_M (s) \cdot K_P \cdot  H} $$

Analizzando lo schema del sistema di controllo con regolatore proporzionale, si può notare che questo non è adatto al controllo di un motore in corrente continua. In caso di errore negativo, il controllo proporzionale genera una tensione negativa per rallentare il motore, invertendo il senso di rotazione del motore. Questa tensione negativa induce una corrente nel motore pari al doppio della corrente di spunto che può mettere sotto stress il motore fino a danneggiarlo. Usiamo quindi un sistema di controllo modificato:

<figure markdown="span">
  ![Image title](images/controllo-proporzionale-motore-modificato.svg)
  <figcaption markdown="span">
    Sistema di controllo per motore in CC
  </figcaption>
</figure>

Calcoliamo la funzione di trasferimento complessiva del sistema. La funzione di trasferimento del motore può essere scritta come:

$$ G_{\text{M}} (s) = \frac{K_M}{(1+ \tau_m s) \cdot (1+\tau_e s)}$$

dove $\tau_m$ è la costante di tempo meccanica del motore, $\tau_e$ è la costante di tempo elettrica del motore e $K_M$ è il guadagno statico del motore.

Il segnale di errore $E$ vale:

$$ E(s) = V_{\text{REF}}(s) - H \cdot \Omega (s) $$

Il segnale di uscita $\Omega (s)$ vale:

$$ \Omega(s) = G_M (s) \cdot (V_{\text{REF}}(s) \cdot K_R + K_P \cdot E(s)) $$

Ovvero:

$$\begin{split}
\Omega(s) & = G_M (s) \cdot (V_{\text{REF}}(s) \cdot K_R + K_P \cdot (V_{\text{REF}}(s) - H \cdot \Omega (s))) \\
 & = G_M (s) \cdot V_{\text{REF}}(s) \cdot K_R + G_M (s) \cdot K_P \cdot V_{\text{REF}}(s) - G_M (s) \cdot K_P \cdot  H \cdot \Omega (s)
\end{split}$$

Ed infine otteniamo:

$$ G(s) = \frac{\Omega(s)}{ V_{\text{REF}} (s)}  =  \frac{G_M (s) \cdot (K_P+K_R)}{1+G_M (s) \cdot K_P \cdot  H} $$

Analizziamo il funzionamento statico di questo sistema di controllo. Una volta terminati i transitori, infatti, $G_M(s) = K_M$

$$ \omega _\infty = V_{\text{REF}} \cdot  \frac{K_M \cdot (K_P+K_R)}{1+K_M \cdot K_P \cdot  H}  $$

Scegliendo opportunamente i valori delle costanti, possiamo ottenere:


## Implementazione con amplificatori operazionali

# Dimensionamento del segnale di riferimento

Per poter impostare il segnale di riferimento, si suppone che la velocità angolare d'uscita debba essere regolata fra due valori, chiamati $\omega_{\text{min}}$ e $\omega_{\text{max}}$. La tensione $V_{\text{ref}}$ prelevata dal partitore con l'inseguitore di tensione, può essere calcolata con la formula:

$$ V_{\text{REF}} = \frac{E}{R_1+R_2+R_3} [(1-\gamma) R_1 + R_3] $$

dove $\gamma$ varia tra 0 e 1 e rappresenta la posizione del cursore della resistenza variabile.
Si possono quindi ricavare le tensioni massime e minime di riferimento per i due valori limite di $\gamma$:

$$ \begin{cases}
  V_{\text{ref}}^{\text{min}} =  \dfrac{E}{R_1+R_2+R_3}  (R_3) \\[10pt]
  V_{\text{ref}}^{\text{max}} =  \dfrac{E}{R_1+R_2+R_3}  (R_1 + R_3)
\end{cases}\, $$

Le resistenze devono essere scelte in modo che la corrente non sia troppo eccessiva e quindi dissipare potenza inutilmente e troppo ridotta, tale da essere sensibile a disturbi esterni. La corrente dovrebbe essere quindi nell'ordine di 1 mA.

## Amplificatore differenziale

L'amplificatore differenziale deve sottrarre dal segnale di riferimento il segnale proveniente dal trasduttore. È possibile dunque utilizzare una configurazione a guadagno unitario in cui tutte le resistenza sono uguali e possono essere scelte nell'ordine di 1 k$\Omega$.

## S

